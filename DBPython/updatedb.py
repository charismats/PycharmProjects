from __future__ import print_function

import mysql.connector


def main():
    conn = mysql.connector.connect(host='localhost', database='universitas', user='root', password='')

    cur = conn.cursor()

    data1 = ('charisma tubagus', 2, '33xx01', 3.7, 1)

    sql = "UPDATE mahasiswa SET nama=%s, semester=%s, NIM=%s, ipk=%s WHERE id=%s"
    try:
        cur.execute(sql, data1)

        print('Records updated successfully')

    except mysql.connector.Error as e:
        print('Error ', e)
    else:
        conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()