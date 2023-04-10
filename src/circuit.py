from qiskit import QuantumCircuit
from collections import defaultdict
from typing import List
from src.circuit_node import CircuitNode, CircuitType, OP_SPAN


# Check if the circuit is valid
def is_valid_circuit(outputs: List["CircuitNode"]) -> bool:
    # Must contain a node
    if len(outputs) == 0:
        return False

    # All nodes in last layer should be measurement type
    valid_measures = {}

    for output in outputs:
        if output.c_type != CircuitType.MEASURE:
            return False
        valid_measures[output] = True

    # All leaf nodes should be inputs
    stack = outputs.copy()
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
        elif node not in valid_measures and node.c_type == CircuitType.MEASURE:
            return False

        for child in node.children:
            stack.append(child)

    return True


# Print the circuit
def print_circuit(outputs: List["CircuitNode"]):
    stack = [(x, 0) for x in outputs]

    while len(stack):
        node, tab_size = stack.pop(-1)

        print(("\t" * tab_size) + str(node))

        for child in node.children:
            stack.append((child, tab_size + 1))


# Build the circuit from a valid circuit and the number of inputs


def build(outputs: List["CircuitNode"]) -> QuantumCircuit:
    # **** These numbers will be built by first assembling the graph, calling the operation on them, and then figuring out the number of inputs and outputs
    # **** We can figure out the number of inputs required by calculating the number of leaf nodes - in this case every leaf will correspond to a new hadamard
    # **** So the count inputs actually comes from the entire circuit - we just apply hadamards to the specific input values (which we see when we see)

    # **** So the first thing we will do is loop through each of the outputs, then check where the output ends up at based on the current offset and the op size

    stack = outputs.copy()
    seen = {}

    total_size = 0

    while len(stack):
        node = stack.pop(-1)

        if node in seen:
            continue
        seen[node] = True

        total_size += OP_SPAN[node.c_type]

        for child in node.children:
            stack.append(child)

    # **** It is important to note that we cannot just write the outputs here randomly - we need to process the other nodes sequentially from the bottom up, then make our way to the end.
    # Then at the end, we will write the measure output

    # **** We also need to make sure there is some way of interpolating the result that comes out of the computation
    # **** This is going to be difficult to evaluate given this system - we might need state tuples

    circuit = QuantumCircuit(total_size, len(outputs))
    print(circuit)

    stack = outputs.clone()
    seen = defaultdict(int)
    counter = 0

    # **** Instead of having seen map to true, we will figure out where it needs to go

    while len(stack):
        elem = stack.pop()

        if elem.out is None:
            for child in elem.children:
                pass

            # **** Now we need to get the value for the previous elem and evaluate it ???
            # elem.out =

            # Process the children of the current node
            pass
        else:
            # Process the current node
            pass

        # **** Now for this we look at the operation and perform the value on it (but only after it has been completed - thus, we need to check what state we are in)

    return circuit


if __name__ == "__main__":
    pass
