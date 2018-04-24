
import heapq

class City:

    def __init__(self):
        self.id = self.dist = 0
        self.parent = -1

    def __init__(self, id, dist, parent):
        self.id = id
        self.dist = dist
        self.parent = parent

    def __cmp__(self, other):
        if self.dist > other.dist :
            return 1
        if self.dist < other.dist:
            return -1
        return 0

    def __lt__(self, other):
        return self.dist < other.dist

    def __str__(self):
        if self.parent > -1:
            return "City = " + str(chr(self.id + ord('A'))) + " Shortest Distance = "+ str(self.dist) + " parent = " + str(chr(self.parent + ord('A')))
        else:
            return "City = " + str(chr(self.id + ord('A'))) + " Shortest Distance = " + str(self.dist) + " parent = " + 'None'

