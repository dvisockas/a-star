from node import Node

class Solver(object):
    def __init__(self, grid):
        self.grid = grid
        self.objective = None
        self.found = False
        self.open = []
        self.closed = []
        self.goal = None

    def solve(self):
        self.find_objective()
        if not self.objective:
            return print('No objective found')
        print('Solving...')
        self.starting_node = Node(0, 0)
        self.open.append(self.starting_node)
        while len(self.open) and not self.goal:
            self.explore()
        return self.goal

    def explore(self):
        nodes_by_f = list(map(lambda x: x.f, self.open))
        min_f = min(nodes_by_f)
        selected_idx = nodes_by_f.index(min_f)
        selected = self.open.pop(selected_idx)
        self.closed.append(selected)
        self.process_successors(selected)

    def process_successors(self, parent):
        children = parent.successors()
        for child in children:
            if self.in_grid(child) and self.can_walk(child):
                self.calculate_for(child)
                if not child in self.closed:
                    self.open.append(child)
                if self.is_goal(child):
                    self.goal = child
    def is_goal(self, node):
        return self.grid[node.x][node.y] == 9

    def can_walk(self, node):
        return not self.grid[node.x][node.y] == 1

    def calculate_for(self, node):
        node.g = node.parent.g + 1
        goal = self.objective
        node.h = abs(node.x - goal.x) + abs(node.y - goal.y)
        node.f = node.g + node.h

    def in_grid(self, node):
        if node.x < 0 or node.y < 0:
            return False
        if node.x > self.max_x or node.y > self.max_y:
            return False
        return True

    def find_objective(self):
        for x, row in enumerate(self.grid):
            for y, column in enumerate(row):
                if column == 9:
                    print(f'Found objective at {x}, {y}')
                    self.objective = Node(x, y)
                self.max_x = x
                self.max_y = y