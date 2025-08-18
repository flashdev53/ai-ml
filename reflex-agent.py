import random
grid = [
    [" ", "*", "#"],
    ["#", " ", " "],
    ["*", "#", " "]
]
agent_pos = [0, 0]
moves = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}
def is_valid(pos):
    x, y = pos
    return 0 <= x < 3 and 0 <= y < 3 and grid[x][y] != "#"
def reflex_agent(pos):
    x, y = pos
    if grid[x][y] == "*":
        print(f"Collected item at ({x}, {y})")
        grid[x][y] = " "
    valid_moves = []
    for direction, (dx, dy) in moves.items():
        new_x, new_y = x + dx, y + dy
        if is_valid((new_x, new_y)):
            valid_moves.append((direction, (new_x, new_y)))
    if valid_moves:
        chosen = random.choice(valid_moves)
        print(f"Moving {chosen[0]} to {chosen[1]}")
        return chosen[1]
    else:
        print("No valid moves. Stops")
        return pos
for step in range(6):
    print(f"\nStep {step + 1}")
    agent_pos = reflex_agent(agent_pos)
