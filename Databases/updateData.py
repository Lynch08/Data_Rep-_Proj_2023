import mysql.connector

testDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testDB"
)

cursor = testDb.cursor()
sql =  "UPDATE player SET name = %s,  age = %s WHERE id = %s"
values = ("Enda", 35, 1)

cursor.execute(sql, values)
testDb.commit()
print("Update Complete")


testDb.close()
cursor.close()