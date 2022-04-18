import wtforms
from wtforms.validators import DataRequired, email, EqualTo, length
from models import EmailCpatchaModel, UserModel


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=4, max=25)])
    email = wtforms.StringField( validators=[email()])
    captcha = wtforms.StringField( validators=[length(min=4, max=4)])
    password = wtforms.StringField( validators=[length(min=6, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo('password', message='Passwords must match')])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCpatchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            raise wtforms.ValidationError('邮箱验证码错误！')
        return True

    def validate_email(self, field):
        email = field.data
        if UserModel.query.filter_by(email=email).first():
            raise wtforms.ValidationError('邮箱已被注册！')
        return True

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
