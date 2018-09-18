# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World !"


def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.add_url_rule('/', 'hello', hello_world)
    app.run(host='0.0.0.0', port=7070, debug=True)
