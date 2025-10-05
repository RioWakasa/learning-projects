from player_hand import Tehuda

class Player(Tehuda):
  def __init__(self, name):
    self.name = name
    self.coin = 0
    self.bet = 0
    self.hand = Tehuda()
    self.Flag = True