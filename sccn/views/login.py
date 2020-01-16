from flask import render_template,Blueprint

lg = Blueprint('lg',__name__)

@lg.route('/login')
def login():
    return render_template('login.html')