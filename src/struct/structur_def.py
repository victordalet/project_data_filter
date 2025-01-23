from pydantic import BaseModel
from typing import List


class Student(BaseModel):
    first_name: str
    last_name: str
    age: int
    apprentice: bool
    grades: List[int]


class Item(BaseModel):
    name: str
    category: str
    price: float
    quantity: int
