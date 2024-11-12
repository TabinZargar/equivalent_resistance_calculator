def convert_to_spice_netlist(circuit_data):
    """
    Convert custom circuit data (JSON format) to a SPICE netlist.

    Parameters:
        circuit_data (dict): The input circuit data with nodes and connections.
            - "nodes": A list of nodes in the circuit.
            - "connections": A list of connections, each containing "start", "end",
              and "resistance" values.

    Returns:
        str: A SPICE netlist string that represents the circuit.

    Example:
        {
            "nodes": ["A", "B", "C", "D"],
            "connections": [
                {"start": "A", "end": "B", "resistance": 100},
                {"start": "B", "end": "C", "resistance": 50},
                {"start": "C", "end": "D", "resistance": 200},
                {"start": "D", "end": "A", "resistance": 150}
            ]
        }
    """
    # Extract nodes and connections from the input data
    connections = circuit_data.get("connections", [])

    # Initialize the netlist string
    netlist = "* SPICE Netlist for the given circuit\n"

    # Iterate over the connections and generate corresponding SPICE resistor definitions
    for i, conn in enumerate(connections, 1):
        start, end, resistance = conn['start'], conn['end'], conn['resistance']
        netlist += f"R{i} {start} {end} {resistance}\n"

    return netlist

