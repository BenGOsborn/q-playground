from typing import List
from enum import Enum


class CircuitType(Enum):
    MEASURE = "measure"
    INPUT = "input"
    OR = "or"
    AND = "and"


class CircuitNode:
    def __init__(self, prev: List["CircuitNode"]) -> "CircuitNode":
        self.prev = prev
        self.type = CircuitType.INPUT
        self.out = None  # The output bit of the node

    def and_(self, node: "CircuitNode") -> "CircuitNode":
        temp = CircuitNode([self, node])
        temp.type = CircuitType.AND

        return temp

    def or_(self, node: "CircuitNode") -> "CircuitNode":
        temp = CircuitNode([self, node])
        temp.type = CircuitType.OR

        return temp

    def measure_(self):
        temp = CircuitNode([self])
        temp.type = CircuitType.MEASURE

        return temp

    def __str__(self) -> str:
        return str(self.type)
