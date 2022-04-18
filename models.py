from exts import db
from datetime import datetime


class EmailCpatchaModel(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    captcha = db.Column(db.String(4), nullable=False)
    # 记录发送时间 不加括号代表当前时间 加括号代表运行项目的时间
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)  # 用户名
    password = db.Column(db.String(200), nullable=False)  # 密码 加密存储
    email = db.Column(db.String(50), nullable=False, unique=True)  # 邮箱
    avatar = db.Column(db.String(200), nullable=False, default='/static/image/default.png')  # 头像
    join_time = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 加入时间


class VideoModel(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uiid = db.Column(db.String(100), nullable=False, unique=True)  # 视频的 uiid，用于存储视频的唯一标识
    name = db.Column(db.String(100), nullable=False)  # 用于存储视频原来的名字
    yolo_uiid = db.Column(db.String(200))  # 用于存储解析后视频的 位置
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    user = db.relationship('UserModel', backref=db.backref("video", uselist=False))  # 一对一关系
