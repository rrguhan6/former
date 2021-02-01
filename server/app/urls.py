from app import views
from app import app
from flask_restful import Api

api = Api(app)


api.add_resource(views.HelloWorld, '/api/')
api.add_resource(views.Books, '/api/books/')
api.add_resource(views.BooksCreate, '/api/booksCreate/')
api.add_resource(views.FormBuilder, '/api/form/')
api.add_resource(views.Former, '/api/former/<int:id>')
api.add_resource(views.TableData, '/api/records/<int:id>')
