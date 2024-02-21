""" app.pt """
from flask import Flask
from web_site.models.User_model import User
from web_site import db, app
from web_site import models

from web_site.views.app_views import app_views
from web_site.views.login import app_login
from flask_login import LoginManager
from os import getenv, path

DB = 'eBook_db.db'


app.register_blueprint(app_views)
app.register_blueprint(app_login)

login_manager = LoginManager()
login_manager.login_view = 'app_login.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.errorhandler(404)
def page_not_found(err):
    """handler"""
    return {"error": "Not found"}, 404

@app.errorhandler(400)
def page_not_found(err):
    """handler"""
    msg = err.description
    return msg, 400

@app.teardown_appcontext
def close_db(err):
    db.session.close()

def create_database(app):
    if not path.exists('~/eBookClub/instance' + DB):
        with app.app_context():
            db.create_all()


if __name__ == "__main__":
    host = '178.128.208.215'
    port = '5000'
    create_database(app)
    app.run(debug=True, host=host, port=port, threaded=True)

