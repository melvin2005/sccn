from sccn import create_app,dbconn
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sccn import create_app,dbconn

app = create_app()
# manager = Manager(app)
# Migrate(app,dbconn)
# manager.add_command('dbconn',MigrateCommand)

if __name__=='__main__':
    app.run()
    # manager.run()
