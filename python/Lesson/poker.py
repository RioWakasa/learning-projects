from trump import Trump
from hand import Tehuda

#インスタンス化
trump = Trump()
dealer = Tehuda()
player = Tehuda()

#カードを引く
def draw(pd):
  h = trump.deal()
  n = trump.num(h)
  pd.hand.append(h)
  pd.number.append(n)

#最初の手札を配る(n枚)
def first_draw(n):
  for i in range(n):
    draw(player)
    draw(dealer)

#ゲーム開始時の処理
def game_start(n):
  trump.shuffle()
  first_draw(n)

hand = game_start(5)
print(player.hand,dealer.hand,player.number,dealer.number)
