from flask import Flask, render_template, url_for, jsonify, request, redirect
import psycopg2

app = Flask(__name__)

cursor = None
def connect_db():
    db_link = 'postgres://mzlmdawh:68uKpdQLKb5UwzZces5mCIbhtG2yOH3o@batyr.db.elephantsql.com/mzlmdawh'

    conn = psycopg2.connect(db_link)
    return conn

def delete_from_db(table, _id, id_type):
    # Open connection
    conn = connect_db()
    curr = conn.cursor()

    # Table is the table you'll want to query, id_type is the specific attr, _id is the attr itself
    query = f'DELETE FROM {table} WHERE {id_type} = {_id}'
    print('executing', query)
    curr.execute(query)
    conn.commit()

    # Close connection
    curr.close()
    conn.close()

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
        if custID != '':
            return redirect(url_for('search_cus'))
        elif manID != '':
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

# Vinyl operations
@app.route('/admin-vinyl')
def manager_vinyl():
    data = get_table('vinyls')
    print('data',data)
    return render_template('admin-vinyl.html', data=data)

@app.route('/admin-vinyl/delete', methods=['GET', 'POST'])
def delete_vinyl():
    if request.method == 'POST':
        vin_id = request.form['del']
        delete_from_db('vinyls', vin_id, 'vin_id')
    return redirect(url_for('manager_vinyl'))

@app.route('/admin-vinyl/update', methods=['GET', 'POST'])
def update_vinyl():
    if request.method == 'POST':
        pass

# Customer operations
@app.route('/admin-cust')
def manager_cust():
    data = get_table('customers')
    print('data', data)
    return render_template('admin-cust.html', data=data)

@app.route('/admin-cust/delete', methods=['GET', 'POST'])
def delete_cust():
    if request.method == 'POST':
        cust_id = request.form['del']
        delete_from_db('customers', cust_id, 'cust_id')
    return redirect(url_for('manager_cust'))

# Manager operations
@app.route('/admin-mana')
def manager_mana():
    data = get_table('managers')
    print('data', data)
    return render_template('admin-manager.html', data=data)

@app.route('/admin-mana/create', methods=['GET', 'POST'])
def create_mana():
    if request.method == 'POST':
        print(request.form)
        if all([request.form[item] != '' for item in request.form]):
            print("HELP")
            # All items are accounted for
            query = f"""
            INSERT INTO managers (mana_fname, mana_lname, mana_phone)
            VALUES ('{request.form['fname']}', '{request.form['lname']}', '{request.form['phone']}')
            """
            conn = connect_db()
            curr = conn.cursor()

            print('executing', query)

            curr.execute(query)
            conn.commit()
            curr.close()
            conn.close()
    return redirect(url_for('manager_mana'))

if __name__ == "__main__": 
    app.run(debug=True) 
    #when going to debud set debug to False
