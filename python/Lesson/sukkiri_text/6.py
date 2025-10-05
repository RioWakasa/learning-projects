#append関数やformat関数の呼び出し
tpl = '3人目は{}さん'
names = ['松田', '浅木']
names.append('工藤')
message = tpl.format(names[2]) #値.関数名()で呼び出す
print(message)

#整数もリストもデータと関数をセットで持つ
num = 10
print(num.bit_length())
names = ['松田', '浅木']
names.append('工藤')

"""
メソッドの呼び出し
オブジェクト.メソッド名(引数...)
"""

"""
capitalize() 先頭文字だけ大文字に、残りを小文字にする
lower() すべてを小文字にする
upper() すべてを大文字にする
title() 単語の先頭だけを大文字に、残りの全てを小文字にする
strip(○) 文字列○で区切り、各要素をリストで返す
replace(○,□) 文字列中の○の部分を□に置き換えた結果を返す
count(○) 文字列○が登場する回数を返す
"""

#strオブジェクトのメソッドを活用した血液型占い
userinfo = input('名前と血液型をカンマで区切って1行で入力')
[name, blood] = userinfo.split(',')
blood = blood.upper().strip()
print('{}さんは{}型なので大吉です'.format(name, blood))

"""
クラス名関数によるオブジェクト生成
関数名 = クラス名()
"""

#リテラルやクラス名関数を用いたオブジェクトの生成
int_value1 = 0 #intオブジェクト(中身のデータは0)を生成
int_value2 = int()
int_value3 = int(9) #intオブジェクト(中身のデータは9)を生成
int_value1 = [] #空のリストオブジェクトを生成
int_value2 = list()
int_value3 = list(('松田', '浅木')) #2つの要素を持つリストオブジェクトを生成

#RPGの勇者を表すクラスの定義と利用
class Hero: #データとしてnameとhp、関数としてsleepを持つオリジナル設計図Heroを定義
  name = '松田'
  hp = 100
  def sleep(self, hours):
    print('{}ha{}時間寝た!'.format(self.name, hours))
    self.hp += hours

#ゲーム開始
print('スッキリファンタジーⅫ 〜黄金の理想郷〜')
h = Hero() #HP100の勇者松田がオブジェクトとして誕生
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name, h.hp))

#オブジェクトのidentityの確認
scores1 = [80, 40, 50]
scores2 = [80, 40, 50]
print('scores1のidentity: {}'.format(id(scores1)))
print('scores2のidentity: {}'.format(id(scores2)))

if scores1 == scores2:
  print('scores1とscores2は同じ内容です')
else:
  print('scores1とscores2は違う内容です')

if id(scores1) == id(scores2):
  print('scores1とscores2は同じ存在です')
else:
  print('scores1とscores2は違う存在です')

#リストオブジェクトのコピーによる不可解な動作


#関数に渡すと変数の内容を書き換えられてしまう


#防御的コピーを用いて悪影響を防ぐ


#文字列を引き渡しても悪影響が起きない


#リストと文字列による書き換え時のidentity値の変化


#