# Apache Airflow Samples

This repository contains sample Workflow applications that demonstrate various capabilities of [Airflow](https://github.com/apache/airflow).

- Apache Airflow repo: hhttps://github.com/apache/airflow
- Apache Airflow docs: https://airflow.apache.org/docs/apache-airflow/stable/

## Table of Contents

- [Apache Airflow Samples](#apache-airflow-samples)
  - [Table of Contents](#table-of-contents)
  - [How to use](#how-to-use)
  - [Airflow Web UI](#airflow-web-ui)
  - [Samples directory](#samples-directory)
    - [Hello samples](#hello-samples)
  - [IDE Integration](#ide-integration)
    - [PyCharm](#intellij)

## How to use

1. Clone this repository:

       git clone https://github.com/misticorion/samples-airflow
       cd samples-airflow

2. Create virtual environment and install airflow:

       virtualenv env
       export AIRFLOW_HOME={PATH_OF_PROJECT}
       pip install apache-airflow==2.3.3

3. Run airflow locally with:

       airflow standalone


## Airflow Web UI

The Airflow Server running locally includes a Web UI, exposed by default on port 8080.
You can connect to the WebUI running using a browser and opening the following URI:

[http://localhost:8080/home](http://localhost:8080/home)


## Samples directory

The following section lists all available samples.
Click on the sample link to view the README, which contains instructions on how to run them.


### Hello samples

  - [**HelloWorld**](https://github.com/misticorion/samples-airflow/tree/main/dags/hello_world): Demonstrates a DAG Definition that executes a single Activity.


## IDE Integration

### PyCharm
