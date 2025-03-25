from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

# In-memory "database"
items = []

@app.get("/items/", response_model=List[Item])
def get_items():
    return items

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    return items.pop(item_id)
