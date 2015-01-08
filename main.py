from flask import Flask, g
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config.from_pyfile('config.py')

from apps.posts import posts

app.register_blueprint(posts)

mongo = PyMongo(app, config_prefix='MONGO')


@app.before_request
def before_request():
    g.mongo = mongo


if __name__ == '__main__':
    app.run()