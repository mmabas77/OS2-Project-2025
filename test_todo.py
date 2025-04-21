import pytest
import subprocess
import requests
import time
import os

BASE_URL = "http://localhost:3000"
IMAGE_NAME = "student-todo-app"
CONTAINER_NAME = "student-todo-container"
todo_id = None


@pytest.mark.run(order=1)
def test_dockerfile_exists_and_valid():
    try:
        assert os.path.exists("Dockerfile")
    except Exception as e:
        pytest.fail(f"❌ No Dockerfile {e}")


@pytest.mark.run(order=2)
def test_build_docker_image():
    result = subprocess.run(
        ["docker", "build", "-t", IMAGE_NAME, "."],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    try:
        assert result.returncode == 0
    except Exception as e:
        pytest.fail(f"❌ Docker build failed:: {e}")


@pytest.mark.run(order=3)
def test_run_docker_container():
    subprocess.run(["docker", "rm", "-f", CONTAINER_NAME], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    subprocess.run([
        "docker", "run", "-d",
        "--network=host",
        "--name", CONTAINER_NAME,
        "-p", "3000:3000",
        IMAGE_NAME
    ], check=True)

    time.sleep(5)

    try:
        res = requests.get(f"{BASE_URL}/todos", timeout=5)
        assert res.status_code in [200, 404]
    except Exception as e:
        pytest.fail(f"❌ App did not start or not reachable: {e}")


@pytest.mark.run(order=4)
def test_post_create():
    global todo_id
    response = requests.post(f"{BASE_URL}/todos", json={"task": "pytest todo"})
    assert response.status_code == 201
    data = response.json()
    assert "task" in data and "_id" in data
    todo_id = data["_id"]


@pytest.mark.run(order=5)
def test_get_all():
    global todo_id
    response = requests.get(f"{BASE_URL}/todos")
    assert response.status_code == 200
    data = response.json()
    assert any(todo["_id"] == todo_id for todo in data)


@pytest.mark.run(order=6)
def test_put_update():
    global todo_id
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json={"done": True})
    assert response.status_code == 200
    data = response.json()
    assert data["done"] is True


@pytest.mark.run(order=7)
def test_delete():
    global todo_id
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 204
