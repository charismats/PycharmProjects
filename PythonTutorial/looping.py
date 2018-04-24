from __future__ import print_function

def main():

    i = 0
    while i < 5:
        print(i)
        i += 1

    for i in range(0,5):
        for j in range(0,5):
            print("*", end='')
        print()

    for i in range(0,5):
        for j in range(0, i+1):
            print("*", end='')
        print()

    for i in range(0,5):
        for j in range(0, 4 - i):
            print(" ", end='')
        for j in range(0, 2 * i + 1):
            print("*", end='')
        print()

if __name__ == "__main__":
    main()