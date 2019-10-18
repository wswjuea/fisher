from flask import Flask
from flask_login import LoginManager
from app.models.base import db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    # static_folder静态文件夹路径，最好不要指定
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    # 初始化loginmanager
    # 没有登录则跳转到登录界面

    with app.app_context():
        db.create_all()
    # 如果表不存在则生成表
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)