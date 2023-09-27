# BookWorm
A Tini Tiny Recommender System with software engineering diagrams and some other features


## Features

- UML Diagrams! you can see UML diagrams for each service in the reports/diagrams folder
- Network diagram! view the network relations between systems in reports/diagrams
- Docker graph! an efficient graph describing all kinds of communication between docker containers is available again in  reports/diagrams
- FastAPI! A brand new FastAPI is used for the system.
- Load Test Report! In reports/load_test you can find an HTML file which is a detailed report of a load test I did for the API using Locust.
- Unit Tests! In/test folder you can find a test file for each component


## Prerequisites

* docker engine
* docker-compose
* Python >= 3.6

## 

Clone the project

```bash
  git clone https://github.com/KianaLia/bookworm.git
```

After making sure you have the prerequisits installed, run the command below:

```bash
docker-compose -f "Bookworm\docker-compose.yml" up -d --build
```

Then, open the address below on your browser and on the /docs endpoint you will see the swagger UI of the API to use.

```bash
localhost:5020/docs
```