from flask import Flask,url_for, request, redirect, abort, jsonify


app = Flask(__name__, static_url_path='', static_folder='static_pages_for_api')

NflPlayers =[ 
    {"Id":1, "Name":"Tom Brady", "Position": "QB", "Team":"New England Patriots", "Player_Rank": 1},
    {"Id":2, "Name":"Joe Burrow", "Position": "QB", "Team":"Cincinatti Bengals", "Player_Rank": 10},
    {"Id":3, "Name":"Julian Edelman", "Position": "WR", "Team":"New England Patriots", "Player_Rank": 100}
]

nextID = 4

#index
@app.route('/')
def index():
    return "Hello World especially Enda"

#get all
@app.route('/allPlayers', methods=['GET'])
def getAll():
    return jsonify(NflPlayers)

#Find by ID
@app.route('/allPlayers/<int:Id>')
def findById(Id):
    playerByID = list(filter(lambda t : t["Id"]==Id, NflPlayers))
    if len(playerByID) == 0:
        return "Not A Valid ID"
        #return jsonify({}), 204
    return jsonify(playerByID[0])
    #return playerByID
    #return "served by findById() with ID: " +str(Id)

#Create
#curl -X POST -H "content-type:application/json" -d "{\"Name\":\"Test\", \"Player_Rank\":123, \"Position\":\"WR\", \"Team\":\"Test Team\"}" http://127.0.0.1:5000/allPlayers
@app.route('/allPlayers',methods=['POST'] )
def create():
    global nextID
    if not  request.json:
        abort(400)

    player = {
        "Id" : nextID,
        "Name": request.json["Name"],
        "Position": request.json ["Position"],
        "Team": request.json["Team"],
        "Player_Rank": request.json["Player_Rank"]
    }

    NflPlayers.append(player)
    nextID += 1
    return jsonify(player)
    #return "Served by Create()"


#Update
# curl -X PUT -d "{\"Name\":\"New_Player\", \"Player_Rank\":199, \"Position\":\"DL\", \"Team\":\"Test_Team\"}" -H "content-type:application/json"  http://127.0.0.1:5000/allPlayers/2

@app.route('/allPlayers/<int:id>', methods=['PUT'])
def update(id):
    playerByID = list(filter(lambda t : t["Id"]==id, NflPlayers))
    if len(playerByID) == 0:
        return "Cannot Find Player"
    currentPlayer = playerByID[0]
    if 'Name' in request.json:
        currentPlayer ['Name'] = request.json['Name']
    if 'Position' in request.json:
        currentPlayer ['Position'] = request.json['Position']
    if 'Team' in request.json:
        currentPlayer ['Team'] = request.json['Team']
    if 'Player_Rank' in request.json:
        currentPlayer ['Player_Rank'] = request.json['Player_Rank']

    return jsonify(currentPlayer)

#Delete
@app.route('/allPlayers/<int:id>', methods=['DELETE'])
def delete(id):
    playerByID = list(filter(lambda t : t["Id"]==id, NflPlayers))
    if len(playerByID) == 0:
        return "Cannot Find Player To Delete"
    NflPlayers.remove(playerByID[0])
    return jsonify({"done":True})




if __name__ == "__main__":
    app.run(debug = True)