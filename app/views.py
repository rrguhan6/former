from flask import Flask
from flask_restful import Resource,reqparse

from app import models

parser = reqparse.RequestParser()
parser.add_argument('task')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Books(Resource):
    query = models.Book.query.all()
    model = models.Book

    def get(self):
        books = self.query
        return books

    def post(self):

