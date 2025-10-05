from trump import Trump
from player import Player
from chip import Chip

class Bj:
  dealer = Player('dealer')
  chip = Chip()
  trump = Trump()

  def __init__(self):
    self.trump_make()
    
  def trump_make(self):
    self.trump = Trump()
    self.trump.shuffle()

  def player_make(self, name, players):
    for i in range(len(name)):
      name[i] = Player(name[i])
      players.append(name[i])
      name[i].coin += 1000