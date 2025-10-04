class MouseMotion:
  def mouse_move(self, x, y, e):
    x = e.x
    y = e.y

  def mouse_press(self, c, e):
    c = True
    return c

  def mouse_release(self, c, e):
    c = False
    return c

  def mouse_check(self, x, y, c):
    fnt = ('Times New Roman', 30)
    txt = f'mouse({x},{y}){c}'
    self.cvs.delete('TEST')
    self.cvs.create_text(456, 384, text=txt, fill='black', font=fnt, tag='TEST')
    self.root.after(100, self.mouse_check)