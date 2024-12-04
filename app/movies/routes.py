from flask import render_template
from .import movies

@movies.route('/')
def index():
    return render_template('movies/index.html')