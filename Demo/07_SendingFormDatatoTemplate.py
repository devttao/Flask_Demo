from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result2 = request.form
        return render_template("result2.html", result=result2)


if __name__ == '__main__':
    app.run(debug=True)
