# PyHydra

PyHydra is a web service that allows data replication to various sinks such as Kafka, S3 etc. 
The service delivers web clients' json payloads to Kafka topics asynchronously. While services for Kafka sinks are 
currently under development, support for other sink platforms will be added in the future.

# Project Dependencies

This project uses `Python 3.9` and `pip-tools version 6.4.0+` and `pip 21.2+`. Install the project dependencies
using `pip install -r requirements.txt`

# Setting up local development
- Create .env file. A minimal example that works for local development should include the following -
  ```
  BOOTSTRAP_SERVERS=localhost:9092
  ```
- Run a local single node kafka with `docker-compose -f docker-compose-cp.yml up -d`
- Run PyHra with `docker-compose up -d`

# Running application
```
uvicorn app.main:app --reload
```

## Available Endpoints

### Metadata
| Path     | HTTP Method | Description                                                                                                                        |
|----------|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| /health  | GET         | A summary overview of the overall health of the system.  Includes health checks for Kafka. (coming soon)                                        |
| /metrics | GET         | A collection of JVM-related memory and thread management metrics, including deadlocked threads, garbage collection run times, etc. (coming soon) |


### Sink Endpoints
| Path       | HTTP Method | Description                                                                          |
|------------|-------------|--------------------------------------------------------------------------------------|
| /sink | GET         | A list of all the registered sinks currently managed by PyHydra.                   |

### Kafka Sink Endpoints
| Path | HTTP Method | Description |
|------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /sink/kafka/schema | GET | Returns a list of all schemas managed by PyHydra. |
| /sink/kafka/schema/[NAME] | POST | Registers a new schema with the registry. Use this for both new and existing schemas; for existing schemas, compatibility will be checked prior to registration. |
| /sink/kafka/topic/ | GET | Returns _only_ the JSON for the latest schema. |
| /sink/kafka/topic//[NAME]/ | POST | Asynchronously Post a message to a Kafka Topic |