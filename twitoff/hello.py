from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print('YOU VISITED THE HOMEPAGE')
    return "Hello World!"

@app.route("/about")
def about():
    print('YOU VISITED THE ABOUT PAGE')
    return "About Me (TODO)"

# $ FLASK_APP=hello.py flask run