from flask import (Flask, render_template)
from journal import app

@app.route('/')
@app.route('/entries')
def index():
    return render_template('index.html')


@app.route('/entries/add')
def add_entry():
    pass

@app.route('/entry/')
def view_entry():
    return render_template('entry.html')

@app.route('/entry/edit')
def edit_entry():
    return render_template('edit.html')
