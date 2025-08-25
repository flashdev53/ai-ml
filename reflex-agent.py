import random
import time
import os
grid = [
    ["_", "*", "#"],
    ["#", "_", "_"],
    ["#", "*", "_"]
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
def print_board():
    os.system('cls')
    board_copy = [row[:] for row in grid]
    agent_x, agent_y = agent_pos
    board_copy[agent_x][agent_y] = "A"
    
    for row in board_copy:
        print(" ".join(row))
    print()
def reflex_agent(pos):
    x, y = pos
    if grid[x][y] == "*":
        print(f"Collected item at ({x}, {y})")
        grid[x][y] = "_"
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
def check_items_collected():
    for row in grid:
        if "*" in row:
            return False
    return True
step=0
while True:
    os.system('cls')
    print(f"\nStep {step + 1}")
    print_board()
    agent_pos = reflex_agent(agent_pos)
    if check_items_collected():
        print("All items collected. Stopping.")
        break
    time.sleep(1)
