import mysql.connector

testDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testDB"
)

cursor = testDb.cursor()
sql =  "DELETE FROM player where id = %s"
values = (1,)

cursor.execute(sql, values)
testDb.commit()
print("Deletion Complete")


testDb.close()
cursor.close()