rows = 5
cols = 5

grid = [["." for _ in range(cols)] for _ in range(rows)]

for row in grid:
    print(" ".join(row))
