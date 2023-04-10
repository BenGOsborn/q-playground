from src.circuit import *
from src.circuit_node import CircuitNode

if __name__ == "__main__":
    out = CircuitNode([]).and_(CircuitNode([])).or_(CircuitNode([])).measure_()

    print_circuit([out])

    pass
