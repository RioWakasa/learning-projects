import random
import datetime

# #5-4Step1 虫喰いアルファベットを作る
# ALP = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# r = random.choice(ALP)
# alp = ""
# for i in ALP:
#   if i != r:
#     alp = alp + i
# print(alp)

# #答えを入力し判定する
# ans = input('抜けているアルファベットは？')
# if ans == r:
#   print('正解です')
# else:
#   print('違います')

# #時間の計測を加える
# st = datetime.datetime.now() #開始日時を変数stに入れる
# ans = input('抜けているアルファベットは？')
# if ans == r:
#   print('正解です')
#   et = datetime.datetime.now() #終了日時を変数etに入れる
#   print((et - st).seconds) #etとstの差を秒数にして出力
# else:
#   print('違います')

ALP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
r = random.choice(ALP)
alp = ""
for i in ALP:
  if i != r:
    alp = alp + i
print(alp)

st = datetime.datetime.now() #開始日時を変数stに入れる
ans = input('抜けているアルファベットは？')
if ans == r:
  print('正解です')
  et = datetime.datetime.now() #終了日時を変数etに入れる
  print(f'{(et - st).seconds}秒かかりました') #etとstの差を秒数にして出力
else:
  print('違います')