import mysql.connector
class PlayerDAO:
    host = ""
    user = ""
    password = ""
    database = ""

    connection = ""
    cursor = ""

    def __init__(self):
        # these should be read in from a config file
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "testDB"


    def getCursor(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql =  'INSERT INTO player (name, age) values (%s, %s)'
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    def getAll(self):
        cursor = self.getCursor()
        sql =  "select * from player"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result
    
    def findByID(self,id):
        cursor = self.getCursor()
        sql = "select * from player where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result
    
    def updateByID(self, values):
        cursor = self.getCursor()
        sql = "UPDATE player SET name = %s,  age = %s WHERE id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def deleteByID(self, id):
        cursor = self.getCursor()
        sql = "DELETE FROM player where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

playerDAO = PlayerDAO()



