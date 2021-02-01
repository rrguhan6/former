from flask import Flask, make_response
from flask_restful import Resource, reqparse, marshal_with
import pprint
from app import models, db, ma
import json
from app import serializer
import ast
from former import crud

BookSchema = serializer.BookSchema()
BookSchemas = serializer.BookSchema(many=True)


def _str2dict(data):
    return json.loads(data.replace("'", "\""))


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Books(Resource):
    def get(self):
        # breakpoint()
        books = models.Book.query.all()
        return BookSchemas.dump(books)


class BooksCreate(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('data')

    def post(self):
        data = BooksCreate.parser.parse_args()['data']

        data = _str2dict(data)
        book = models.Book(**data)

        db.session.add(book)
        db.session.commit()

        return {"data": data}


class FormBuilder(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('form')

    def post(self):
        data = FormBuilder.parser.parse_args()['form']
        _data = ast.literal_eval(data)

        data = {
            "form_schema": data
        }
        form = models.Form(**data)

        db.session.add(form)
        db.session.commit()

        crud.create_table(form.id, _data)

        return_data = {
            "id": f"{form.id}",
            "data": data,
            "url": f"/former/{form.id}"
        }

        return return_data


class Former(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('data')

    def get(self, id):
        form = models.Form.query.filter_by(id=id)
        try:
            _data = {
                "id": form[0].id,
                "form_schema": ast.literal_eval(form[0].form_schema),
                "error": False
            }

            return _data
        except:
            return make_response(404)

    def post(self, id):
        data = Former.parser.parse_args()
        _data = ast.literal_eval(data["data"])
        crud.insert(f'table_{id}', _data)
        return {"status": 200}


class TableData(Resource):
    def get(self, id):
        # breakpoint()
        data = crud.get_all(f'table_{id}', engine=db)
        print(data)
        return {"data": data}
