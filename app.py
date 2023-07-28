from flask import Flask, render_template, url_for, jsonify
import psycopg2from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/franchise')
def franchise():
    return render_template('franchise.html')

@app.route('/search-cus')
def search_cus():
    data = get_table('vinyls')
    print('data',data)
    return render_template('search-cus.html', data=data)


if __name__ == "__main__": 
    app.run(debug=True) 
    #when going to debud set debug to False
