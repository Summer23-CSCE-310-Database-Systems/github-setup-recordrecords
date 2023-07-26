from flask import Flask, render_template, url_for

app = Flask(__name__)

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
