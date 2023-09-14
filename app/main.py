from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

# MySQL設定
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('db-search.html')

@app.route('/numbersearch')
def db_serch():
    number=int(request.form.get('number'))
    cur = mysql.get_db().cursor()
    cur.execute('select name from items')
    data=cur.fetchall()
    return render_template('search_result.html',data=data)

@app.route('/test')
def test():
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM items")
    data = cur.fetchall()
    return render_template('test.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
