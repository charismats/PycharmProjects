from Edge import Edge
import operator

def main():
    e1 = Edge()
    e1.v1 = 0
    e1.v2 = 1
    e1.weight = 4

    e2 = Edge()
    e2.v1 = 1
    e2.v2 = 2
    e2.weight = 2

    listedge = []
    listedge.append(e1)
    listedge.append(e2)
    listedge.sort()
   # sorted(listedge, key=operator.attrgetter('weight'))
    for e in listedge:
        print(e)


if __name__ == "__main__":
    main()