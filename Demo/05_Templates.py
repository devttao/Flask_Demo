from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<html><body><h1>Hello World</h1></body></html>'


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)


@app.route('/hello2/<int:score>')
def hello_score(score):
    return render_template('hello2.html', marks=score)


@app.route('/result')
def result():
    dict1 = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=dict1)


if __name__ == '__main__':
    app.run(debug=True)
