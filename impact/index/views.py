from flask import render_template, request, Blueprint

index = Blueprint('index', __name__)

@index.route('/')
def index():
    return render_template('index.html')

@index.route('/about')
def about():
    return render_template('about.html')