class Trump:
  digit = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10, 'J':11, 'Q':12, 'K':13}
  suit = ['♢', '♡', '♧', '♤'] #フィールド
  card = [i + j for i in suit for j in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']] #フィールド

  def shuffle(self): #関数
    import random
    random.shuffle(self.card) #シャッフル

  def deal(self):
    draw = self.card[0] #山札の1番上のカードを1枚引く
    self.card.pop(0) #山札の1番上のカードを消す
    return draw

  def num(self, n):
    digit = self.digit[n[-1]]
    return digit