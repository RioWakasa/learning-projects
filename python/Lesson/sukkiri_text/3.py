scores = [80, 100, 20,60]
if 100 in scores:
  print('100がある')

num = 75

if not (num < 60 or num > 100): #60以上100以下
  pass

initial = 'K'
if initial == 'K':
  print('出たよ')

point = 80

if point < 256 and point >= 80:
  print('OK')

bmi = 18

if bmi < 20 or bmi > 25:
  print('不健康')

year = 2100

if (year % 4) == 0:
  if (year % 100 == 0 and year % 400 != 0):
    print('平年')
  else:
    print('閏年')

day = 27

if not (day in [28,30,31]):
  print('OK')

isError = False
n = 90

if isError == False and n < 100:
  print('画面表示')

m = 50

if m % 2 == 0:
  print('偶数')
else:
  print('奇数')

s = input()

if s == 'こんにちは':
  print('こんにちワン')
elif s == 'ありがとう':
  print('ありがとうさぎ')
elif s == 'こんばんは':
  print('こんばんわに')
elif s == 'さようなら':
  print('さよなライオン')
else:
  print('どうしました？')