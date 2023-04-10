from qiskit import QuantumCircuit

# The more circuits we define here instead of using abstraction results in more efficient circuits
# TODO make an abstraction for this that is independent of 'QuantumCircuit' for other implementations


def q_or(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.x(in_bit1)
    circuit.x(in_bit2)
    circuit.ccx(in_bit1, in_bit2, out_bit)
    circuit.x(out_bit)


def q_and(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.ccx(in_bit1, in_bit2, out_bit)


def q_not(circuit: QuantumCircuit, out_bit: int):
    circuit.x(out_bit)


def q_c_not(circuit: QuantumCircuit, in_bit: int, out_bit: int):
    circuit.cx(in_bit, out_bit)


def q_hadamard(circuit: QuantumCircuit, out_bit: int):
    circuit.h(out_bit)


def q_measure(circuit: QuantumCircuit, out_bit: int, c_bit: int):
    circuit.measure(out_bit, c_bit)
