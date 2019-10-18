from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.models.base import Base

from sqlalchemy import Column, Integer, String, Boolean, Float
from flask_login import UserMixin


class User(Base, UserMixin):
    # __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    # wx_open_id = Column(String(50))
    # wx_name = Column(String(12))

    _password = Column('password', String(100), nullable=False)
    # 传递的字符串password就是新建数据库表的属性名,如果没有则默认的对象属性名为数据库表属性名

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
    # 获取密码,将密码加密后传回

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
    # 验证传入的密码

    # def get_id(self):
    #     return self.id
    # # flask-login插件必须要手动编写获取用户id的方法,已继承
@login_manager.user_loader
# login_manager在app.__init__初始化
def get_user(uid):
    User.query.get(int(uid))
#     查询主键,直接用get()
