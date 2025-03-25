from django.shortcuts import render

from fastapi import FastAPI
from pydantic import BaseModel
from myapp.models import Item
from django.db import IntegrityError

app = FastAPI()

# Pydantic models for input validation
class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

@app.get("/items/", response_model=list[ItemResponse])
def get_items():
    items = Item.objects.all()
    return list(items.values())

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    try:
        item_obj = Item.objects.create(**item.dict())
        return ItemResponse(id=item_obj.id, **item.dict())
    except IntegrityError:
        return {"error": "Item creation failed"}

