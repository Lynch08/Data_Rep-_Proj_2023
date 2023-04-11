import mysql.connector

testDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testDB"
)

cursor = testDb.cursor()
sql =  'INSERT INTO player (name, age) values (%s, %s)'
values = ("Lebron", 35)

cursor.execute(sql, values)
testDb.commit()
print("1 Record insertd, ID:", cursor.lastrowid)

testDb.close()
cursor.close()