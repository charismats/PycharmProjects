#!C:\Python27\python

from __future__ import print_function

def main():
    #prompt user input string
    nama = raw_input("Masukkan nama anda : ")
    #prompt user input character
    karakter = raw_input("Masukkan sebuah karakter : ")

    print("Halo ", nama, ", apa kabar?")
    print("Karakter yang dimasukkan : '", karakter,"'")

if __name__ == "__main__":
    main()