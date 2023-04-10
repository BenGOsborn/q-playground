from qiskit import QuantumCircuit
from collections import defaultdict
from src.circuit_node import CircuitNode, CircuitType, OP_SPAN
from src.q_operators import *


# Check if the circuit is valid
def is_valid_circuit(root: CircuitNode) -> bool:
    if root.c_type != CircuitType.MEASURE:
        return False

    stack = [root]
    seen = {}

    while len(stack):
        node = stack.pop(-1)

        if node in seen:
            continue

        seen[node] = True

        if len(node.children) == 0 and node.c_type != CircuitType.INPUT:
            return False
        elif len(node.children) != 0 and node.c_type == CircuitType.INPUT:
            return False
        elif node != root and node.c_type == CircuitType.MEASURE:
            return False

        for child in node.children:
            stack.append(child)

    return True


# Print the circuit
def print_circuit(root: CircuitNode):
    stack = [(root, 0)]

    while len(stack):
        node, tab_size = stack.pop(-1)

        print(("\t" * tab_size) + str(node))

        for child in node.children:
            stack.append((child, tab_size + 1))


# Build the circuit from a valid circuit and the number of inputs
def build(root: CircuitNode) -> QuantumCircuit:
    # Calculate the circuit size
    stack = [root]
    seen = {}

    total_size = 0
    total_inputs = 0

    while len(stack):
        node = stack.pop(-1)

        if node in seen:
            continue
        seen[node] = True

        total_size += OP_SPAN[node.c_type]
        if node.c_type == CircuitType.INPUT:
            total_inputs += 1

        for child in node.children:
            stack.append(child)

    # Build the circuit - measurements are not considered as a part of the circuits size - we need to artifically add the amount of measurements
    circuit = QuantumCircuit(total_size + total_inputs, total_inputs)

    stack = [root]
    seen = defaultdict(bool)

    counter = 0
    input_index = []

    while len(stack):
        elem = stack.pop(-1)

        if not seen[elem]:
            # Process the children of the current node
            seen[elem] = True
            stack.append(elem)

            for child in elem.children:
                stack.append(child)

        elif elem.out is None:
            # Perform the vector operation
            if elem.c_type == CircuitType.INPUT:
                q_hadamard(circuit, counter)
                elem.out = counter

                input_index.append(counter)

            elif elem.c_type == CircuitType.NOT:
                q_not(
                    circuit,
                    elem.children[0].out,
                    counter
                )
                elem.out = counter

            elif elem.c_type == CircuitType.AND:
                q_and(
                    circuit,
                    elem.children[0].out,
                    elem.children[1].out,
                    counter
                )
                elem.out = counter

            elif elem.c_type == CircuitType.OR:
                q_or(
                    circuit,
                    elem.children[0].out,
                    elem.children[1].out,
                    counter,
                    counter + 1,
                    counter + 2
                )
                elem.out = counter + 2

            elif elem.c_type == CircuitType.MEASURE:
                for j, i in enumerate(input_index):
                    q_and(circuit, i, elem.children[0].out, counter)
                    q_measure(circuit, counter, total_inputs - j - 1)
                    counter += 1

            counter += OP_SPAN[elem.c_type]

    return circuit


if __name__ == "__main__":
    pass
