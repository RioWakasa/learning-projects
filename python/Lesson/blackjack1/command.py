class Command:
  def title_click(self):
    self.cvs.delete('TITLE')
    self.btn.destroy()
    self.index = 1
  
  def game_click(self):
    self.btn.destroy()