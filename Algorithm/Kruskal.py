from Edge import Edge
from Set import Set

graph = [
    [0, 7, 0, 5, 0, 0, 0],
    [7, 0, 8, 9, 7, 0, 0],
    [0, 8, 0, 0, 5, 0, 0],
    [5, 9, 0, 0, 15, 6, 0],
    [0, 7, 5, 15, 0, 8, 9],
    [0, 0, 0, 6, 8, 0, 11],
    [0, 0, 0, 0, 9, 11, 0]
]


class Kruskal:

    def __init__(self):
        self.listedges = []
        self.listset = []
        self.MST = Set()
        self.MSTEdges = []

    def runalgorithm(self):
        for i in range(0, len(graph)):
            s = Set()
            s.vertices.append(i)
            self.listset.append(s)

        for i in range(0, len(graph)):
            for j in range( i, len(graph)):
                if i != j and graph[i][j] > 0:
                    e = Edge()
                    e.v1 = i
                    e.v2 = j
                    e.weight = graph[i][j]
                    self.listedges.append(e)

        self.listedges.sort()
        while len(self.listedges) > 0 and not self.not_found_mst():
            removed_edge = self.listedges[0]
            self.listedges.remove(removed_edge)
            v1 = removed_edge.v1
            v2 = removed_edge.v2
            s1 = self.find_set(v1)
            s2 = self.find_set(v2)

            if not self.is_same_set(s1, s2):
                self.union(s1,s2)
                self.MSTEdges.append(removed_edge)

        print("MST Found")

        self.print_mst_result()

    def union(self, s1, s2):
        for i in s1.vertices:
            if i not in s2.vertices:
                s2.vertices.append(i)
            if i not in self.MST.vertices:
                self.MST.vertices.append(i)

        for i in s2.vertices:
            if i not in s1.vertices:
                s1.vertices.append(i)
            if i not in self.MST.vertices:
                self.MST.vertices.append(i)

    def is_same_set(self, s1, s2):
        for i in s1.vertices:
            if i not in s2.vertices:
                return False
        return True

    def find_set(self, vertice):
        for i in range(0, len(self.listset)):
            set = self.listset[i]
            if vertice in set.vertices:
                return set

        return None

    def not_found_mst(self):
        for i in range(0, len(graph)):
            if i not in self.MST.vertices:
                return False

        return True

    def print_mst_result(self):
        print("MST vertices : ")
        for i in self.MST.vertices:
            print(chr(i + ord('A')))

        for e in self.MSTEdges:
            print(e)


kruskal = Kruskal()
kruskal.runalgorithm()