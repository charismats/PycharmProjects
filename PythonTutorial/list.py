from __future__ import print_function


def main():
    li = [100,200,300,400]

    for i in li:
        print(i)
    print(li[-1])
    print(li[-2])
    print(li[-3])
    print(li[-4])
    print(li.index(100))

if __name__ == "__main__":
    main()