from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from function import search
import os, hashlib, pymysql

app = Flask(__name__)

# MySQL設定(環境変数から読み取り)
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = 'mysql'

mysql = MySQL(app)

# indexルート
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dbdelete')
def dbdelte():
    cur = mysql.get_db().cursor()
    # テーブルの情報をすべて返す
    cur.execute("SELECT * FROM employee")
    data = cur.fetchall()
    return render_template('db_delete.html', data=data)

# 検索フォーム
@app.route('/search')
def search():
    return render_template('db_search.html')

# 新規登録フォーム
@app.route('/entry')
def entry():
    return render_template('entry.html')

@app.route('/delete', methods=['POST'])
def delete():
    number=int(request.form.get('radio'))
    # MySQLへ接続
    conn=mysql.get_db()
    cur=conn.cursor()
    cur.execute("delete from employee where number = %s",(number))
    conn.commit()
    cur.close()
    return redirect('/show')

@app.route('/numbersearch', methods=['POST'])
def db_serch():
    # POSTメソッドがリクエストされた場合のみ実行
    if request.method == 'POST':
        # フォームから値の受け取り
        number=request.form.get('number')
        if number == "None":
            return render_template('index.html')
        else:
            cur = mysql.get_db().cursor()
            # SQL実行
            cur.execute("select name, category from employee where number = %s",(number))
            data=cur.fetchone()
            cur.close()
            return render_template('search_result.html',name=data[0],category=data[1])
    # POSTメソッドがリクエストされていないのでリダイレクトする
    else:
        return redirect('/')

# 新規登録フォームのデータをデータベースへ登録する処理
@app.route('/dbinsert', methods=['POST'])
def dbinsert():
    # データの受け取り（5個）
    name=request.form.get('name')
    category=request.form.get('category')
    auth=int(request.form.get('auth'))
    gender=request.form.get('gender')
    start=int(request.form.get('start'))
    finish=int(request.form.get('finish'))
    passwd=request.form.get('pass')

    # パスワードはハッシュ化して登録する
    passwdhs=hashlib.sha256(passwd.encode()).hexdigest()

    # MySQLへ接続
    conn=mysql.get_db()
    cur=conn.cursor()
    # SQL実行
    cur.execute("INSERT INTO employee(name, category, auth, gender, start, finish, pass) VALUES(%s, %s, %s, %s, %s, %s, %s)",(name,category,auth,gender,start,finish,passwdhs))
    conn.commit()
    cur.close()
    return redirect('/show')

# testページ
@app.route('/show')
def test():
    cur = mysql.get_db().cursor()
    # テーブルの情報をすべて返す
    cur.execute("SELECT * FROM employee")
    data = cur.fetchall()
    return render_template('show_dbdata.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
