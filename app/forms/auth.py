from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email
from wtforms import ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[
        DataRequired(),
        Length(8, 64),
        Email(message='invalidate email')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空, 请输入你的密码'),
        Length(6, 32)
    ])

    nickname = StringField(validators=[
        DataRequired(),
        Length(2, 10, message='昵称至少需要2个字符, 最多10个字符')
    ])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')
        # 根据方法名,自动对应email的验证;filter_by类似mysql的where

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')

class LoginForm(Form):
    email = StringField(validators=[
        DataRequired(),
        Length(8, 64),
        Email(message='invalidate email')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空, 请输入你的密码'),
        Length(6, 32)
    ])

