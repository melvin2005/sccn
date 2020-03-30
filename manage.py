from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sccn import create_app,dbconn
from flask import session,redirect,request,render_template

app = create_app()
# manager = Manager(app)
# Migrate(app,dbconn)
# manager.add_command('dbconn',MigrateCommand)

@app.before_request
def before():
    if request.path == '/login':
        return None

    if session.get('user'):
        return None

    return render_template('login.html')

if __name__=='__main__':
    app.run()
    # manager使用方法：cmd中执行python manage.py runserver -h 127.0.0.1 -p 8080
    # manager.run()