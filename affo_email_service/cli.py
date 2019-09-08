from flask_script import Manager
from flask_migrate import MigrateCommand

from affo_email_service.application import create_app


app = create_app()

manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
