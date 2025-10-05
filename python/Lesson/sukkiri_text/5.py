# #見通しの悪いプログラム
# student_list = ['浅木', '松田']
# count = 0
# for student in student_list:
#   print('{}さんの結果を入力してください'.format(student))
#   network = int(input('ネットワークの得点? >>'))
#   database = int(input('データベースの得点? >>'))
#   security = int(input('セキュリティーの得点? >>'))
#   if student == '浅木':
#     asagi_scores = [network, database, security]
#     asagi_avg = sum(asagi_scores) / len(asagi_scores)
#   else:
#     matsuda_scores = [network, database, security]
#     matsuda_avg = sum(matsuda_scores) / len(matsuda_scores)
# print('浅木さんの平均点は{}です'.format(asagi_avg))
# print('松田さんの平均点は{}です'.format(matsuda_avg))

# """
# #見通しが良くなったプログラム
# #得点を入力
# asagi_scores = input('浅木')
# matsuda_scores = input('松田')
# #平均点を計算
# asagi_avg = calc_average(asagi_scores)
# matsuda_avg = calc_average(matsuda_scores)
# #結果を出力
# output_result('浅木', asagi_avg)
# output_result('松田', matsuda_avg)
# """

# #hello関数の定義(definition)
# def hello():
#   print('こんにちは。工藤です。') #インデント

# #hello関数の呼び出し(call)
# hello()

# """
# #シンプルな関数の定義
# def 関数名():
#   処理
# 処理はインデントして記述する
# """

# """
# #シンプルな関数の呼び出し
# 関数名()
# """

# #名前を表示するつもりのinput_scores関数
# def input_scores():
#   name = '' #空の変数nameを準備
#   print('{}の試験結果を入力してください'.format(name))

# #input_scores関数内の変数nameに代入するつもり
# name = '浅木' #input_scores関数内の変数nameに代入したつもり
# input_scores()
# name = '松田' #input_scores関数内の変数nameに代入したつもり
# input_scores()

# #引数を受け取るhello関数
# def hello(name): #呼び出し時に渡されるデータを受け取る変数
#   print('こんにちは。{}です。'.format(name))

# #引数を私ながらhello関数を呼び出す
# hello('浅木') #呼び出しと同時に'浅木'を渡す
# hello('松田') #呼び出しと同時に'松田'を渡す

# #複数の引数を受け取るprofile関数
# def profile(name, age, hobby):
#   print('私の名前は{}です。'.format(name))
#   print('年齢は{}歳です。'.format(age))
#   print('趣味は{}です。'.format(hobby))

# #複数の引数を渡しながらprofile関数を呼び出す
# profile('浅木',24,'カフェ巡り')

# """
# #引数を利用する関数の定義
# def 関数名(引数1,引数2,...):
#   処理
# #引数を利用する関数の呼び出し
# 関数名(引数1,引数2,...)
# """

# #リストの平均を求めるcalc_average関数
# def calc_average(scores): #リストを受け取る引数
#   avg = sum(scores) / len(scores) #受け取ったリストに格納されている得点の平均を求める
#   print('平均点は{}です'.format(avg))

# #input_scores関数とcalc_average関数
# def input_scores(name): #得点入力を担当する関数
#   print('{}さんの試験結果を入力してください'.format(name))
#   network = int(input('ネットワークの得点? >>'))
#   database = int('データベースの得点? >>')
#   security = int(input('セキュリティーの得点? >>'))
#   scores = [network, database, security] #入力された得点をローカル変数scoresにリストとして代入

# def calc_average(scores): #平均算出を担当する関数
#   avg = sum(scores) / len(scores) 
#   print('平均点は{}です'.format(avg))

# #input_scoresとcalc_averageを呼び出す
# input_scores('浅木')
# """
# calc_average(scores) #ここでエラーが発生
# """

# """
# #引数と戻り値を利用する関数の定義
# def 関数名():
#   処理
#   return 戻り値
# """

# #足し算の結果を返すplus関数
# def plus(x, y):
#   answer = x + y
#   return answer #ローカル変数answerの値を戻す

# #plus関数の呼び出し
# answer = plus(100, 50) #変数answerに戻り値が代入される
# print('足し算の答えは{}です'.format(answer))

# """
# #引数と戻り値を利用する関数の呼び出し
# 戻り値を受け取る変数名 = 関数名(引数1, 引数2, ...)
# """

# #さまざまな機能を担当する関数の定義
# def input_scores(name): #得点入力を担当する関数
#     print('{}さんの試験結果を入力してください'.format(name))
#     network = int(input('ネットワークの得点? >>'))
#     database = int(input('データベースの得点? >>'))
#     security = int(input('セキュリティーの得点? >>'))
#     scores = [network, database, security]
#     return scores

# def calc_average(scores): #平均算出を担当する関数
#     avg = sum(scores) / len(scores)
#     return avg

# def output_result(name, avg): #平均点の出力を担当する関数
#     print('{}さんの平均点は{}です'.format(name, avg))

# #試験結果を入力して平均点を出す
# #浅木と松田の得点入力
# asagi_scores = input_scores('浅木')
# matsuda_scores = input_scores('松田')
# #平均点を計算
# asagi_avg = calc_average(asagi_scores) #input_scores関数の戻り値を引数に渡す
# matsuda_avg = calc_average(matsuda_scores) #input_scores関数の戻り値を引数に渡す
# #結果を出力
# output_result('浅木', asagi_avg) #calc_average関数の戻り値を引数に渡す
# output_result('松田', matsuda_avg) #calc_average関数の戻り値を引数に渡す

# #2つの戻り値を返す?
# def plus_and_minus(a, b):
#   return a + b, a - b #和と差の2つの値が戻り値のように見える

# next, prev = plus_and_minus(1978, 1)

# #戻り値のタプルをアンパック代入
# def plus_and_minus(a, b):
#   return (a + b, a - b) #要素数2のタプルを1つ返しているだけ
# (next, prev) = plus_and_minus(1978, 1) #返ってきたタプルをアンパック代入しているだけ

# #指定された3食を表示するeat関数
# def eat(breakfast, lunch, dinner):
#   print('朝は{}を食べました'.format(breakfast))
#   print('昼は{}を食べました'.format(lunch))
#   print('夜は{}を食べました'.format(dinner))

# #松田くんの食生活を出力する
# print('8月1日')
# eat('トースト', 'おにぎり', 'カレー')
# print('8月2日')
# eat('納豆ごはん', 'ラーメン', 'カレー')
# print('8月3日')
# eat('バナナ', 'そば', '焼肉')
# print('8月4日')
# eat('サンドウィッチ', 'しゅうまい弁当', 'カレー')

# #引数にデフォルト値を指定する関数の定義
# def eat(breakfast, lunch, dinner='カレー'):
#   print('朝は{}を食べました'.format(breakfast))
#   print('昼は{}を食べました'.format(lunch))
#   print('夜は{}を食べました'.format(dinner))

# #指定された3食を表示するeat関数(デフォルト値を利用)
# def eat(breakfast, lunch, dinner='カレー'):
#   print('朝は{}を食べました'.format(breakfast))
#   print('昼は{}を食べました'.format(lunch))
#   print('夜は{}を食べました'.format(dinner))
  
# #松田くんの言うまでもない食生活を出力する
# print('8月1日')
# eat('トースト', 'おにぎり') #引数dinnerの実引数を省略
# print('8月2日')
# eat('納豆ごはん', 'ラーメン') #引数dinnerの実引数を省略
# print('8月3日')
# eat('バナナ', 'そば', '焼肉')
# print('8月4日')
# eat('サンドウィッチ', 'しゅうまい弁当') #引数dinnerの実引数を省略

# """
# def eat(breakfast='トースト', lunch, dinner):
# デフォルト引数が指定された仮引数より後ろにデフォルト引数がない仮引数を定義してはならない
# """

# #松田くんの基本的なeat関数
# def eat(breakfast, lunch='ラーメン', dinner='カレー'):
#   print('朝は{}を食べました'.format(breakfast))
#   print('昼は{}を食べました'.format(lunch))
#   print('夜は{}を食べました'.format(dinner))
  
# #夜がカレーじゃない日のeat関数の呼び出し
# eat('納豆ごはん', 'ラーメン', 'カレーうどん') #昼は基本ラーメンなので、本当は省略したいが...

# """
# #引数にキーワードを指定した関数呼び出し
# 関数名(仮引数名1=実引数名1, 仮引数名2=実引数名2,...)
# """

# #夜がカレーじゃない日のeat関数の呼び出し(キーワード指定)
# eat(breakfast='納豆ごはん', dinner='カレーうどん')
# eat(dinner='カレーうどん', breakfast='納豆ごはん') #順番は入れ替えてもよい
# eat('納豆ごはん', dinner='カレーうどん')

# #おやつも出力できるeat関数
# def eat(breakfast, lunch, dinner='カレー', desserts=()): #要素数0のタプルをデフォルト引数として指定
#   print('朝は{}を食べました'.format(breakfast))
#   print('昼は{}を食べました'.format(lunch))
#   print('夜は{}を食べました'.format(dinner))
#   for d in desserts:
#     print('おやつに{}を食べました'.format(d))

# #おやつも食べた日のeat関数の呼び出し
# eat('トースト', 'パスタ', 'カレー', ('アイス', 'チョコ', 'パフェ')) #おやつの部分は丸括弧で囲んでタプルにする

# """
# #可変長引数を利用した冠す定義
# def 関数名(仮引数1, 仮引数2,...,*仮引数名n):
# """

# #おやつも出力できるeat関数(可変勝引数を利用)
# def eat(breakfast, lunch, dinner='カレー', *desserts): #dessertsは可変長引数であることを表明
#   print('朝は{}を食べました'.format(breakfast))
#   print('昼は{}を食べました'.format(lunch))
#   print('夜は{}を食べました'.format(dinner))
#   for d in desserts:
#     print('おやつに{}を食べました'.format(d))

# #おやつも食べた日のeat関数の呼び出し(可変長引数を利用)
# eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'カレー') #後ろの3つがタプルとして仮引数dessetsに引き渡される

# #ディクショナリを用いた可変長引数
# def eat(**kwargs):
#   for key in kwargs: #for文にディクショナリ指定するとキーが順番に取り出される
#     print('{}に{}を食べました'.format(key,kwargs[key]))

# #引数を使わないで変数nameの値を受け渡している
# name = '松田'
# def hello():
#   print('こんにちは' + name + 'さん') #関数の外にある変数nameを使ってしまっている

# #hello関数の呼び出し
# hello()

# #グローバル変数に代入する?
# name = '松田'
# def change_name():
#   name = '浅木' #グローバル変数nameに代入しているつもり
#   def hello():
#     print('こんにちは' + name + 'さん')

# #関数の中からグローバル変数への代入を試みる
# change_name()
# hello()

# """
# #global文
# global 変数名
# """

# #global文を用いて黒オーバル変数に代入する
# name = '松田'
# def change_name():
#   global name #この関数における「name」はローカル変数ではなくグローバル変数を意味することを宣言
#   name = '浅木' #グローバル変数nameへ代入している
#   def hello():
#     print('こんにちは' + name + 'さん')

# def addition(num1, num2, kigou):
#   if kigou == '+':
#     answer = num1 + num2
#   elif kigou == '-':
#     answer = num1 - num2
#   elif kigou == 'x':
#     answer = num1 * num2
#   elif kigou == '/':
#     answer = num1 / num2
#   return answer

# answer = addition(30, 50, '-')
# print(answer)

# def daikei(a,b,c):
#   return (a+b)*c/2

# print(daikei(3,4,5))

# def weather():
#   print('今日は晴れです')

# weather()

# def calc_circle_area(r):
#   return r * r * 3.14

# print(calc_circle_area(2))

# import datetime
# def nowstr():
#   now = datetime.datetime.now()
#   return now.strftime('%H時%M分%S秒')

# print(nowstr())

# def nowint():
#   now = datetime.datetime.now()
#   h = now.hour
#   m = now.minute
#   s = now.second
#   return h,m,s

# print(nowint())

# def is_leapyear(year):
#   if year % 400 == 0:
#     print(f'西暦{year}年は閏年です')
#   if year % 4 == 0 and year % 100 != 0:
#     print(f'西暦{year}年は閏年ではありません')

# print(is_leapyear(2100))

def int_input(a):
  s = int(input(f'{a}を入力してください'))
  return s

def calc_payment(amount, people):
  dnum = amount / people
  pay = dnum // 100 * 100
  if dnum > pay:
    pay = int(pay + 100)
  payorg = amount - pay * (people - 1)
  return pay, payorg

def show_payment(pay, payorg, people):
  print('***支払額***')
  print(f'1人あたり{pay}円({people-1}人)、幹事は{payorg}円です')

amount = int_input('支払い総額')
people = int_input('参加人数')
pay, payorg = calc_payment(amount,people)
show_payment(pay, payorg, people)