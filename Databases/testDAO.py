from zplayerDAO import playerDAO

#create
latestid = playerDAO.create(('Mark', 35))

#find by id
result = playerDAO.findByID(latestid);
print ("Test create() and findByID()")
print(result)

#update
playerDAO.updateByID(("Enda", 35, latestid))
result = playerDAO.findByID(latestid)
print("test updateByID()")
print (result)

#getAll
print("test GetAll()")
allPlayers = playerDAO.getAll()
for player in allPlayers:
    print (player)

#Delete
playerDAO.deleteByID(latestid)
