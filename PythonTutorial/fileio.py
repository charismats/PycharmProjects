from __future__ import print_function

def main():
    f = open('test.txt')
    line = f.readline()

    while line:
        print(line, end='')
        words = line.split(' ')
        for w in words:
            print (w)
        line = f.readline()

    f.close()

if __name__ == "__main__":
    main()