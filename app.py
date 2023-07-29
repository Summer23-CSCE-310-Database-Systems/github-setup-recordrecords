from flask import Flask, render_template, url_for, jsonify, request, redirect
import psycopg2

app = Flask(__name__)

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

cursor = None
def connect_db():
    db_link = 'postgres://mzlmdawh:68uKpdQLKb5UwzZces5mCIbhtG2yOH3o@batyr.db.elephantsql.com/mzlmdawh'

    conn = psycopg2.connect(db_link)
    return conn

@app.route('/get_data', methods=['GET'])
def get_table(table):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        # Replace 'your_table_name' with the name of the table you want to query
        query = f"SELECT * FROM {table};"
        print('executing ', query)
        cursor.execute(query)
        # Fetch all data from the query result
        data = cursor.fetchall()
        # Close the cursor and database connection
        cursor.close()
        conn.close()
        # Convert data to a JSON response
        return data

    except Exception as e:
        print("ERROR")
        return jsonify({'error': str(e)})

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        custID = request.form.get('CustomerID')
        manID = request.form.get('ManagerID')
        print('custid', custID, 'manID', manID)
        if custID  != '':
            return redirect(url_for('search_cus'))
        elif manID  != '':
            return redirect(url_for('manager_vinyl'))
        else:
            return render_template('index.html')
    return render_template('index.html')
    


@app.route('/franchise')
def franchise():
    return render_template('franchise.html')

@app.route('/search-cus')
def search_cus():
    data = get_table('vinyls')
    print('data',data)
    return render_template('search-cus.html', data=data)

@app.route('/manager-vinyl')
def manager_vinyl():
    data = get_table('vinyls')
    print('data',data)
    return render_template('manager.html', data=data)

if __name__ == "__main__": 
    app.run(debug=True) 
    #when going to debud set debug to False
