# #5-2クイズゲーム
# #文字列をif文で判定する
# print('サザエさんの旦那さんの名前は？')
# ans = input()
# if ans in ['マスオ', 'ますお']:
#   print('正解です')
# else:
#   print('不正解です')

#問題数を増やす
QUESTION = [
'サザエさんの旦那さんの名前は？',
'カツオの妹の名前は？',
'タラちゃんはカツオから見てどんな関係？'] #定数は大文字で記述
R_ANS = [['マスオ','ますお'],['ワカメ','わかめ'],['甥','おい']]

for i in range(3):
  print(QUESTION[i])
  ans = input()
  if ans in R_ANS[i]:
    print('正解です')
  else:
    print('不正解です')