
from City import City
import heapq


graph = [
    [0, 1, 3, -1, -1],
    [1, 0, 1,  2,  3],
    [3, 1, 0, -1,  4],
    [-1, 2, -1,  0,  2],
    [-1, 3, 4,  2, 0]
]


class Dijkstra(object):

    def __init__(self):
        self.pq = [ ]
        self.cities = []

    def run_algorithm(self):
        self.start = 0
        for i in range(0, len(graph)):
            c = City(i, 1000, -1)
            self.cities.append(c)

        self.cities[self.start].dist = 0


        heapq.heappush(self.pq, self.cities[self.start])

        while len(self.pq) > 0:
            current = heapq.heappop(self.pq)
            id_curr = current.id

            for j in range(0, len(graph[id_curr])):
                if j != id_curr and graph[id_curr][j] >= 0:
                    if current.dist + graph[id_curr][j] < self.cities[j].dist:
                        self.cities[j].dist = current.dist + graph[id_curr][j]
                        self.cities[j].parent = id_curr
                        heapq.heappush(self.pq, self.cities[j] )


        print("Shortdest Path found")
        self.print_shortest_path()

    def print_shortest_path(self):
        for city in self.cities:
            print(city),
            self.print_path(self.start, city.id)

    def print_path(self, frm , to):

        c = self.cities[to]
        parent = None
        path = ""
        while c.id != frm :
            path = "-" + chr(c.id + ord('A')) + path
            c = self.cities[c.parent]
        path = chr(frm + ord('A')) + path;

        print(path)

dijkstra = Dijkstra()
dijkstra.run_algorithm()
