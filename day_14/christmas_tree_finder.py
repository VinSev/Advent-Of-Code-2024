from image_handler import ImageHandler
from simulation import Simulation


class ChristmasTreeFinder():
    def __init__(self, simulation: Simulation, image_handler: ImageHandler) -> None:
        self.simulation = simulation
        self.image_handler = image_handler

    def find_christmas_tree(self, seconds: int) -> str:        
        for second in range(1, seconds + 1):
            self.simulation.simulate_robot_movement(seconds=1)
            
            if self.is_potential_christmas_tree(second):
                self.image_handler.create_image(self.simulation.spaces, self.simulation.width, self.simulation.height, second)

        return self.image_handler.get_name_smallest_image()
    
    def is_potential_christmas_tree(self, second: int) -> bool:
        return (second % 101) - 39 == 0
