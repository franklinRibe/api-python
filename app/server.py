#!/usr/bin/python3
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db = create_engine('sqlite:///users.db')

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        conn = db.connect()
        query = conn.execute("select * from users")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)
        
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0')