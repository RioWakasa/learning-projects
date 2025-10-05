class Chip:
  def bet_coin(self, players, func):
    print('100枚からbet可能です\n')
    for i in players:
      if i.Flag:
        print(f'{i.name}の所持コインは{i.coin}枚です')
        bet = func.input_text.range_check(f'{i.name} Place your bet >>', 100, i.coin)
        i.bet = bet
        i.coin -= bet
        print(f'{i.name}は{i.bet}枚ベットしました\n')