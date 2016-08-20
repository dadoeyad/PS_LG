from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cats.html')


@app.route('/data/<path:filename>')
def data(filename):
    return send_from_directory('data', filename)
