from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import hashlib
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "202cb962ac59075b964b07152d234b70"
app.permanent_session_lifetime = timedelta(hours=1)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:**********@localhost/flask_python13'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column('user_id', db.Integer, primary_key=True)
    login = db.Column('login', db.String(20))
    password = db.Column('password', db.String(32))
    email = db.Column('email', db.String(100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email


class Post(db.Model):
    _id = db.Column('post_id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(50))
    content = db.Column('content', db.String(1000))
    date_added = db.Column('date_added', db.DateTime())
    owner = db.Column('owner', db.String(20))

    def __init__(self, title, content, owner):
        self.title = title
        self.content = content
        self.date_added = datetime.now()
        self.owner = owner


@app.route('/')
def home():
    posts = Post.query.order_by(desc('date_added')).all()
    return render_template('home.html', posts=posts)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_login = request.form['user_login']

        user_password = hashlib.md5(request.form['user_password'].encode()).hexdigest()
        user_in_db = User.query.filter_by(login=user_login).first()
        if user_in_db:
            if user_password == user_in_db.password:
                session['login'] = user_login
                session['email'] = user_in_db.email
                flash('Logged in successfuly.', 'success')
                return redirect(url_for('user_profile'))
            else:
                flash('Wrong credentials!', 'danger')
                return redirect(url_for('login'))
        else:
            new_user = User(user_login, user_password, '')
            db.session.add(new_user)
            db.session.commit()
            session['login'] = user_login
            session['email'] = ''
            flash('New user created', 'success')
            return redirect(url_for('user_profile'))
    else:
        if 'login' in session:
            flash('Already logged in', 'info')
            return redirect(url_for('user_profile'))
        else:
            return render_template('login.html')

@app.route('/user_profile/', methods=['POST', 'GET'])
def user_profile():
    if 'login' in session:
        user_login = session['login']
        if request.method == 'POST':
            user_email = request.form['user_email']
            session['email'] = user_email
            user_in_db = User.query.filter_by(login=user_login).first()
            user_in_db.email = user_email
            db.session.commit()
            flash('Email was changed', 'success')
        return render_template('user.html', login=user_login, email=session['email'])
    else:
        flash('Please log in', 'info')
        return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.pop('login', None)
    session.pop('email', None)
    flash('Logged out', 'info')
    return redirect(url_for('login'))


@app.route('/delete/')
def delete():
    User.query.filter_by(login=session['login']).delete()
    db.session.commit()
    session.pop('login', None)
    session.pop('email', None)
    flash('User was deleted', 'success')
    return redirect(url_for('login'))


@app.route('/post/', methods=['POST', 'GET'])
def post():
    if 'login' in session:
            
        if request.method == 'POST':
            title = request.form['post_title']
            content = request.form['post_content']
            owner = session['login']
            new_post = Post(title, content, owner)
            db.session.add(new_post)
            db.session.commit()
            flash('Post saved', 'success')
            return redirect(url_for('post'))
        else:
            return render_template('post.html')
    else:
        return redirect(url_for('login'))
    

@app.route('/my_posts/')
def my_posts():
    if 'login' in session:
        posts = Post.query.filter_by(owner=session['login']).order_by(desc('date_added'))
        return render_template('my_posts.html', posts=posts)
    else:
        flash('You are not logged in', 'warning')
        return redirect(url_for('login'))


@app.route('/del_post/<post_id>')
def del_post(post_id):
    Post.query.filter_by(_id=post_id).delete()
    db.session.commit()
    flash('Post was deleted', 'info')
    return redirect(url_for('my_posts'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)