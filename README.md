Equivalent Resistance Calculator

A Python Script that calculates the equivalent resistance of any general electrical circuit network represented as a graph. This Script accepts JSON input describing the circuit's nodes, connections, and target nodes for calculating equivalent resistance. The application performs data validation to ensure the input is valid and safe for processing.

Features
- Accepts JSON input for any general circuit network with arbitrary configurations.
- Calculates equivalent resistance between specified input and output nodes.

Getting Started

Prerequisites
- Python 3.10 or higher
- Conda (recommended for environment management)


Input JSON Format
The API accepts JSON input with the following structure:

{
  "nodes": ["A", "B", "C", "D"],
  "connections": [
    {"start": "A", "end": "B", "resistance": 10},
    {"start": "B", "end": "C", "resistance": 5},
    {"start": "C", "end": "D", "resistance": 20},
    {"start": "D", "end": "A", "resistance": 15}
  ],
  "input_node": "A",
  "output_node": "C"
}

- nodes: List of node names (strings) representing the circuit's nodes.
- connections: List of connections, where each connection has:
  - start: The starting node (string).
  - end: The ending node (string).
  - resistance: Resistance value between nodes (positive number).
- input_node and output_node: Nodes between which the equivalent resistance is calculated.


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions, feel free to reach out or open an issue in this repository.

Happy calculating!

