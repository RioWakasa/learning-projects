import pymysql
from flask import Flask

app = Flask(__name__)

def getConnection():
    return pymysql.connect(
        host='localhost',
        #CREATEUSERで作ったやつ
        user='app', #mysqlのユーザー名
        password='app', #mysqlのパスワード
        database='vantan', #mysqlに作ったデータベースからどれか選択する
        cursorclass=pymysql.cursors.DictCursor)

@ app.route('/')
def hello():
     return "<h1>Hello Flask</h1>\n"

@ app.route('/users')
def users():
    connection = getConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `users`" #データベース内のテーブルを選択
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')