from __future__ import print_function
import operator

def main():
    d = {'satu':10, 'dua':20, 'tiga':30}

    print("d['satu']", d['satu'])

    d['empat'] = 40
    d['lima'] = 50

    print("Sorted based on keys")
    for k, v in sorted(d.items()):
        print(k, ' ', v)

    print("Sorted based on values")
    for k, v in sorted(d.items(), key=operator.itemgetter(1), reverse=True):
        print(k, ' ', v )


if __name__ == '__main__':
    main()