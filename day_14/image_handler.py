import os
import random
from PIL import Image
from typing import List

IMAGE_DIRECTORY = 'potential_christmas_trees'

class ImageHandler():
    def create_image(self, spaces: List[List[int]], width: int, height: int, second: int) -> None:
        image = Image.new('RGB', (width, height), (255, 255, 255))
        pixels = image.load()

        for y in range(height):
            for x in range(width):
                if spaces[y][x] > 0:
                    color_chance = random.random()
                    if color_chance < 0.8:
                        pixels[x, y] = (7,86,0)
                    elif color_chance < 0.9:
                        pixels[x, y] = (240,219,77)
                    else:
                        pixels[x, y] = (170,0,0)
                else:
                    pixels[x, y] = (255, 255, 255)

        image.save(f'{IMAGE_DIRECTORY}/{second}.png')

    def get_name_smallest_image(self) -> str:
        files = [
            file for file in os.listdir(IMAGE_DIRECTORY) 
            if os.path.isfile(os.path.join(IMAGE_DIRECTORY, file))
        ]
        
        smallest_file = min(files, key=lambda file: os.path.getsize(os.path.join(IMAGE_DIRECTORY, file)))
        
        return smallest_file[:-4]
