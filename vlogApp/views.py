from flask import render_template, request, redirect, url_for
from vlogApp import app

@app.route('/')
def top():
    return render_template('Vlog_html/top.html')
  
@app.route('/register')
def register():
    return render_template('register.html')
  
@app.route('/login')
def login():
    return render_template('login.html')
  
@app.route('/myPage')
def myPage():
    return render_template('myPage.html')
  
@app.route('/makeVlog')
def makeVlog():
    return render_template('makeVlog.html')
  
@app.route('/view')
def view():
    return render_template('view.html')