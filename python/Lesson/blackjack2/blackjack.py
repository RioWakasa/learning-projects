from prebj import Bj
from game_func import Func

class Game:
  game_num = 0
  count = 0
  p_num = 0
  next = 'y'

  name = list()
  players = list()
  split = list()

  bj = Bj
  func = Func()

  def game_main(self):
    self.p_num = self.func.input_text.range_check('何人でプレイしますか?', 1, 4)
    self.name = self.func.input_text.name_input('あなたの名前を入力してください', self.p_num, self.name)
    self.bj.player_make(self.p_num, self.name, self.players)
    while True:
      self.bj.chip.bet_coin(self.players, self.func)
      print('=========================\n')
      self.func.card.first_draw(self.bj, self.players)
      self.func.show_card(self.bj, self.players)
      print('=========================\n')
      self.func.hit_stand()
      print('=========================\n')
      self.func.dealer_deal()
      print('\n=========================\n')
      self.func.judgement()
      self.count = self.func.next_game()
      if self.game_num == 5 or self.count == self.p_num:
        print('No more bet')
      else:
        self.next = self.func.input_text.yes_no('continue? (y or n)')
        print()
      if self.next == 'n' or self.game_num == 5 or self.count == self.p_num:
        for i in self.players:
          print(f'{i.name}さんの所持コイン{i.coin}枚')
          break

game = Game()
game.game_main()