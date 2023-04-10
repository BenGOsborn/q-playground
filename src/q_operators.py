from qiskit import QuantumCircuit

# The more circuits we define here instead of using abstraction results in more efficient circuits
# Note that all operations need to be read only for the state - to write to a variable, it must first be copied then mutated using the c not gate

# TODO make an abstraction for this that is independent of 'QuantumCircuit' for other implementations


def q_or(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_in_bit1: int, out_in_bit2: int, out_bit: int):
    circuit.cx(in_bit1, out_in_bit1)
    circuit.cx(in_bit2, out_in_bit2)

    circuit.x(out_in_bit1)
    circuit.x(out_in_bit2)
    circuit.ccx(out_in_bit1, out_in_bit2, out_bit)
    circuit.x(out_bit)


def q_and(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.ccx(in_bit1, in_bit2, out_bit)


def q_not(circuit: QuantumCircuit, in_bit: int, out_bit: int):
    circuit.cx(in_bit, out_bit)
    circuit.x(out_bit)


def q_hadamard(circuit: QuantumCircuit, out_bit: int):
    circuit.h(out_bit)


def q_measure(circuit: QuantumCircuit, out_bit: int, c_bit: int):
    circuit.measure(out_bit, c_bit)
