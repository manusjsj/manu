import sqlite3 as sql

def insertUser(cart_items):

    conn = sql.connect('C:/Users/BRANDO/phytonml/sqlite/sample.db')
    cur = conn.cursor()
    query = "INSERT INTO CART VALUES('{}')".format(cart_items)
    cur.execute(query)
    conn.commit()  # this will actually refect the change to db
   
    conn.close()

def retriveUsers():
    conn =sql.connect('C:/Users/BRANDO/phytonml/sqlite/sample.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM CART")
    users = cur.fetchall()
    conn.close()
    return users
