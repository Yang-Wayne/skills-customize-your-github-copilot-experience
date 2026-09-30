from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: Create a simple in-memory store for todo items.


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI todo API!"}


# TODO: Define a Pydantic model for todo items.


# TODO: Create a GET /todos endpoint.


# TODO: Create a POST /todos endpoint.


# TODO: Create a GET /todos/{todo_id} endpoint.
