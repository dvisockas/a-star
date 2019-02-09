import pdb

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = 0
        self.g = 0
        self.f = 0
        self.parent = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def successors(self):
        children = [
            Node(self.x + 1, self.y),
            Node(self.x, self.y + 1),
            Node(self.x - 1, self.y),
            Node(self.x, self.y - 1)
        ]
        for child in children:
            child.parent = self
        return children
