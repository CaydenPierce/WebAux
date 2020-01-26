from flask import render_template, make_response
from flask_restful import Resource, reqparse, fields, marshal_with

from player import playYoutube
from getSong import getSongUrl

class playEnd(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('songname', type=str)
        args = parser.parse_args()

        query = args['songname']

        playYoutube(getSongUrl(query))

