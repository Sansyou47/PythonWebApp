from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#フォームに入力された数値を倍にする処理
@app.route('/multiply', methods=['POST'])
def multiply():
    #フォームから数値を受け取る
    number = int(request.form['number'])
    #数値が負の数なら失敗にする
    if number<0:
        return render_template('result-failure.html',result=number)
    #正の数なら倍にする処理を実行して返す
    else:
        result = number * 2
        return render_template('result-success.html', result=result)

#テスト用のページ
@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)