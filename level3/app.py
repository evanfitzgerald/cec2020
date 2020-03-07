from flask import Flask
from flask_cors import CORS
import json

from Cube import Cube
from readfile import readfile
from testJ import testJ

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/getsolvedgrid/<file_name>')
def fetch_solved_grid(file_name):
    c = readfile(file_name)
    data = json.dumps({
        'size': c.size,
        'grid': c.GetHex(True)
    })
    return data

@app.route('/getscrambledgrid/<file_name>')
def fetch_scrambled_grid(file_name):
    c = readfile(file_name)
    data = json.dumps({
        'size': c.size,
        'grid': c.GetHex(False)
    })
    return data

@app.route('/getdronegrid/<file_name>')
def fetch_drone_grid(file_name):
    c = testJ(file_name)
    data = json.dumps({
        'size': c.size,
        'grid': c.GetHex(False)
    })
    return data

if __name__ == '__main__':
    app.run()
