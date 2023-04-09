from qiskit import QuantumCircuit


def build(self, outputs: list):
    # **** These numbers will be built by first assembling the graph, calling the operation on them, and then figuring out the number of inputs and outputs
    # **** We can figure out the number of inputs required by calculating the number of leaf nodes - in this case every leaf will correspond to a new hadamard
    return QuantumCircuit(1, 2)
