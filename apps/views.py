from functools import wraps
from apps import app
from flask import Flask,redirect,request,url_for,render_template,flash
from flask import session
from apps.model import User
from apps.forms import LoginForm,RegistForm
from apps import db
from flask_login import login_user, logout_user, login_required
#
# def user_login_req(f):
#     @wraps(f)
#     def decorated_function(*args,**kwargs):
#         if "name"not in session:
#             return redirect(url_for("login"),next=request.url)
#         return f(*args,**kwargs)
#     return decorated_function




@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")



@app.route('/login/',methods=['GET','POST'])
# @login_required
def login():


    form=LoginForm()

    if form.validate_on_submit():
        uesername=request.form["name"]
        userpwd=request.form['pwd']

        user_x=User.query.filter_by(name=uesername).first()
        if not user_x:
            flash("用户名不存在",category='err')
            return render_template('login.html',form=form)
        else:
            if not user_x.check_pwd(str(userpwd)):
                flash("用户密码错误",category='err')
                return render_template('login.html', form=form)
            else:
                login_user(user_x, form.remember_me.data)
                session["name"]=user_x.name
                # return redirect(url_for("success"))
                return redirect(request.args.get('next') or url_for('success'))
    return render_template("login.html",form=form)

@app.route('/loginout')
# @user_login_req
def loginout():
    logout_user()
    # session.pop("name",None)
    return redirect(url_for('index'))



@app.route('/regist/',methods=['GET','POST'])

def regist():

    form=RegistForm()
    if form.validate_on_submit():
        username=form.name.data
        useremail = form.email.data
        user_x = User.query.filter_by(name=username).first()
        user_e=User.query.filter_by(email=useremail).first()
        if user_x:

            flash("用户名已经存在！", category="err")
            return render_template("regist.html", form=form)
        elif user_e:
            flash("邮箱已经被注册！", category="err")

        user=User()
        user.name=form.name.data
        user.pwd = form.pwd.data
        user.email = form.email.data
        db.session.add(user)
        db.session.commit()
        flash("注册成功",category="ok")
        return redirect(url_for("login",username=user.name))
    return render_template("regist.html",form=form)


@app.route('/success',methods=['GET','POST'])
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug = True)