from django.db import models
from pydantic import BaseModel

# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.FloatField()

#     def __str__(self):
#         return self.name

class Item(BaseModel):
    name: str
    description: str
    price: float

