from flask import Flask
from flask_restful import Resource, Api, reqparse

class uploadImg(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file')