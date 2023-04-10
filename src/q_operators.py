from qiskit import QuantumCircuit

# The more circuits we define here instead of using abstraction results in more efficient circuits


def q_or(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.x(in_bit1)
    circuit.x(in_bit2)
    circuit.ccx(in_bit1, in_bit2, out_bit)
    circuit.x(out_bit)


def q_and(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.ccx(in_bit1, in_bit2, out_bit)


def q_not(circuit: QuantumCircuit, in_bit: int):
    circuit.x(in_bit)
