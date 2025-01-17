from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/admin.html')
def crack(name=None):
    return render_template('admin.html', name=name)


@app.route('/pull.html')
def pull(name=None):
    return render_template('admin.html', name=name)


if __name__ == '__main__':
    app.run()