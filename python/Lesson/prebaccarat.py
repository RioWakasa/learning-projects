from trump import Trump
from hand import Tehuda

class Baccarat:
  #インスタンス化
  trump = Trump()
  player = Tehuda()
  banker = Tehuda()
  #プレイヤーとバンカーの手札の合計の一桁目
  player_score = 0
  banker_score = 0
  #ベットする人
  bet_person = []