FROM python:3.9.0-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.in requirements.txt ./
RUN pip install pip-tools==6.4.0 && \
    pip install -r requirements.txt

COPY . ./

CMD uvicorn --host=0.0.0.0 app.main:app
