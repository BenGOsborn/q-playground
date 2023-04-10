from typing import List
from enum import Enum


class CircuitType(Enum):
    MEASURE = "measure"
    INPUT = "input"
    OR = "or"
    AND = "and"
    NOT = "not"


# Derived using the q_operator span - how many extra bits does this operation add
OP_SPAN = {
    CircuitType.MEASURE: 0,
    CircuitType.INPUT: 1,
    CircuitType.OR: 3,
    CircuitType.AND: 1,
    CircuitType.NOT: 1
}


class CircuitNode:
    def __init__(self, children: List["CircuitNode"] = [], c_type: CircuitType = CircuitType.INPUT) -> "CircuitNode":
        self.children = children
        self.c_type = c_type
        self.out = None  # The output bit of the node

    def and_(self, node: "CircuitNode") -> "CircuitNode":
        return CircuitNode([self, node], CircuitType.AND)

    def or_(self, node: "CircuitNode") -> "CircuitNode":
        return CircuitNode([self, node], CircuitType.OR)

    def not_(self):
        return CircuitNode([self], CircuitType.NOT)

    def measure_(self):
        return CircuitNode([self], CircuitType.MEASURE)

    def __str__(self) -> str:
        return str(self.c_type)
