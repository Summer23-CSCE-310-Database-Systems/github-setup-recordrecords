from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mzlmdawh:68uKpdQLKb5UwzZces5mCIbhtG2yOH3o@batyr.db.elephantsql.com/mzlmdawh'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

"""
    SETUP:
        To run the app:
            export FLASK_APP=app.py
            flask run 
        
        DO THE ABOVE FIRST!

        To add, delete, change any columns or add new models:
            flask db migrate
            flask db upgrade
"""
class ManagerModel(db.Model):
    __tablename__ = 'managers'

    mana_id = db.Column(db.Integer, primary_key=True)
    mana_fname = db.Column(db.String())
    mana_lname = db.Column(db.String())
    mana_phone = db.Column(db.String())

    def __init__(self, id, fname, lname, phone):
        self.mana_id = id
        self.mana_fname = fname
        self.mana_lname = lname
        self.mana_phone = phone

    def __repr__(self):
        return f'<Manager {mana_id}>'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/franchise')
def franchise():
    return render_template('franchise.html')

@app.route('/search-cus')
def search_cus():
    return render_template('search-cus.html')


if __name__ == "__main__": 
    app.run(debug=True) 
    #when going to debud set debug to False
