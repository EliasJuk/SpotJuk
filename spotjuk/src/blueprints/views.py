from flask import render_template

def init_app(app):
  @app.route('/')
  def index():
    albums = [
      {
        'artista':'Artista-01',
        'capa': 'capa-01.jpg'
      },
      {
        'artista':'Artista-02',
        'capa': 'capa-02.jpg'
      },
      {
        'artista':'Artista-03',
        'capa': 'capa-03.jpg'
      },
      {
        'artista':'Artista-04',
        'capa': 'capa-04.jpg'
      },
      {
        'artista':'Artista-05',
        'capa': 'capa-05.jpg'
      },
      {
        'artista':'Artista-06',
        'capa': 'capa-06.jpg'
      },
      {
        'artista':'Artista-07',
        'capa': 'capa-07.jpg'
      },
      {
        'artista':'Artista-08',
        'capa': 'capa-08.jpg'
      }
    ]
    return render_template('index.html', albums=albums)

  @app.route('/login')
  def login():
    return render_template('login.html')