from qiskit import QuantumCircuit


def or_circuit(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.x(in_bit1)
    circuit.x(in_bit2)
    circuit.ccx(in_bit1, in_bit2, out_bit)
    circuit.x(out_bit)


def and_circuit(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.ccx(in_bit1, in_bit2, out_bit)


# TODO
def adder_circuit(circuit: QuantumCircuit):
    # https://www.youtube.com/results?search_query=make+an+adder+circuit
    pass
