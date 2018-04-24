class Edge:
    def __init__(self):
        self.v1 = 0
        self.v2 = 0
        self.weight = 0

    def __cmp__(self, other):
        if self.weight < other.weight:
            return -1
        if self.weight > other.weight:
            return 1
        return 0

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return str(self.v1) + " -> " + str(self.v2) + " = "+ str(self.weight)