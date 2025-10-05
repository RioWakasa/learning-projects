class Card:
  def draw(self, bj, pos):
    hand = bj.trump.deal()
    pos.tehuda.hand.append(hand)
    num = bj.trump.num(hand)
    num = bj.change_number(num, pos)
    pos.tehuda.number.append(num)

  def sum_card(self, pos):
    if not (pos.name in self.split):
      sum_hand = sum(pos.tehuda.number)
      print(f'{pos.name}\n手札: {pos.tehuda.hand}\n合計: {sum_hand}')
    else:
      sum_list = list()
      for i in len(pos.tehuda.hand):
        sum_list = sum(pos.tehuda[i])
      sum_hand = sum_list
    return sum_hand

  def first_draw(self, bj, players):
    for i in range(2):
      self.draw(bj, bj.dealer)
      for j in players:
        if j.Flag:
          self.draw(bj, j)

  def change_number(self, num, pos):
    if num > 10:
      num = 10
    if num == 1 and sum(pos.tehuda.number) <= 11:
      num = 11
    return num
