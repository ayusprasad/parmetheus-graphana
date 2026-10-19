import re

from app import app


def test_root_endpoint_returns_service_message() -> None:
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.json["metrics_path"] == "/metrics"


def test_metrics_endpoint_uses_prometheus_format() -> None:
    client = app.test_client()
    client.get("/")
    response = client.get("/metrics")
    text = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "# TYPE total_api_requests_total counter" in text
    match = re.search(r"total_api_requests_total (\\d+)", text)
    assert match is not None
    assert int(match.group(1)) >= 1
    assert "last_request_latency_seconds" in text


def test_scrape_does_not_increment_request_counter() -> None:
    client = app.test_client()
    client.get("/")
    first = client.get("/metrics").get_data(as_text=True)
    second = client.get("/metrics").get_data(as_text=True)
    first_count = re.search(r"total_api_requests_total (\\d+)", first)
    second_count = re.search(r"total_api_requests_total (\\d+)", second)
    assert first_count is not None and second_count is not None
    assert first_count.group(1) == second_count.group(1)
