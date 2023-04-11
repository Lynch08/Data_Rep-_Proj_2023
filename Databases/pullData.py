import mysql.connector

testDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testDB"
)

cursor = testDb.cursor()
sql =  "select * from player where name = %s"
values = ("Steph",)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)


testDb.close()
cursor.close()