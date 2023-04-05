from flask import Flask, url_for, redirect

app = Flask(__name__, static_url_path = '', static_folder = 'static_pages')

@app.route('/')
def index():
     return "<a href =" + url_for('getUser')+">getusers</a>"

@app.route('/user' , methods = ['GET'])
def getUser():
    return "Hello There "

@app.route('/user/<int:id>' , methods = ['GET'])
def getUserById(id):
    return "Getting by ID " + str(id)

@app.route('/user', methods = ['POST'])
def postUser():
    return "Hello There, Enda Is Posting"

@app.route('/invalid' , methods = ['GET'])
def invalid():
    return redirect (url_for('index'))


if __name__ == "__main__":
    app.run(debug = True)