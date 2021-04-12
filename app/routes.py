from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'PeaWarrior'}
  posts = [
    {
      'author': {'username': 'John'},
      'body': 'Today is a beautiful day!'
    },
    {
      'author': {'username': 'Billy'},
      'body': 'Yesterday was a beautiful day!'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash(f'Login requested for user {form.username.data}, remember_me {form.remember_me.data}')
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)