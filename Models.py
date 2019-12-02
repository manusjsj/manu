import sqlite3 as sql

def insertUser(username, password):

    conn = sql.connect('C:/Users/BRANDO/phytonml/sqlite/sample.db')
    cur = conn.cursor()
    query = "INSERT INTO LOGIN VALUES('{}','{}')".format(username,password)
    cur.execute(query)
    conn.commit()  # this will actually refect the change to db
    print("you have been registerd sucessfully")

    conn.close()

def retriveUsers():
    conn =sql.connect('C:/Users/BRANDO/phytonml/sqlite/sample.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM LOGIN")
    users = cur.fetchall()
    conn.close()
    return users
