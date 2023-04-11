import mysql.connector

testDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testDB"
)

mycursor = testDb.cursor()
sql = "SOME SQL"
mycursor.execute(sql)

testDb.close()
mycursor.close()
