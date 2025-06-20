from flask import render_template, request, redirect, url_for
from vlogApp import app

@app.route('/')
def top():
    return render_template('vlog_html/top.html')
  
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # 登録処理をここに追加
        # 例えば、データベースにユーザー情報を保存するなど
        print(f"Email: {email}, Password: {password}")
        return '登録完了'
    else:
        return render_template('register.html')


# @app.route('/register-post', methods=['POST'])
# def register():
#     return render_template('register.html')
  
@app.route('/login')
def login():
    return render_template('vlog_html/login.html')
  
@app.route('/myPage')
def myPage():
    return render_template('vlog_html/myPage.html')
  
@app.route('/makeVlog')
def makeVlog():
    return render_template('vlog_html/makeVlog.html')