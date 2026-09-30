# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework in Python. Students will learn how to define routes, accept JSON requests, return responses, and validate data with Pydantic models.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a minimal FastAPI application and run it locally to confirm that the server responds to requests.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Define a root endpoint at `/` that returns a welcome message.
- Run the app with `uvicorn` or a similar ASGI server.
- Example response:
```json
{"message": "Welcome to the FastAPI todo API!"}
```

### 🛠️ Build a Todo API

#### Description
Create endpoints for listing and creating todo items in memory.

#### Requirements
Completed program should:

- Define a `GET /todos` endpoint that returns all todo items.
- Define a `POST /todos` endpoint that accepts a JSON body.
- Store items in a simple in-memory list.
- Return each item with a unique ID, title, and completed status.
- Example request body:
```json
{
  "title": "Finish homework",
  "completed": false
}
```

### 🛠️ Add Retrieval and Validation

#### Description
Add a route for fetching one todo by ID and validate the request data using a Pydantic model.

#### Requirements
Completed program should:

- Define a `GET /todos/{todo_id}` endpoint.
- Return the matching item or a 404 error if the item does not exist.
- Use a Pydantic model to validate the request payload.
- Ensure that `title` is not empty and `completed` is a boolean value.
- Example response:
```json
{
  "id": 1,
  "title": "Finish homework",
  "completed": false
}
```
