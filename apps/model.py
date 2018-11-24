from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from apps import db,login_manager
from flask_login import UserMixin,login_user


class User(UserMixin,db.Model):
    _tablename = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True,nullable=False)
    pwd = db.Column(db.String(120),nullable=False)
    email= db.Column(db.String(120), unique=True,nullable=False)
    addtime=db.Column(db.DATETIME,index=True,default=datetime.now())

    def __repr__(self):
        return '<Role %r>' % self.username

    def check_pwd(self,pwd):
        return self.pwd==pwd

@login_manager.user_loader
def load_user(id):
        return User.query.get(id)

if __name__=="__main__":
    db.drop_all()
    db.create_all()