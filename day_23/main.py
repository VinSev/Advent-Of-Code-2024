from computer_network import ComputerNetwork


def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()
        
    connections = [line.split('-') for line in content.splitlines()]
    
    network = ComputerNetwork(connections)
    triangles = network.find_triangles()
    
    triangle_count = network.count_triangles_with_t(triangles)
    print(f'Amount of triangular connections starting with \'t\': {triangle_count}')

    largest_lan_party = network.get_largest_lan_party()
    print(f'Largest LAN party: {','.join(largest_lan_party)}')


if __name__ == '__main__':
    main()
