from flask import Flask, render_template
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

# MySQL設定
app.config['MYSQL_DATABASE_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
app.config['MYSQL_DATABASE_DB'] = 'pytest'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM items")
    data = cur.fetchall()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
