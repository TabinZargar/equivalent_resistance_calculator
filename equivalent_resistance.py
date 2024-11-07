import numpy as np


def parse_circuit_data(circuit_data):
    # List of nodes and connections
    nodes = circuit_data["nodes"]
    input_node, output_node = circuit_data["input_node"], circuit_data["output_node"]

    # Map each node to a matrix index
    node_index = {node: i for i, node in enumerate(nodes)}
    num_nodes = len(nodes)

    # Initialize conductance matrix and current vector
    G = np.zeros((num_nodes, num_nodes))  # Conductance matrix
    I = np.zeros(num_nodes)  # Current vector

    # Populate the conductance matrix based on connections
    for conn in circuit_data["connections"]:
        start, end, resistance = conn["start"], conn["end"], conn["resistance"]
        i, j = node_index[start], node_index[end]

        # Calculate conductance (1 / resistance)
        conductance = 1 / resistance
        G[i, i] += conductance
        G[j, j] += conductance
        G[i, j] -= conductance
        G[j, i] -= conductance

    # Set boundary conditions: voltage at input node, and reference current
    input_idx = node_index[input_node]
    output_idx = node_index[output_node]

    # Assume 1V at input node to calculate equivalent resistance
    I[input_idx] = 1

    return G, I, input_idx, output_idx


def calculate_equivalent_resistance(G, I, input_idx, output_idx):
    # Solve for node voltages
    # Remove the row and column for the reference (ground) node (output_idx) for a reduced matrix
    G_reduced = np.delete(np.delete(G, output_idx, axis=0), output_idx, axis=1)
    I_reduced = np.delete(I, output_idx)

    # Solve the system of linear equations
    V_reduced = np.linalg.solve(G_reduced, I_reduced)

    # Insert the ground voltage (0V) back into the voltage array at the output index
    V = np.insert(V_reduced, output_idx, 0)

    # Calculate the current flowing into the network from the input node
    I_total = sum(G[input_idx, j] * (V[input_idx] - V[j]) for j in range(len(V)))

    # Equivalent resistance calculation
    R_eq = V[input_idx] / I_total
    return R_eq


# Sample circuit data
circuit_data = {
    "nodes": ["A", "B", "C", "D", "E", "F"],
    "connections": [
        {"start": "A", "end": "C", "resistance": 20},
        {"start": "C", "end": "D", "resistance": 30},
        {"start": "D", "end": "E", "resistance": 40},
        {"start": "D", "end": "F", "resistance": 10},
        {"start": "C", "end": "F", "resistance": 60},
        {"start": "F", "end": "E", "resistance": 50},
        {"start": "E", "end": "B", "resistance": 80},
    ],
    "input_node": "A",
    "output_node": "B"
}

# Construct conductance matrix, current vector, and indices for input/output nodes
G, I, input_idx, output_idx = parse_circuit_data(circuit_data)

# Calculate equivalent resistance
R_eq = calculate_equivalent_resistance(G, I, input_idx, output_idx)
print("Equivalent Resistance between nodes", circuit_data["input_node"], "and", circuit_data["output_node"], "is:",
      R_eq, "ohms")
