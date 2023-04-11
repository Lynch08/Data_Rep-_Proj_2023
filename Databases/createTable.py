import mysql.connector

testDb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testDB"
)

cursor = testDb.cursor()
sql =  "CREATE TABLE player(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), age INT)" 

cursor.execute(sql)

testDb.close()
cursor.close()