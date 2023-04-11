import mysql.connector

testDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testDB"
)

mycursor = testDb.cursor()
sql = "SOME SQL values(%s,%s)"
values = ("Some", "Values")
mycursor.execute(sql, values)

testDb.commit()
testDb.close()
mycursor.close()
