from enum import Enum

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


class FilterType(str, Enum):
    CONTAINS = "contains"
    EQUALS = "equals"
    STARTS_WITH = "starts_with"
    FINISH_WITH = "finish_with"
    IS_BELOW = "is_below"
    IS_ABOVE = "is_above"
