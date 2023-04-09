from qiskit import QuantumCircuit, Aer, execute

# **** I need a comparison circuit
# **** I also need an equals circuit


def adder_circuit(circuit: QuantumCircuit):
    # https://www.youtube.com/results?search_query=make+an+adder+circuit
    pass


def or_circuit(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.x(in_bit1)
    circuit.x(in_bit2)
    circuit.ccx(in_bit1, in_bit2, out_bit)
    circuit.x(out_bit)


def and_circuit(circuit: QuantumCircuit, in_bit1: int, in_bit2: int, out_bit: int):
    circuit.ccx(in_bit1, in_bit2, out_bit)


def build_circuit():
    circuit = QuantumCircuit(7, 2)

    # Superposition input states
    circuit.h(0)
    circuit.h(1)

    # Move state down
    circuit.cx(0, 2)
    circuit.cx(1, 3)

    # Apply logic gate to get satisfy output
    circuit.x(3)
    circuit.ccx(2, 3, 4)

    # Check initial states used for output satisfied
    circuit.ccx(0, 4, 5)
    circuit.ccx(1, 4, 6)

    # Measure
    circuit.measure(5, 1)
    circuit.measure(6, 0)

    return circuit


def main():
    circuit = build_circuit()
    print(circuit)

    sim = Aer.get_backend("qasm_simulator")

    result = execute(circuit, sim).result()

    counts = result.get_counts()
    print(counts)


if __name__ == "__main__":
    main()
