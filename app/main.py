from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiply', methods=['POST'])
def multiply():
    number = int(request.form['number'])
    if number<0:
        return render_template('result-failure.html',result=number)
    else:
        result = number * 2
        return render_template('result-success.html', result=result)

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)