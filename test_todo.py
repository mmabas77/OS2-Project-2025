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
def test_post_create():
    global todo_id
    response = requests.post(f"{BASE_URL}/todos", json={"task": "pytest todo"})
    assert response.status_code == 201
    data = response.json()
    assert "task" in data and "_id" in data
    todo_id = data["_id"]


@pytest.mark.run(order=2)
def test_get_all():
    global todo_id
    response = requests.get(f"{BASE_URL}/todos")
    assert response.status_code == 200
    data = response.json()
    assert any(todo["_id"] == todo_id for todo in data)


@pytest.mark.run(order=3)
def test_put_update():
    global todo_id
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json={"done": True})
    assert response.status_code == 200
    data = response.json()
    assert data["done"] is True


@pytest.mark.run(order=4)
def test_delete():
    global todo_id
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    assert response.status_code == 204
