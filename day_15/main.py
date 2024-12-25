ROBOT = '@'
WALL = '#'
BOX = 'O'
EMPTY = '.'

DIRECTIONS = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}

def find_robot(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == ROBOT:
                return (x, y)

def process_instruction(grid, direction):
    robot_x, robot_y = find_robot(grid)
    dx, dy = DIRECTIONS[direction]
    new_x, new_y = robot_x + dx, robot_y + dy

    if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]):
        return

    if grid[new_y][new_x] == WALL:
        return

    if grid[new_y][new_x] == BOX:
        box_new_x = new_x
        box_new_y = new_y
        
        while True:
            box_new_x += dx
            box_new_y += dy
            
            if box_new_y < 0 or box_new_y >= len(grid) or box_new_x < 0 or box_new_x >= len(grid[0]):
                return 
            if grid[box_new_y][box_new_x] == EMPTY:
                grid[box_new_y][box_new_x] = BOX
                grid[new_y][new_x] = EMPTY
                break
            elif grid[box_new_y][box_new_x] == WALL:
                return
            elif grid[box_new_y][box_new_x] == BOX:
                continue
            else:
                return

    grid[robot_y][robot_x] = EMPTY
    grid[new_y][new_x] = ROBOT
    
def calculate_gps_sum(grid):
    total_gps = 0
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == BOX: 
                total_gps += (100 * y) + x
                
    return total_gps

def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()
        
    grid, instructions = content.split('\n\n')
    grid = [[value for value in line] for line in grid.splitlines()]
    instructions = ''.join(instructions.splitlines())

    for instruction in instructions:
        process_instruction(grid, instruction)

    total_gps = calculate_gps_sum(grid)
    print(f'The sum GPS coordinates: {total_gps}')

if __name__ == '__main__':
    main()