from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def hello():
    return 'Welcome to Flask'

