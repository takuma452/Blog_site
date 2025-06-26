from blogApp import app,db
with app.app_context():
    db.create_all()
    print("データベース作成完了")