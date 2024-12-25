from typing import List, Tuple

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)
        
    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def move(self, direction: 'Point') -> 'Point':
        return self + direction

ROBOT_SYMBOL = '@'
WALL_SYMBOL = '#'
BOX_SYMBOL = 'O'
EMPTY_SYMBOL = '.'

ROBOT_WIDE = '@.'
WALL_WIDE = '##'
BOX_WIDE = '[]'
EMPTY_WIDE = '..'

EXPAND_CONVERSION_MAP = {
    ROBOT_SYMBOL: ROBOT_WIDE,
    WALL_SYMBOL: WALL_WIDE,
    BOX_SYMBOL: BOX_WIDE,
    EMPTY_SYMBOL: EMPTY_WIDE
}

DIRECTIONS = {
    '^': Point(0, -1),
    '>': Point(1, 0),
    'v': Point(0, 1),
    '<': Point(-1, 0)
}

def find_robot(grid: List[List[str]]) -> 'Point':
    for row_index, row in enumerate(grid):
        for col_index, character in enumerate(row):
            if character == ROBOT_SYMBOL:
                return Point(col_index, row_index)
            
    raise ValueError('Robot not Found')

def expand_grid(grid: List[List[str]]) -> List[List[str]]:
    wide_grid = []
    
    for row in grid:
        wide_row = []
        
        for character in row:
            wide_row.extend(EXPAND_CONVERSION_MAP[character])
            
        wide_grid.append(wide_row)
        
    return wide_grid

def calculate_gps_sum(grid: List[List[str]]) -> int:
    total_gps = 0
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if ''.join(grid[y][x : x + 2]) == BOX_WIDE: 
                total_gps += (100 * y) + x
                
    return total_gps

def move_robot(grid, current_position: 'Point', new_position: 'Point') -> Tuple[List[List[int]], 'Point']:
    grid[current_position.y][current_position.x] = EMPTY_SYMBOL
    grid[new_position.y][new_position.x] = ROBOT_SYMBOL
    
    return grid, new_position

def count_boxes(grid, new_position: 'Point', direction: 'Point') -> Tuple[Point, int]:
    start_x, start_y = new_position.x, new_position.y
    distance = 0

    while grid[start_y][start_x] in BOX_WIDE:
        distance += 1
        start_x += direction.x

    return Point(start_x, start_y), distance

def move_boxes(grid, start_position: 'Point', distance: int, direction: 'Point') -> None:
    current_x, current_y = start_position.x, start_position.y

    for _ in range(distance):
        grid[current_y][current_x] = grid[current_y - direction.y][current_x - direction.x]
        current_x -= direction.x

def push_boxes(grid: List[List[str]], new_position: 'Point', direction: 'Point') -> None:
    start_position, distance = count_boxes(grid, new_position, direction)

    if grid[start_position.y][start_position.x] == WALL_SYMBOL:
        raise ValueError('Can\'t push boxes.')

    move_boxes(grid, start_position, distance, direction)

def handle_box_movement(grid: List[List[str]], robot_position: 'Point', direction: 'Point') -> None:
    boxes_to_push = [{(robot_position.x, robot_position.y)}]
    can_push = True
    all_empty = False

    while can_push and not all_empty:
        next_push = set()
        all_empty = True
        
        for x, y in boxes_to_push[-1]:
            if grid[y][x] == EMPTY_SYMBOL:
                continue
            
            target = Point(x + direction.x, y + direction.y)
            
            if grid[target.y][target.x] == WALL_SYMBOL:
                can_push = False
                break
            
            if grid[target.y][target.x] != EMPTY_SYMBOL:
                all_empty = False

            next_push.add((target.x, target.y))
            check_box(grid, next_push, target.x, target.y)

        boxes_to_push.append(next_push)

    if not can_push:
        raise ValueError('Can\'t push boxes.')

    update_grid_after_push(grid, boxes_to_push, direction)

def check_box(grid: List[List[str]], next_push, x, y) -> None:
    if grid[y][x] == BOX_WIDE[0]:
        next_push.add((x + 1, y))
    elif grid[y][x] == BOX_WIDE[1]:
        next_push.add((x - 1, y))

def update_grid_after_push(grid: List[List[str]], boxes_to_push, direction: 'Point') -> None:
    for index in range(len(boxes_to_push) - 1, 0, -1):
        for box_x, box_y in boxes_to_push[index]:
            from_x, from_y = (box_x - direction.x, box_y - direction.y)
            
            if (from_x, from_y) in boxes_to_push[index - 1]:
                grid[box_y][box_x] = grid[from_y][from_x]
                continue

            grid[box_y][box_x] = EMPTY_SYMBOL

def process_instruction(grid: List[List[str]], robot_position: 'Point', instruction: str) -> Tuple[List[List[str]], 'Point']:
    direction = DIRECTIONS[instruction]

    new_position = robot_position.move(direction)

    if grid[new_position.y][new_position.x] == EMPTY_SYMBOL:
        return move_robot(grid, robot_position, new_position)
    elif grid[new_position.y][new_position.x] == WALL_SYMBOL:
        return grid, robot_position

    if direction.y == 0:
        try:
            push_boxes(grid, new_position, direction)
            return move_robot(grid, robot_position, new_position)
        except ValueError:
            return grid, robot_position

    try:
        handle_box_movement(grid, robot_position, direction)
        return move_robot(grid, robot_position, new_position)
    except ValueError:
        return grid, robot_position

def main():
    with open('data.txt', 'r') as file:
        content = file.read()
    
    grid, instructions = content.split('\n\n')
    grid = [[value for value in line] for line in grid.splitlines()]
    instructions = ''.join(instructions.splitlines())
    
    wide_grid = expand_grid(grid)
    robot_position = find_robot(wide_grid)

    for instruction in instructions:
        wide_grid, robot_position = process_instruction(wide_grid, robot_position, instruction)

    total_gps = calculate_gps_sum(wide_grid)
    print(f'The sum GPS coordinates: {total_gps}')

if __name__ == "__main__":
    main()
