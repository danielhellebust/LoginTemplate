import os
from bson import ObjectId
from datetime import datetime
from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for, session
from werkzeug.utils import secure_filename
from . import mongo, ALLOWED_EXTENSIONS


views = Blueprint('views', __name__)


def allowed_file(filename):
    """ Function to check if uploaded image file from add_product() route has valid file extension. """

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@views.route('/', methods=['GET', 'POST'])
def home():
    """ Route to home page """
    if 'email' in session:
        return render_template("home.html")

    return redirect(url_for('auth.login'))




