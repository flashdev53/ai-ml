def read_grid(grid_lines):
    grid = [list(line.strip()) for line in grid_lines if line.strip()]
    return grid

def find_start_and_tasks(grid):
    start = None
    tasks = []

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 'S':
                start = (row_idx, col_idx)
            elif cell == 'T':
                tasks.append((row_idx, col_idx))

    return start, tasks
ascii_grid = [
    "#####",
    "#S..#",
    "#.T.#",
    "#..T#",
    "#####"
]

grid = read_grid(ascii_grid)
start, tasks = find_start_and_tasks(grid)

print("Start position:", start)
print("Task cells:", tasks)
