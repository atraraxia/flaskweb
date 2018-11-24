from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,DateField,SubmitField,BooleanField
from wtforms.validators import DataRequired,length,Email
from flask_login import UserMixin

class RegistForm(FlaskForm):
    name=StringField(label="用户名",validators=[DataRequired(message="用户名不能为空！"),length(3,12)],
                          render_kw={"placeholder":"请输入用户名",
                                     "class": "form-control"})

    pwd=PasswordField(label="密码",validators=[DataRequired(message="密码长度在3-12个字符之间"),length(3,12)],
                          render_kw={"placeholder":"请输入密码",
                                     "class": "form-control"})

    email=StringField(label="邮箱",validators=[DataRequired(),Email(message='邮箱格式不合法'),length(6,36)],
                          render_kw={"placeholder":"请输入邮箱",
                                     "class": "form-control"})


    submit=SubmitField(
        label="注册",render_kw={"class": "btn btn-success",
                              "value":"注册"}
    )

class LoginForm(FlaskForm):
    name = StringField(label="用户名", validators=[DataRequired(message="用户名不能为空！")],
                       render_kw={"placeholder": "请输入用户名",
                                  "class": "form-control"})

    pwd = PasswordField(label="密码",
                        render_kw={"placeholder": "请输入密码",
                                   "class": "form-control"})

    remember_me = BooleanField(label="记住我")

    submit=SubmitField(
        label="登录",render_kw={"class": "btn btn-success",
                              "value":"登录"}
    )