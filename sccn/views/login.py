from flask import render_template,Blueprint
from sccn import dbconn,models
lg = Blueprint('lg',__name__)

@lg.route('/login')
def login():
    #return render_template('login.html')
    result = dbconn.session.query(models.LoginUser).all()
    for item in result:
        print(item.id,item.name,item.login_pwd)
    dbconn.session.remove()
    return 'login'