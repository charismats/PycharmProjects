from __future__ import print_function

import mysql.connector


def main():
    conn = mysql.connector.connect(host='localhost', database='universitas', user='root', password='')

    cur = conn.cursor()

    sql = "SELECT * FROM mahasiswa"

    try:
        cur.execute(sql)

        result = cur.fetchall()

        for row in result:
            print(row[0], ' ', row[1], ' ', row[2], ' ', row[3], ' ', row[4])

    except mysql.connector.DataError as e:
        print("Error ", e)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()