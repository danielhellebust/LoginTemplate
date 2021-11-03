from flask import Flask
from flask_pymongo import PyMongo

# PyMongo datanbase object
mongo =PyMongo()


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def create_app():
    app = Flask(__name__)

    # app.config variables should be wrapped in environment variables for security reasons.

    app.config['SECRET_KEY'] = 'sdfgdfghfjyuikyuiyukyuk'


    # MongoDB connection string to Atlas cluster. Username and password is admin and name of DB is LoginTemplate
    app.config['MONGO_URI'] = f'mongodb+srv://admin:admin@cluster0.rhshz.mongodb.net/LoginTemplate?retryWrites=true&w=majority'

    # Upload folder for product images
    app.config['UPLOAD_FOLDER'] = '/website/static/uploads'

    # Initializing the mongo database object.
    mongo.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app