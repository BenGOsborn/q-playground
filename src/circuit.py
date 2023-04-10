from qiskit import QuantumCircuit
from typing import List
from src.circuit_node import CircuitNode, CircuitType


# Check if the circuit is valid
def is_valid_circuit(outputs: List["CircuitNode"]) -> bool:
    # All nodes in last layer should be measurement type
    valid_measures = {}

    for output in outputs:
        if output.c_type != CircuitType.MEASURE:
            return False
        valid_measures[output] = True

    # All leaf nodes should be inputs
    stack = outputs.copy()
    seen = {}

    while len(stack):
        node = stack.pop(-1)

        if node in seen:
            continue

        seen[node] = True

        if len(node.children) == 0 and node.c_type != CircuitType.INPUT:
            return False
        elif len(node.children) != 0 and node.c_type == CircuitType.INPUT:
            return False
        elif node not in valid_measures and node.c_type == CircuitType.MEASURE:
            return False

        for child in node.children:
            stack.append(child)

    return True


# Print the circuit
def print_circuit(outputs: List["CircuitNode"], tab_size=0):
    for node in outputs:
        print(("\t" * tab_size) + str(node))

        print_circuit(node.children, tab_size+1)


# Count the leaf nodes / inputs in the circuit
def count_inputs(outputs: List["CircuitNode"]) -> int:
    if len(outputs) == 0:
        return 1

    leaves = 0

    for node in outputs:
        leaves += count_inputs(node.children)

    return leaves


# Build the circuit
def build(outputs: List["CircuitNode"]) -> QuantumCircuit:
    # **** These numbers will be built by first assembling the graph, calling the operation on them, and then figuring out the number of inputs and outputs
    # **** We can figure out the number of inputs required by calculating the number of leaf nodes - in this case every leaf will correspond to a new hadamard
    return QuantumCircuit(1, 2)


if __name__ == "__main__":
    pass
