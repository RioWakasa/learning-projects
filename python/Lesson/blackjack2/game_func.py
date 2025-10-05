from input_text import Input
from card_func import Card

class Func:
  input_text = Input()
  card = Card()

  def show_card(self, bj, players):
    print(f'ディーラー: {bj.dealer.tehuda.hand[0]}\n合計: {bj.dealer.tehuda.number[0]}\n')
    for i in players:
      if i.Flag:
        sum_hand = self.card.sum_card(i)
        # while True:
        #   Flag = 0
        #   if not (i.name in self.split) and i.tehuda.number[0] == i.tehuda.number[1]:
        #     Flag = self.split_hand(i)
        #   elif i.name in self.split:
        #     for j in range(len(i.tehuda.hand)):
        #       if i.tehuda.number[j][0] == i.tehuda.number[j][1]:
        #         Flag = self.split_hands(i, j)
          # if Flag != 'y':
          #   break
        if sum_hand == 21:
          print('Black Jack!!\n')
          i.Flag = 'BJ'
          i.coin += int(i.bet*1.5)
        else:
          print()

  def dealer_deal(self, players, bj):
    count = 0
    for i in players:
      if i.Flag == True:
        count += 1
    if count >= 1:
      sum_hand = self.card.sum_card(bj.dealer)
    if sum_hand <= 16:
      while sum_hand <= 16:
        self.card.draw(bj.dealer)
        sum_hand = self.card.sum_card(bj.dealer)
    if sum_hand > 21:
      bj.dealer.Flag = False

  def hit_stand(self, players):
    for i in players:
      count = 0
      if i.Flag == True:
        while True:
          self.card.sum_card(i)
          if count == 0:
            h_s = input(f'{i.name}: hit or stand or double? (h or s or d)')
          else:
            h_s = input(f'{i.name}: hit or stand? (h or s)')
          if h_s == 'h':
            self.card.draw(i)
            sum_hand = self.card.sum_card(i)
            count += 1
            if sum_hand > 21:
              print('BUST\n')
              i.Flag = False
              break
            elif sum_hand == 21:
              print()
              break
          elif h_s == 's':
              print()
              break
          elif h_s == 'd':
              i.coin -= i.bet
              i.bet = i.bet * 2
              self.card.draw(i)
              sum_hand = self.card.sum_card(i)
              count += 1
              if sum_hand > 21:
                print('BUST\n')
                i.Flag = False
              else:
                print()
              break
          else:
            print('入力が違います')
      elif i.Flag == 'BJ':
        print(f'{i.name}: Black Jack!\n')

  def judgement(self, bj, players):
    for i in players:
      if i.Flag == True:
        if bj.dealer.Flag:
          sum_hand = sum(i.tehuda.number)
          dealer_hand = sum(bj.dealer.tehuda.number)
          if sum_hand > dealer_hand:
            print(f'{i.name}: WIN')
            i.coin += i.bet * 2
          elif sum_hand < dealer_hand:
            print(f'{i.name}: LOSE')
          else:
            print(f'{i.name}: DRAW')
            i.coin += i.bet
        else:
          print(f'{i.name}: WIN')
          i.coin += i.bet
      elif i.Flag == 'BJ':
        print(f'{i.name}: Black Jack!')
      elif i.Flag == False and i.bet >= 100:
        print(f'{i.name}: LOSE')

  def next_game(self, bj, players, count):
    bj.dealer.Flag == True
    bj.dealer.tehuda.trump_make()
    for i in players:
      print(f'{i.name}の所持コイン: {i.coin}枚')
      if i.coin >= 100:
        i.Flag = True
        i.tehuda.__init__()
        print()
      else:
        i.Flag = False
        count += 1
      if i.Flag == False and i.bet > 0:
        print('所持コインが足りません\n')
        i.bet = 0
    return count