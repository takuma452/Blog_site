from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from blogApp import db, app
from blogApp.models import User, Blog

@app.route('/')
def top():
    return render_template('blog_html/top.html') 

# アカウント登録処理
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        myPassword = request.form['password']
        hashed_pw = generate_password_hash(myPassword)

        # データベースに保存(model.User)
        user = User(username=username,email=email, hashed_pw=hashed_pw)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))  # 登録後はログインへ
    return render_template('blog_html/register.html')  # ← 修正

# ログイン
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        myPassword = request.form['password']

        # DBからユーザー取得(models.User)
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.hashed_pw, myPassword):
            return redirect(url_for('myPage'))
        else:
            error = "ログインに失敗しました。再度お試しください。"
            return render_template('blog_html/login.html', error=error)

    return render_template('blog_html/login.html') 

# マイページ-- 自身のブログを表示する。
@app.route('/myPage', methods=['GET', 'POST'])
def myPage():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        blog = Blog(title=title, content=content, author=author)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('myPage'))
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('blog_html/myPage.html', blogs=blogs)

#ブログを書く
@app.route('/makeBlog', methods=['GET', 'POST'])
def makeBlog():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            author = request.form['author']
            blog = Blog(title=title, content=content, author=author)
            db.session.add(blog)
            db.session.commit()
            return redirect(url_for('myPage'))
        return render_template('blog_html/makeBlog.html')