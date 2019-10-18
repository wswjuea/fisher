from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # 这里的user是上面的relationship创建的User对象
    isbn = Column(String(15), nullable=False)
    # 作为gift的书籍可能是多本的,所以不唯一
    launched = Column(Boolean, default=False)
    # launched记录判断书籍是否送出