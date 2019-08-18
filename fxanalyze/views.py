from flask import request, redirect, url_for, render_template, flash
from fxanalyze import app


@app.route('/')
def show_entries():
    return render_template('show_entries.html')


@app.route('/add', methods=['POST'])
def add_entry():
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
