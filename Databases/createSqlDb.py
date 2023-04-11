import mysql.connector

testDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    #database = "testDB"
)

cursor = testDb.cursor()
cursor.execute("create DATABASE TestDb")

testDb.close()
cursor.close()