from qiskit import QuantumCircuit
from typing import List
from src.circuit_node import CircuitNode


def print_circuit(outputs: List["CircuitNode"], tab_size=0):
    for node in outputs:
        print(("\t" * tab_size) + str(node))

        print_circuit(node.prev, tab_size+1)


def count_leaves(outputs: List["CircuitNode"]):
    if len(outputs) == 0:
        return 1

    leaves = 0

    for node in outputs:
        leaves += count_leaves(node.prev)

    return leaves


def build(outputs: List["CircuitNode"]):
    # **** These numbers will be built by first assembling the graph, calling the operation on them, and then figuring out the number of inputs and outputs
    # **** We can figure out the number of inputs required by calculating the number of leaf nodes - in this case every leaf will correspond to a new hadamard
    return QuantumCircuit(1, 2)


if __name__ == "__main__":
    pass
