#Module Imports
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Dummy Data

posts = [
    {
        'author': "Enda Lynch",
        'title': "Blog post 1",
        "content": "First Post Content",
        "date_posted": "April 13th 2023"
    },
    {
        'author': "Colm Lynch",
        'title': "Blog post 2",
        "content": "Second Post Content",
        "date_posted": "April 14th 2023"
    }
]



#root page(Homepage)
@app.route("/") 
@app.route("/home") 
def home():
    return render_template('home.html', posts = posts) # posts variable within the template is equal to the dummy data

#About page
@app.route("/about") 
def about():
    return render_template('about.html', title = 'About')




if __name__== '__main__':
    app.run(debug=True)
