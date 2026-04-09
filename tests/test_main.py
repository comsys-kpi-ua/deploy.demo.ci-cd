import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_default_version(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"App Version: 1.0.1" in response.data


def test_hello_custom_version(client, monkeypatch):
    monkeypatch.setenv("APP_VERSION", "2.0.0")
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"App Version: 2.0.0" in response.data


def test_health_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"


def test_health_error_when_crash_file_exists(client, monkeypatch, tmp_path):
    crash_file = tmp_path / "crash.txt"
    crash_file.write_text("crash")
    monkeypatch.chdir(tmp_path)
    app.config["TESTING"] = True
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 500
