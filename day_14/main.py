from christmas_tree_finder import ChristmasTreeFinder
from image_handler import ImageHandler
from simulation import Simulation


def main() -> None:
    width = 101
    height = 103
    
    simulation = Simulation(width, height)
    simulation.read_robot_data('data.txt')
    
    simulation.simulate_robot_movement(seconds=100)
    quadrants = simulation.calculate_quadrants()
    security_factor = simulation.calculate_security_factor(quadrants)
    print(f'Security factor: {security_factor}')

    simulation = Simulation(width, height)
    simulation.read_robot_data('data.txt')
    
    image_handler = ImageHandler()
    christmas_tree_finder = ChristmasTreeFinder(simulation, image_handler)
    christmas_tree_at_second = christmas_tree_finder.find_christmas_tree(seconds=10000)
    print(f"Christmas tree at second: {christmas_tree_at_second}")


if __name__ == "__main__":
    main()
