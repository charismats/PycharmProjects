from __future__ import print_function

import mysql.connector


def main():
    conn = mysql.connector.connect(host='localhost', database='universitas', user='root', password='')

    cur = conn.cursor()

    data1 = ('charisma tubagus setyobudhi', 3, '333xxx01', 3.4)
    data2 = ('john dahl tommasson', 2, '33xx021', 3.3)
    data3 = ('paladin knight', 1, '33333', 3.1)

    sql = "INSERT INTO mahasiswa(nama, semester, nim, ipk) VALUES (%s, %s, %s, %s)"

    try:
        cur.execute(sql, data1)
        #cur.execute(sql, data2)
        #cur.execute(sql, data3)

        print('Rows inserted successfully')
    except mysql.connector.DataError as e:
        conn.rollback()
        print('Error' , e)
    else:
        conn.commit()
        cur.close()


if __name__ == "__main__":
    main()

