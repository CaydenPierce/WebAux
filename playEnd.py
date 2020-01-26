from flask import render_template, make_response
from flask_restful import Resource, reqparse, fields, marshal_with

class playEnd(Resource):
    def __init__(self, myPlayer):
        self.myPlayer = myPlayer
        
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('songname', type=str)
        args = parser.parse_args()

        query = args['songname']
        print(query)
        if query.lower() == "stop" or query.lower() == "pause":
            self.myPlayer.stop()
        else:
            self.myPlayer.play(query)

        return {"success" : 1}

