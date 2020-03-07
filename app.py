from flask import Flask
from flask_cors import CORS
import json

from Cube import Cube
from readfile import readfile

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/getgrid/<file_name>')
def fetch_grid(file_name):
    c = readfile(file_name)
    data = json.dumps({
        'size': c.size,
        'grid': c.GetHex()
    })
    return data

if __name__ == '__main__':
    app.run()
