class Split:
  def split_hand(self, player):
    if player.coin >= player.bet:
      print(f'{player.name}: SPLIT CHANCE')
      print('splitは倍のベット数をかけることで手札を2つにすることができます\nそれぞれの手札に同じベット数がかかっている状態になります')
      split = self.input_text.yes_no(f'{player.tehuda.hand}をsplitしますか? (y or n)')
      if split == 'y':
        for i in range(2):
          self.draw(player)
        player.tehuda.hand = [[player.tehuda.hand[0],player.tehuda.hand[2]], [player.tehuda.hand[1], player.tehuda.hand[3]]]
        player.tehuda.number = [[player.tehuda.number[0],player.tehuda.number[2]], [player.tehuda.number[1], player.tehuda.number[3]]]
        print(f'{player.name}の手札: {player.tehuda.hand}')
        self.split.append(player.name)
      else:
        print('splitしませんでした')
      return split

  def split_hands(self, player, num):
    if player.coin >= player.bet:
      print(f'{player.name}: SPLIT CHANCE')
      split = self.input_text.yes_no(f'{player.tehuda.hand[num]}をsplitしますか? (y or n)')
      if split == 'y':
        for i in range(2):
          self.draw(player)
        player.tehuda.hand = [[player.tehuda.hand[0],player.tehuda.hand[2]], [player.tehuda.hand[1], player.tehuda.hand[3]]]
        player.tehuda.number = [[player.tehuda.number[0],player.tehuda.number[2]], [player.tehuda.number[1], player.tehuda.number[3]]]
        print(f'{player.name}の手札: {player.tehuda.hand}')
        self.split.append(player.name)
      else:
        print('splitしませんでした')
      return split
