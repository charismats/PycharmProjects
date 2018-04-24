from __future__ import print_function

def main():
    s1 = set([1,2,3])
    s2 = set([3,4])

    #union
    s3 = s1 | s2
    print(s3)

    #difference
    s4 = s1 - s2
    print(s4)

    #intersection
    s5 = s1 & s2
    print(s5)

    s6 = s1 ^ s2
    print(s6)


if __name__ == "__main__":
    main()
