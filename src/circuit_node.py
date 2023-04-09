from .operation import Operation
from typing import List


class CircuitNode:
    def __init__(self, prev: List["CircuitNode"]):
        self.prev = prev
        self.seen = False
        self.op = None

    def and_(self, node: "CircuitNode"):
        temp = CircuitNode([self, node])
        temp.op = Operation.AND

        return temp

    def or_(self, node: "CircuitNode"):
        temp = CircuitNode([self, node])
        temp.op = Operation.OR

        return temp
