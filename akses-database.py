import sqlite3 as lite

con = lite.connect('database.db')

with con:
    cur = con.cursor()    
    # cur.execute("INSERT INTO Users VALUES(1,'Michelle')")
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    for row in rows:
        print('-----------------')
        print("Judul   :", row[0])
        print("Penulis :", row[1])