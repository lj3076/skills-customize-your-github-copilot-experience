from fastapi import FastAPI

app = FastAPI(title="Item API")

items = [
    {"id": 1, "name": "Notebook", "price": 5.99},
    {"id": 2, "name": "Pen", "price": 1.50},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Item API"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item
