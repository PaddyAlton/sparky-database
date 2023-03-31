sparky-database
===============

An old learning project, provided here in case it helps someone in future.

Demonstrating that we can use docker-compose to bring up a mini Spark cluster and a postgres database and submit jobs that read CSV data and output it via JDBC.

Instructions
------------

- make sure you have installed `docker` and `docker-compose`
- run `docker-compose up`
- this should bring up four containers: a Spark 'master' node, two Spark 'worker' nodes, and a gateway container
- the last of these is to ensure that you're using compatible versions of python etc. when you try to submit pyspark jobs
- use `docker exec -it pyspark-gateway /bin/bash` to shell into the gateway container
- run `python src/main.py` to run the example job

If you have `psql` you can use `psql postgresql://postgres:postgres@localhost:5454/sparxcercise` to connect to the database (or you can use that connection string with any other DB utility) to verify that one of the CSVs has been read in and written to the database.
