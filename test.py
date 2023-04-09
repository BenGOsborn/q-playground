from qiskit import QuantumCircuit, Aer, execute


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
