from flask import render_template,Blueprint,redirect,request,session

idx = Blueprint('idx',__name__)

@idx.route('/index')
def index():
    return render_template('index.html')
