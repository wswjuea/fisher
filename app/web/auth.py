from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # 从页面获取form表单提交的数据
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
        # ORM将数据导入数据库
    return render_template('auth/register.html', form=form)

@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        # 从数据库查询当前email的密码进行验证
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
            # remember=True:Cookie会被记忆,即使关闭浏览器也不会被清除
            # 登录成功则重定向到网址?后面的字段的网页文件
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)




@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass

@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass