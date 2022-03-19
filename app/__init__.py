from flask import Flask
from app.routes.posts_route import get_posts_route


def create_app():
    app = Flask(__name__)

    get_posts_route(app)

    return app