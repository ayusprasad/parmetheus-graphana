# 📈 Prometheus & Grafana Monitoring for Python Web Services

A complete observability stack demonstrating real-time metrics generation, scraping, and dashboard visualization using **Flask**, **Prometheus**, and **Grafana**.

---

## 🌟 Architecture & Endpoints
- **Flask Metrics Service (`:5000`)**: Exposes simulated metrics at `/metrics` conforming to OpenMetrics format (`total_api_requests_total`, `request_processing_latency_seconds`, `model_prediction_success_rate`).
- **Prometheus Scraper (`:9090`)**: Periodically scrapes the Flask app metrics every 5 seconds.
- **Grafana Visualizer (`:3000`)**: Interactive dashboard engine to graph requests, latency distribution, and SLO success rates.

---

## 🚀 Quickstart

### 1. One-Click Stack Run (Docker Compose)
```bash
docker-compose up --build
```
Once started:
- **Flask App:** [http://localhost:5000](http://localhost:5000) (Metrics: `/metrics`)
- **Prometheus UI:** [http://localhost:9090](http://localhost:9090)
- **Grafana Dashboard:** [http://localhost:3000](http://localhost:3000) *(User: `admin`, Password: `admin`)*

---

### 2. Standalone Local Run
```bash
pip install -r requirements.txt
python app.py
```
Open [http://localhost:5000](http://localhost:5000).

---

## 📁 Repository Structure
```text
parmetheus-graphana/
├── app.py                         # Flask metrics emitter
├── requirements.txt               # Dependencies
├── Dockerfile                     # Container for Flask service
├── docker-compose.yml             # Full stack (Flask + Prometheus + Grafana)
├── prometheus-fixed-config.yaml   # Prometheus scrape configuration
├── flask-app.yaml                 # Kubernetes deployment & service manifest
└── README.md                      # Stack documentation
```