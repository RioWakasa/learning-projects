# for i in range(10, 0, -2): #iの初めは10で、０より大きい間,2ずつ減らしていく
#   print(i)

# import calendar
# print(calendar.month(2022,9))

# print(calendar.prcal(2022))
# print(calendar.isleap(2020)) #2020年が閏年か出力

import datetime
from random import random
print(datetime.date.today()) #現在の日付を出力
print(datetime.datetime.now()) #現在の日付と時刻を出力

d = datetime.datetime.now() #変数dに現在の日時を入れる

print(d.hour) #時
print(d.minute) #分
print(d.second)#秒

today = datetime.date.today() #変数todayに実行時の年月日を代入
birth = datetime.date(1998,11,10) #変数birthに誕生日の年月日を代入
print(today-birth) #2つの日付のデータの引き算で経過日数を求め出力

#1%の確率でレアキャラが出る
import random
cnt = 0 #乱数を発生させた回数を数える変数
while True:
  r = random.randint(1,100) #1以上100以下の乱数をrに代入
  print(r) #rの値を出力
  cnt += 1 #乱数を発生させた回数をカウント
  if r == 77: #77という乱数(レアキャラ)が出たら
    break #繰り返しを中断
print(f'{cnt}回目でレアキャラをゲット') #何回目でレアキャラが出たかを出力