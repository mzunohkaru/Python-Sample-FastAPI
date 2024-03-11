from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    item: str


todos = []

# Get all todos
@app.get("/todos")
def get_todos():
    return {"Todos": todos}

# Get single todos
@app.get("/get/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"Todo": todo}
    return {"Message": "No found Todo"}


# Create a todo
@app.post("/create")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"Message": "Todo created successfully"}


# Update a todo
@app.put("/update/{todo_id}")
def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.item = todo_obj.item
            return {"Message": "Todo updated successfully"}
    return {"Message": "No found Todo"}


# Delete a todo
@app.delete("/delete/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"Message": "Todo deleted successfully"}
    return {"Message": "No found Todo"}

