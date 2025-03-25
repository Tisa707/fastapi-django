from fastapi import FastAPI, HTTPException
from myapp.models import Item

app = FastAPI()

# In-memory database for items
fake_items_db = {}

# Read all items
@app.get("/items/")
def get_items():
    return fake_items_db

# Create a new item
@app.post("/items/")
def  create_item(name: str, description: str, price: float):
    item_id = int(len(fake_items_db) or 0)+ 1
    fake_items_db[item_id] = {"name": name, "description": description, "price": price}
    return {"item_id": item_id, "item": {"name": name, "description": description, "price": price}}

# Get a single item by id
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]

# Update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_items_db[item_id] = item
    return {"item_id": item_id, "updated_item": item}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}
