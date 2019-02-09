from solver import Solver
import sys
import copy

grid = [
    [0,0,0,0,0],
    [1,1,1,1,0],
    [0,0,0,0,0],
    [0,1,1,1,1],
    [0,0,0,0,9],
]

def draw(x, y):
    # Clears stdout
    print(chr(27) + "[2J")
    step = copy.deepcopy(grid)
    step[x][y] = 'x'
    for row in step:
        for column in row:
            sys.stdout.write(str(column))
        sys.stdout.write('\n')
    sys.stdout.flush()

solver = Solver(grid)
path = solver.solve()

while path:
    draw(path.x, path.y)
    path = path.parent
    input('')

