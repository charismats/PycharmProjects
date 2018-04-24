from __future__ import print_function

count = 0

def main():
    global count
    count += 1
    s = 'hello'
    a = 3
    if a == 3:
        s = 'world'
        print(s)
    print(count)

if __name__ == "__main__":
    main()