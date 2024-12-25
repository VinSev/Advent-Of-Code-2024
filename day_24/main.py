from collections import deque
from typing import List, Dict, Set, Tuple, Union

A = 'a'
B = 'b'
C = 'c'
GATE = 'gate'

X = 'x'
Y = 'y'
Z = 'z'

AND = 'AND'
OR = 'OR'
XOR = 'XOR'

def parse_wire_definitions(wire_definitions: List[str]) -> Dict[str, int]:
    wire_values = {}
    
    for line in wire_definitions:
        name, value = line.split(': ')
        wire_values[name] = int(value)
        
    return wire_values

def parse_connection_definitions(connection_definitions: List[str], wire_values: Dict[str, Union[int, None]]) -> List[Dict[str, str]]:
    connections = []
    
    for line in connection_definitions:
        inputs, c = line.split(' -> ')
        a, gate, b = inputs.split(' ')
        
        connections.append({A: a, GATE: gate, B: b, C: c})
        
        wire_values.setdefault(a, None)
        wire_values.setdefault(b, None)
        wire_values.setdefault(c, None)
        
    return connections

def simulate_connections(wire_values: Dict[str, Union[int, None]], connections: List[Dict[str, str]]) -> int:
    queue = deque(connections)

    while queue:
        connection = queue.popleft()
        a = connection[A]
        gate = connection[GATE]
        b = connection[B]
        c = connection[C]
        
        if a in wire_values and b in wire_values:
            if wire_values[a] is not None and wire_values[b] is not None:
                result = evaluate_gate(wire_values[a], wire_values[b], gate)
                wire_values[c] = result
                continue

            queue.append(connection)

    sorted_wire_values = dict(sorted(wire_values.items(), reverse=True))

    binary_number = ''

    for wire, value in sorted_wire_values.items():
        if wire.startswith('z'):
            binary_number += str(value)
            
    decimal_number = int(binary_number, 2)

    return decimal_number

def evaluate_gate(a: int, b: int, gate: str) -> int:
    if gate == AND:
        return and_gate(a, b)
    elif gate == OR:
        return or_gate(a, b)
    elif gate == XOR:
        return xor_gate(a, b)

def and_gate(a: int, b: int) -> int:
    return 1 if a == 1 and b == 1 else 0

def or_gate(a: int, b: int) -> int:
    return 1 if a == 1 or b == 1 else 0

def xor_gate(a: int, b: int) -> int:
    return 1 if a != b else 0

def get_direct_xor_connections(connections: List[Dict[str, str]]) -> Tuple[Set[str], List[Dict[str, str]]]:
    flagged_wires = set()
    
    direct_xor_connections = [
        connection for connection in connections 
        if is_direct_connection(connection) and is_gate_type(XOR)(connection)
    ]
    
    for connection in direct_xor_connections:
        a, b, c = connection[A], connection[B], connection[C]
        is_first_input = a == (X + '00') or b == (X + '00')
        
        if is_first_input:
            if c != (Z + '00'):
                flagged_wires.add(c)
            continue
        elif c == (Z + '00'):
            flagged_wires.add(c)

        if has_z_wire_output(connection):
            flagged_wires.add(c)
    
    return flagged_wires, direct_xor_connections

def get_indirect_xor_connections(connections: List[Dict[str, str]]) -> Tuple[Set[str], List[Dict[str, str]]]:
    flagged_wires = set()
    
    indirect_xor_connections = [
        connection for connection in connections 
        if is_gate_type(XOR)(connection) and not is_direct_connection(connection)
    ]
    
    for connection in indirect_xor_connections:
        if not has_z_wire_output(connection):
            flagged_wires.add(connection[C])
    
    return flagged_wires, indirect_xor_connections

def check_z_connections(connections: List[Dict[str, str]], number_count: int) -> Set[str]:
    flagged_wires = set()
    
    z_connections = [
        connection for connection in connections 
        if has_z_wire_output(connection)
    ]
    
    for connection in z_connections:
        is_last_connection = connection[C] == f'{Z}{number_count}'
        
        if is_last_connection:
            if connection[GATE] != OR:
                flagged_wires.add(connection[C])
            continue
        elif connection[GATE] != XOR:
            flagged_wires.add(connection[C])
    
    return flagged_wires

def check_xor_connections(direct_xor_connections: List[Dict[str, str]], indirect_xor_connections: List[Dict[str, str]], connections: List[Dict[str, str]]) -> Set[str]:
    flagged_wires = set()
    
    connections_to_check = get_checks_to_perform(direct_xor_connections, flagged_wires, indirect_xor_connections)

    for connection in connections_to_check:
        flagged_wires.update(check_connection(connection, indirect_xor_connections, connections))

    return flagged_wires

def get_checks_to_perform(direct_xor_connections: List[Dict[str, str]], flagged_wires: Set[str], indirect_xor_connections: List[Dict[str, str]]) -> List[Dict[str, str]]:
    checks_to_perform = []
    
    for connection in direct_xor_connections:
        c = connection[C]
        
        if c in flagged_wires or c == (Z + '00'):
            continue

        matches = [
            connection for connection in indirect_xor_connections 
            if has_specific_input(c)(connection)
        ]
        
        if not matches:
            checks_to_perform.append(connection)
            flagged_wires.add(c)

    return checks_to_perform

def check_connection(connection: Dict[str, str], indirect_xor_connections: List[Dict[str, str]], connections: List[Dict[str, str]]) -> Set[str]:
    flagged_wires = set()
    
    a = connection[A]
    intended_output = f'{Z}{a[1:]}'
    
    matches = [
        connection for connection in indirect_xor_connections 
        if has_specific_output(intended_output)(connection)
    ]

    match = matches[0]
    inputs_to_check = [match[A], match[B]]
    
    or_connections = [
        connection for connection in connections 
        if is_gate_type(OR)(connection) and connection[C] in inputs_to_check
    ]

    or_connection_output = or_connections[0][C]
    incorrect_wire = next(input for input in inputs_to_check if input != or_connection_output)
    
    flagged_wires.add(incorrect_wire)

    return flagged_wires

def is_direct_connection(connection: Dict[str, str]) -> bool:
    return connection[A].startswith(X) or connection[B].startswith(X)

def is_gate_type(gate: str) -> callable:
    return lambda connection: connection[GATE] == gate

def has_z_wire_output(connection: Dict[str, str]) -> bool:
    return connection[C].startswith(Z)

def has_specific_output(c: str) -> callable:
    return lambda connection: connection[C] == c

def has_specific_input(value: str) -> callable:
    return lambda connection: connection[A] == value or connection[B] == value

def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()
        
    parts = content.split('\n\n')
    wire_definitions, connection_definitions = [part.splitlines() for part in parts]
    
    wire_values = parse_wire_definitions(wire_definitions)
    connections = parse_connection_definitions(connection_definitions, wire_values)
    
    decimal_number = simulate_connections(wire_values, connections)
    print(f'Decimal number: {decimal_number}')
    
    number_count = len(wire_definitions) // 2

    flagged_wires = set()
    flagged_wires.update(get_direct_xor_connections(connections)[0])
    flagged_wires.update(get_indirect_xor_connections(connections)[0])
    flagged_wires.update(check_z_connections(connections, number_count))

    direct_xor_connections, indirect_xor_connections = (
        get_direct_xor_connections(connections)[1], 
        get_indirect_xor_connections(connections)[1]
    )
    flagged_wires.update(check_xor_connections(direct_xor_connections, indirect_xor_connections, connections))

    print(f'Swapped wires: {','.join(sorted(flagged_wires))}')

if __name__ == '__main__':
    main()
