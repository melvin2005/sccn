from flask import render_template,Blueprint,redirect,request,session
from sccn import dbconn,models
import hashlib

lg = Blueprint('lg',__name__)

#库里密码存的密文，我在库里建了个用户，密码为md5加密
def mymd5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    res = obj.hexdigest()
    return res

@lg.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('user')
    passwd = request.form.get('pwd')
    pwd = mymd5(passwd)

    result = dbconn.session.query(models.LoginUser).filter(models.LoginUser.login_name == username)

    for item in result:
        if item.login_pwd == pwd:
            session['user']=username
            return redirect('/index')
        else:
            return 'passwd error'

    dbconn.session.remove()

    #此处需要定义返回信息，否则app.py里的make_response函数将会报错
    return 'user may not exists'
