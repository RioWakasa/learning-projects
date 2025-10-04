import random

class Trump:
  digit = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10, 'J':11, 'Q':12, 'K':13}
  suit = ['spade', 'club', 'dia', 'heart']
  cards = [i + j for i in suit for j in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]

  def shuffle(self):
    random.shuffle(self.cards)

  def deal_card(self):
    deal = self.cards[0]
    self.cards.pop(0)
    return deal

  def num(self, n):
    disit = self.digit[n[-1]]
    return disit