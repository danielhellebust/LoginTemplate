from flask import Blueprint, render_template, request, flash, redirect, current_app, url_for, session


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    """ Route to home page """
    if 'email' in session:
        return render_template("home.html")

    flash('Please login to enter site', category='danger')

    return redirect(url_for('auth.login'))




