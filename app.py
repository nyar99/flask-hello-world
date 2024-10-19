from flask import Flask
from most_played_note import most_played_note
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/most_played_note')
def most_played_note():
    return f'Most played note: {most_played_note()}'