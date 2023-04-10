from src.circuit import *
from src.circuit_node import CircuitNode
from qiskit import QuantumCircuit, Aer, execute

if __name__ == "__main__":
    # Build the circuit
    circuit = CircuitNode().and_(CircuitNode()).or_(CircuitNode()).measure_()

    is_valid = is_valid_circuit(circuit)
    assert is_valid, "Invalid circuit"

    print_circuit(circuit)
    q_circuit = build(circuit)

    print(q_circuit)

    # Run the circuit
    sim = Aer.get_backend("qasm_simulator")

    result = execute(q_circuit, sim).result()

    counts = result.get_counts()
    print(counts)
