# Prometheus and Grafana Metrics Demo

[![CI](https://github.com/ayusprasad/parmetheus-graphana/actions/workflows/ci.yml/badge.svg)](https://github.com/ayusprasad/parmetheus-graphana/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Metrics%20endpoint-000000?logo=flask&logoColor=white)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C?logo=prometheus&logoColor=white)

A small Flask service that exposes request counts and latency in Prometheus text format, with a Kubernetes scrape configuration.

## Architecture

~~~text
GET / → health-style JSON response
GET /metrics → Prometheus counter and latency gauge
Prometheus config → scrapes the Flask service
~~~

The metrics are measured by the Flask process. The /metrics scrape itself is excluded from the request counter to avoid recursive counting.

## Run locally

### Prerequisites

- Python 3.11 or newer

### Install and start

~~~bash
git clone https://github.com/ayusprasad/parmetheus-graphana.git
cd parmetheus-graphana
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
~~~

Open http://127.0.0.1:5000, then inspect http://127.0.0.1:5000/metrics. Set PORT to use a different port.

## Kubernetes

Apply the Flask deployment and service manifests, then apply prometheus-config.yaml in the Prometheus namespace after confirming the target service DNS name is correct for your cluster.

## Quality checks

~~~bash
pytest -q
ruff check --select E4,E7,E9,F app.py tests
~~~

GitHub Actions runs lint, tests, compilation, and a Docker build on pushes and pull requests.
