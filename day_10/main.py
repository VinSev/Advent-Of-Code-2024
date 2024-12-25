from file_reader import FileReader
from path_finder import Pathfinder
from point import Point
from topographic_map import TopographicMap

STARTING_POINT = 0


def main() -> None:
    topographic_data = FileReader.read_matrix('data.txt', target_type=int, separator='')
    topographic_map = TopographicMap(topographic_data)
    pathfinder = Pathfinder(topographic_map)
    
    total_score = 0
    total_rating = 0

    for y, rows in enumerate(topographic_map.map):
        for x, cell in enumerate(rows):
            if cell == STARTING_POINT:
                score, rating = pathfinder.find_paths(Point(x, y))
                total_score += score
                total_rating += rating

    print(total_score, total_rating)

if __name__ == '__main__':
    main()
