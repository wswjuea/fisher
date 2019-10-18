from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger


db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    # 设定为基类,sqlalchemy不会识别出无主键错误
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
            # 当前对象是否包含名字为key的属性
