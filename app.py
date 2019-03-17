from flask import (Flask, render_template)

DEBUG = True
PORT = 300
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')
@app.route('/entries')
def index():
    return render_template('index.html')


@app.route('/entries/add')
def add_entry():
    pass

@app.route('/entry')
def view_entry():
    return render_template('entry.html')


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)