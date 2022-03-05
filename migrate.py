import models
import app

from flask_migrate import Migrate

application = app.app
migrate = Migrate(application, app.db)
