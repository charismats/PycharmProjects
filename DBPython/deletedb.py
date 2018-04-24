from __future__ import print_function


import mysql.connector


def main():
    conn = mysql.connector.connect(host='localhost', database='universitas', user='root', password='')

    cur = conn.cursor()

    sql = "DELETE FROM mahasiswa WHERE id = 3"

    try:
        cur.execute(sql)

        print('Record deleted successfully')

    except mysql.connector.Error as e:
        print('Error ', e)
    else:
        conn.commit()

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()