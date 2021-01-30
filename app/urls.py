from app import views
from app import app
from flask_restful import Api

api = Api(app)


api.add_resource(views.HelloWorld, '/')
api.add_resource(views.Books, '/books')