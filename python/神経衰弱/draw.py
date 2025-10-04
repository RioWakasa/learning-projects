import tkinter as tk

class Draw:
    def draw_txt(self, txt, x, y, siz, col, tg):
      fnt = ('Times New Roman', siz, 'bold')
      self.cvs.create_text(x+2, y+2, text=txt, fill=col, font=fnt, tag=tg)