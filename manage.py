from sccn import create_app,dbconn
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sccn import create_app,dbconn
from flask import session,redirect,request

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

    return redirect('/login')

if __name__=='__main__':
    app.run()
    # manager.run()
