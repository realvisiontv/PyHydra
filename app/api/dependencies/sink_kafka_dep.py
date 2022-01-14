import asyncio
from concurrent.futures import ThreadPoolExecutor as Executor
from threading import Thread

import confluent_kafka
from confluent_kafka import KafkaException


class AIOProducer:
    def __init__(self, configs, loop=None):
        self._loop = loop or asyncio.get_event_loop()
        self._producer = confluent_kafka.Producer(configs)
        self._cancelled = False
        # self._poll_thread = Thread(target=self._poll_loop)
        # self._poll_thread.start()
        self.executor = Executor()
        self._loop.set_default_executor(self.executor)

        self._loop.run_in_executor(None, self._poll_loop)

    def delivery_report(self, err, msg):
        """
        Reports the failure or success of a message delivery.
        Args:
            err (KafkaError): The error that occurred on None on success.
            msg (Message): The message that was produced or failed.
        Note:
            In the delivery report callback the Message.key() and
            Message.value() will be the binary format as encoded
            by any configured Serializers and not the same object
            that was passed to produce(). If you wish to pass the
            original object(s) for key and value to delivery report
            callback we recommend a bound callback or lambda where
            you pass the objects along.
        """
        if err is not None:
            print(
                "Delivery failed for User record {}: {}".format(msg.key(), err)
            )
            return
        print(
            f"User record {msg.key()} successfully produced to {msg.topic()}"
            f"[{msg.partition()}] at offset {msg.offset()}"
        )

    def _poll_loop(self):
        while not self._cancelled:
            self._producer.poll(0.1)

    def close(self):
        self._cancelled = True
        # self._poll_thread.join()
        self.executor.shutdown(wait=True)

    def produce(self, topic, value):
        """
        An awaitable produce method.
        """
        result = self._loop.create_future()

        def ack(err, msg):
            if err:
                self._loop.call_soon_threadsafe(
                    result.set_exception, KafkaException(err)
                )
            else:
                self._loop.call_soon_threadsafe(result.set_result, msg)

        self._producer.produce(topic, value, on_delivery=ack)
        return result


class Producer:
    def __init__(self, configs):
        self._producer = confluent_kafka.Producer(configs)
        self._cancelled = False
        self._poll_thread = Thread(target=self._poll_loop)
        self._poll_thread.start()

    def _poll_loop(self):
        while not self._cancelled:
            self._producer.poll(0.1)

    def close(self):
        self._cancelled = True
        self._poll_thread.join()

    def produce(self, topic, value, on_delivery=None):
        self._producer.produce(topic, value, on_delivery=on_delivery)
