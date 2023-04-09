from qiskit import QuantumCircuit, Aer, execute
from enum import Enum
from typing import List

# **** I need a comparison circuit
# **** I also need an equals circuit

# **** So we will have it such that each node will correspond to ONE operation

# **** It needs to list the nodes that were used to build it, and then we can calculate its operations using those bits from inputs
# **** We will have it such that each output from a previous node corresponds to an input as another node
# **** At the end, we can build the circuit by looking at each node and figuring out where it goes to
# **** This means for each observation, we must record that observation within our circuit builder and use it as our back propogation

# **** We currently need a way of running input nodes - this can probably just be done using hadamards - but how do we model these hadamards ?
# **** All of the last outputs will be recorded as a measurement node
# **** We will build the graph from the bottom up using a postfix search


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
