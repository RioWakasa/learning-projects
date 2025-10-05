import tkinter as tk
from trump import Trump
from player import Player

class Game:
  index = 0

  cursor_x = 0
  cursor_y = 0
  mouse_x = 0
  mouse_y = 0
  mouse_c = 0

  def __init__(self):
    self.trump = Trump()
    self.player = Player()
    self.root = tk.Tk()
    self.root.title('Black Jack')
    self.root.resizable(False, False)
    self.cvs = tk.Canvas(self.root, width=1300, height=760, bg='green')
    self.root.bind('<Motion>', self.mouse_move)
    self.root.bind('<ButtonPress>', self.mouse_press)
    self.root.bind('<ButtonRelease>', self.mouse_release)
    self.cvs.pack()
    self.btn = tk.Button(self.root, text='GAME START',font=('Times New Roman',25), padx=10, pady=20, bd=0, width=20,command=lambda : self.btn_click())
    self.btn.place(relx=0.383,rely=0.6)

  def btn_click(self):
    self.btn.destroy()

  def mouse_move(self, e):
    self.mouse_x = e.x
    self.mouse_y = e.y

  def mouse_press(self, e):
    self.mouse_c = True

  def mouse_release(self, e):
    self.mouse_c = False

  def mouse_check(self):
    fnt = ('Times New Roman', 30)
    txt = f'mouse({self.mouse_x},{self.mouse_y}){self.mouse_c}'
    self.cvs.delete('TEST')
    self.cvs.create_text(456, 384, text=txt, fill='black', font=fnt, tag='TEST')
    self.root.after(100, self.mouse_check)
  
  def deal_card(self):
    