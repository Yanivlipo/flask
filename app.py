from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/redirect')
def hello_redirect():
    return redirect('/')


@app.route('/url_for')
def hello_url_for():
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True)
