from flask import Flask, redirect, url_for, render_template, request
import hashlib

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'name': 'Roman',
        'surname': 'Kutselepa',
        'age': 35
    }
    return render_template('home.html',
                           user_name='Roman',
                           content='I am some content for Flask website.',
                           context=context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_login = request.form['user-login']
        user_password = hashlib.md5(request.form['user-password'].encode()).hexdigest()
        return redirect(url_for('user_profile', name=user_login))
    else:
        return render_template('login.html')

@app.route('/<name>/')
def user_profile(name):
    return f'Hello {name}!'


@app.route('/admin/')
def admin():
    return redirect(url_for('user_profile', name='Roman'))


if __name__ == '__main__':
    app.run(debug=True)