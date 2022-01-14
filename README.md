# PyHydra

PyHydra is a web api service open sourced by [Real Vision](realvision.com) that allows data replication to various sinks such as Kafka, S3 etc. 
The service delivers web clients' json payloads to Kafka topics asynchronously. While services for Kafka sinks are 
currently under development, support for other sink platforms will be added in the future.

## Project Dependencies

This project uses `Python 3.9` and `pip-tools version 6.4.0+` and `pip 21.2+`. Install the project dependencies
using `pip install -r requirements.txt`

## Setting up local development
- Create .env file. A minimal example that works for local development should include the following -
  ```
  BOOTSTRAP_SERVERS=localhost:9092
  ```
- Run a local single node kafka with `docker-compose -f docker-compose-cp.yml up -d`
- Run PyHydra with `docker-compose up -d` or without docker with `uvicorn app.main:app --reload`

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

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/realvisiontv/PyHydra/tags).

## Contributing
All changes to the code base start with creating an issue. When you have resolved the issue, you can request to merge your changes to th code base using a Pull Request. Please read through our [contributing guidelines](https://github.com/realvisiontv/PyHydra/blob/ab070d5bd8a3927827e5eb96fc99939d20d7686e/CONTRIBUTING.md) and our policy on [code of conduct](https://github.com/realvisiontv/PyHydra/blob/efda78268acbffc8a194e20f822547cdc7a6caa5/CODE_OF_CONDUCT.md)

## License
[Apache 2](https://choosealicense.com/licenses/apache-2.0/)
