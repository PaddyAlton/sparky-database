FROM docker.io/bitnami/spark:3

USER root

RUN pip install pyspark

WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/app"
