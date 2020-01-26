#flask
from flask import Flask, render_template, flash, redirect, jsonify
from flask import request

#flask_restful
from flask_restful import Api

#custom
from playEnd import playEnd
from player import playYoutube

#regular
import os

app = Flask(__name__)
app.debug=True
app._static_folder = os.path.abspath("static/")

api = Api(app) #flask_restful

api.add_resource(playEnd, "/")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
