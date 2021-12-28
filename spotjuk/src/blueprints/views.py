from flask import render_template

def init_app(app):
  @app.route('/')
  def index():
    return render_template('index.html')

  @app.route('/login')
  def login():
    return render_template('login.html')