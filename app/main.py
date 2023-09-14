from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

# MySQL設定(セキュリティを考慮して環境変数から読み出しを行っています。)
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql = MySQL(app)

# indexルート
@app.route('/')
def index():
    return render_template('index.html')

# 検索フォーム
@app.route('/search')
def search():
    return render_template('db-search.html')

# SQLによるデータベースからの参照処理
@app.route('/numbersearch')
def db_serch():
    # フォームから値の受け取り
    number=int(request.form.get('number'))
    cur = mysql.get_db().cursor()
    # SQLの実行
    cur.execute('select name from items')
    data=cur.fetchall()
    return render_template('search_result.html',data=data)

# testページ
@app.route('/test')
def test():
    cur = mysql.get_db().cursor()
    # テーブルの情報をすべて返す
    cur.execute("SELECT * FROM items")
    data = cur.fetchall()
    return render_template('test.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
