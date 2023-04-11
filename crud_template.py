from flask import Flask,url_for, request, redirect, abort, jsonify


app = Flask(__name__, static_url_path='', static_folder='static_pages_for_api')

@app.route('/')
def index():
    return "Hello World especially Enda"


@app.route('/books', methods=['GET'])
def getAll():
    return "served by getAll()"

@app.route('/books/<int:id>')
def findById(id):
    return "served by findById() with ID: " +str(id)

@app.route('/books',methods=['POST'] )
def create():
    return "Served by Create()"

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    return "served by update() with ID: " +str(id)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return "served by delete() with ID: " +str(id)




if __name__ == "__main__":
    app.run(debug = True)