from sccn import create_app,dbconn
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = create_app()


if __name__=='__main__':
    app.run()