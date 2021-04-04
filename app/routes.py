from flask import render_template
from app import app

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