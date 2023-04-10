from src.circuit import *
from src.circuit_node import CircuitNode, CircuitType

if __name__ == "__main__":
    circuit = CircuitNode().and_(CircuitNode()).or_(CircuitNode()).measure_()

    is_valid = is_valid_circuit([circuit])
    assert is_valid, "Invalid circuit"

    print_circuit([circuit])
    build([circuit])
