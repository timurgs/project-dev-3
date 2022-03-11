export FLASK_APP=migrate.py
export FLASK_ENV=development
export FLASK_DEBUG=0
flask db init
flask db migrate
flask db upgrade