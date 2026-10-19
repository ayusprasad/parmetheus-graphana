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
    assert "total_api_requests_total 1" in text
    assert "last_request_latency_seconds" in text


def test_scrape_does_not_increment_request_counter() -> None:
    client = app.test_client()
    client.get("/")
    client.get("/metrics")
    response = client.get("/metrics")
    assert "total_api_requests_total 1" in response.get_data(as_text=True)
