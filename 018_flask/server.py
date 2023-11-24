from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import hashlib
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(hours=10)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/flask_python13'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column('login', db.String(20))
    password = db.Column('password', db.String(32))
    email = db.Column('email', db.String(50))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_login = request.form['user-login']
        user_password = hashlib.md5(request.form['user-password'].encode()).hexdigest()
        user_in_db = User.query.filter_by(login=user_login).first()
        if user_in_db:
            if user_password == user_in_db.password:
                session['login'] = user_login
                session['email'] = user_in_db.email
                flash('Signed in successfuly', 'success')
                return redirect(url_for('user_profile'))
            else:
                flash('Wrong credentials', 'danger')
                return redirect(url_for('login'))
        else:
            new_user = User(user_login, user_password, '')
            db.session.add(new_user)
            db.session.commit()
            session['login'] = user_login
            session['email'] = ''
            flash('User was created', 'success')
            return redirect(url_for('user_profile'))
    else:
        if 'login' in session:
            flash('Already signed in', 'info')
            return redirect(url_for('user_profile'))
        else:
            return render_template('login.html')

@app.route('/user_profile/', methods=['GET', 'POST'])
def user_profile():
    if 'login' in session:
        user_login = session['login']
        if request.method == 'POST':
            user_email = request.form['user-email']
            user_in_db = User.query.filter_by(login=user_login).first()
            user_in_db.email = user_email
            db.session.commit()
            session['email'] = user_email
        return render_template('user_profile.html', user_email=session['email'])
    else:
        return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    session.pop('login', None)
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/delete/')
def delete():
    user_login = session['login']
    User.query.filter_by(login=user_login).delete()
    db.session.commit()
    session.pop('login', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/admin/')
def admin():
    return redirect(url_for('user_profile', name='Roman'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)