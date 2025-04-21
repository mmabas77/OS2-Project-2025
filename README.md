# 📝 ToDo API Assignment

Build a simple REST API with Node.js, Express, and MongoDB.

---

## ✨ Features to Implement

You must implement the following endpoints:

### 1. `POST /todos` – Create a todo (status code must be 201 on success)

**Request:**

```bash
curl -X POST http://localhost:3000/todos \
  -H "Content-Type: application/json" \
  -d '{"task": "Finish assignment"}'
```

**Response:**

```json
{
  "_id": "661fe0dbcf1aef8a5b5e0a1a",
  "task": "Finish assignment",
  "done": false
}
```

---

### 2. `GET /todos` – List all todos (status code must be 200 on success)

**Request:**

```bash
curl http://localhost:3000/todos
```

**Response:**

```json
[
  {
    "_id": "661fe0dbcf1aef8a5b5e0a1a",
    "task": "Finish assignment",
    "done": false
  },
  {
    "_id": "661fe1b9cf1aef8a5b5e0a1b",
    "task": "Submit project",
    "done": true
  }
]
```

---

### 3. `PUT /todos/:id` – Update a todo (status code must be 200 on success)

**Request:**

```bash
curl -X PUT http://localhost:3000/todos/661fe0dbcf1aef8a5b5e0a1a \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```

**Response:**

```json
{
  "_id": "661fe0dbcf1aef8a5b5e0a1a",
  "task": "Finish assignment",
  "done": true
}
```

---

### 4. `DELETE /todos/:id` – Delete a todo (status code must be 204 on success)

**Request:**

```bash
curl -X DELETE http://localhost:3000/todos/661fe0dbcf1aef8a5b5e0a1a
```

**Response:**

```json
{
  "message": "Todo deleted successfully"
}
```

---

## 📦 What to Build

- `Todo API`   — Implement the API in any framework you want. Node.js is recommended.
- `Dockerfile` — Containerize the app.

⚠️ **Do not include a docker-compose.yml**. We will run MongoDB separately.

---

## 🐳 Docker Instructions

To run Mongo locally:

```bash
docker run -d --name mongo -p 27017:27017 mongo
```

Then, build and run your app:

```bash
docker build -t todo-app .
docker run -p 3000:3000 --network="host" todo-app
```

---

# Finally, Write brief containing 5 lines at least about what you did here (Don't use AI)
