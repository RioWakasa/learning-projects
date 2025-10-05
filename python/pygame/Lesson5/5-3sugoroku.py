# #5-3すごろくを作る
# #Step1 すごろくの盤面を表示する
# pl_pos = 6
# com_pos = 3
# def banmen():
#   print('・' * (pl_pos-1) + 'P' + '・' * (30-(pl_pos)) + 'Goal')
#   print('・' * (com_pos-1) + 'C' + '・' * (30-(com_pos)) + 'Goal')

# banmen()

# #Step2 繰り返しでコマを進める
# import random
# pl_pos = 1
# com_pos = 1
# def banmen():
#   print('・' * (pl_pos-1) + 'P' + '・' * (30-(pl_pos)) + 'Goal')
#   print('・' * (com_pos-1) + 'C' + '・' * (30-(com_pos)) + 'Goal')
# while True:
# 
#   input('Enterを押すと駒が進みます')
#   pl_pos += random.randint(1,6)
#   com_pos += random.randint(1,6)

#Step3 ゴールに到達したことを判定する
import random
pl_pos = 1
com_pos = 1
def banmen():
  print('・' * (pl_pos-1) + 'P' + '・' * (30-(pl_pos)) + 'Goal')
  print('・' * (com_pos-1) + 'C' + '・' * (30-(com_pos)) + 'Goal')

banmen()
print('スゴロク、スタート！')
while True:
  input('Enterを押すとコマが進みます')
  pl_pos += random.randint(1,6)
  if pl_pos > 30:
    pl_pos = 30
  banmen()
  if pl_pos == 30:
    print('あなたの勝ちです！')
    break
  input('Enterを押すとコンピュータのコマが進みます')
  com_pos += random.randint(1,6)
  if com_pos > 30:
    com_pos = 30
  banmen()
  if com_pos == 30:
    print('コンピュータの勝ちです')
    break