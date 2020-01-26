#flask
from flask import Flask, render_template, flash, redirect, jsonify
from flask import request

#flask_restful
from flask_restful import Api

#custom
from playEnd import playEnd
from player import Player

#regular
import os

app = Flask(__name__)
app.debug=True
app._static_folder = os.path.abspath("static/")

api = Api(app) #flask_restful

myPlayer = Player()
api.add_resource(playEnd, "/", resource_class_args=[myPlayer])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
