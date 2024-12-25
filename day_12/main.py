from file_reader import FileReader
from garden_map_processor import GardenMapProcessor


def main() -> None:
    garden_map = FileReader.read_matrix('data.txt', separator='')

    total_cost_fence_perimeter = 0
    total_cost_fence_sides = 0

    garden_map_processor = GardenMapProcessor(garden_map)
    region_data = garden_map_processor.get_region_data()

    for positions, perimeter, sides in region_data:
        area = len(positions)
        total_cost_fence_perimeter += area * perimeter
        total_cost_fence_sides += area * sides

    print(f'Total cost (Perimeter): {total_cost_fence_perimeter}')
    print(f'Total cost (Sides): {total_cost_fence_sides}')


if __name__ == '__main__':
    main()
