import subprocess
import time
import requests

def test_hello_server():
    # Start the server
    server = subprocess.Popen(["python3", "app/main.py"])
    time.sleep(2)  # Wait for server to start

    try:
        response = requests.get("http://localhost:8080")
        assert response.status_code == 200
        assert "Hello from inside a Docker container" in response.text
    finally:
        server.terminate()
