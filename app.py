from __future__ import annotations

import os
from time import perf_counter

from flask import Flask, jsonify, request

app = Flask(__name__)
request_count = 0
last_request_latency = 0.0


@app.before_request
def start_timer() -> None:
    request.environ["metrics.started_at"] = perf_counter()


@app.after_request
def record_request(response):
    global request_count, last_request_latency
    if request.path != "/metrics":
        request_count += 1
        start = request.environ.get("metrics.started_at")
        if start is not None:
            last_request_latency = max(0.0, perf_counter() - start)
    return response


@app.get("/")
def index():
    return jsonify({"message": "Metrics demo is ready.", "metrics_path": "/metrics"})


@app.get("/metrics")
def metrics():
    body = (
        "# HELP total_api_requests_total Number of non-metrics HTTP requests handled.\n"
        "# TYPE total_api_requests_total counter\n"
        f"total_api_requests_total {request_count}\n"
        "# HELP last_request_latency_seconds Duration of the latest non-metrics request.\n"
        "# TYPE last_request_latency_seconds gauge\n"
        f"last_request_latency_seconds {last_request_latency:.9f}\n"
    )
    return body, 200, {"Content-Type": "text/plain; version=0.0.4; charset=utf-8"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
