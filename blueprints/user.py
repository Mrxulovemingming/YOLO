from flask import Blueprint, render_template, request, url_for, redirect, flash, session, jsonify
from exts import mail, db
from flask_mail import Message
from models import EmailCpatchaModel, UserModel
from datetime import datetime
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

import string
import random

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session["user_id"] = user.id
                return redirect("/")
            else:
                flash("邮箱和密码不匹配")
                return redirect(url_for('user.login'))
        else:
            flash("邮箱或密码格式错误")
            return redirect(url_for('user.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            hash_password = generate_password_hash(password)
            user = UserModel(username=username, email=email, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            return render_template(url_for("user.register"))  # 返回错误信息

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("user.login"))

@bp.route('/captcha', methods=['POST'])
def send_captcha():
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))
    email = request.form.get('email')
    if not mail:
        return jsonify({'code': 400, 'msg': '邮箱不能为空'})
    else:
        user_model = UserModel.query.filter_by(email=email).first()
        if user_model:
            flash("邮箱已经被注册")
            return jsonify({'code': 400, 'message': '该邮箱已注册'})
        message = Message('YOLO 小站 验证码', recipients=[email],
                          body=f'【YOLO 小站】您的注册验证码是：{captcha}, 请勿泄露给他人！')
        mail.send(message)
        captcha_model = EmailCpatchaModel.query.filter_by(email=email).first()
        if not captcha_model:
            captcha_model = EmailCpatchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        else:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        return jsonify({'code': 200, 'msg': '验证码发送成功'})
