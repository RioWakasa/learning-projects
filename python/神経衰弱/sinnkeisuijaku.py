import tkinter as tk
import time
from trump import Trump
# from mouse import MouseMotion

class Game:
  index = 0
  count = 0
  turn = 0
  num = 0
  scores = [0, 0]

  before_x = 20
  before_y = 20
  check_x = list()
  check_y = list()
  cursor_x = 0
  cursor_y = 0
  mouse_x = 0
  mouse_y = 0
  mouse_c = False

  trump_back = list()
  trump_list = list()
  for i in range(4):
    trump_back.append([0,0,0,0,0,0,0,0,0,0,0,0,0])

  # mouse = MouseMotion()

  def btn_click(self):
    self.cvs.delete('TITLE')
    self.btn.destroy()
    self.index = 1

  def mouse_move(self, e):
    self.mouse_x = e.x
    self.mouse_y = e.y

  def mouse_press(self, e):
    self.mouse_c = True

  def mouse_release(self, e):
    self.mouse_c = False

  def __init__(self):
    self.trump = Trump()
    # self.mouse = MouseMotion()
    self.root = tk.Tk()
    self.root.title('神経衰弱')
    self.root.resizable(False, False)
    self.cvs = tk.Canvas(self.root, width=1300, height=760, bg='green')
    self.root.bind('<Motion>', self.mouse_move)
    self.root.bind('<ButtonPress>', self.mouse_press)
    self.root.bind('<ButtonRelease>', self.mouse_release)
    self.cvs.pack()
    self.btn = tk.Button(self.root, text='GAME START',font=('Times New Roman',25), padx=10, pady=20, bd=0, width=20,command=lambda : self.btn_click())
    self.btn.place(relx=0.383,rely=0.6)

    self.img_trump = {'back':tk.PhotoImage(file='trump_img/z01.png'),
    'spade':
    [tk.PhotoImage(file='trump_img/spadeA.png'),
    tk.PhotoImage(file='trump_img/spade2.png'),
    tk.PhotoImage(file='trump_img/spade3.png'),
    tk.PhotoImage(file='trump_img/spade4.png'),
    tk.PhotoImage(file='trump_img/spade5.png'),
    tk.PhotoImage(file='trump_img/spade6.png'),
    tk.PhotoImage(file='trump_img/spade7.png'),
    tk.PhotoImage(file='trump_img/spade8.png'),
    tk.PhotoImage(file='trump_img/spade9.png'),
    tk.PhotoImage(file='trump_img/spade10.png'),
    tk.PhotoImage(file='trump_img/spadeJ.png'),
    tk.PhotoImage(file='trump_img/spadeQ.png'),
    tk.PhotoImage(file='trump_img/spadeK.png')],
    'club':
    [tk.PhotoImage(file='trump_img/clubA.png'),
    tk.PhotoImage(file='trump_img/club2.png'),
    tk.PhotoImage(file='trump_img/club3.png'),
    tk.PhotoImage(file='trump_img/club4.png'),
    tk.PhotoImage(file='trump_img/club5.png'),
    tk.PhotoImage(file='trump_img/club6.png'),
    tk.PhotoImage(file='trump_img/club7.png'),
    tk.PhotoImage(file='trump_img/club8.png'),
    tk.PhotoImage(file='trump_img/club9.png'),
    tk.PhotoImage(file='trump_img/club10.png'),
    tk.PhotoImage(file='trump_img/clubJ.png'),
    tk.PhotoImage(file='trump_img/clubQ.png'),
    tk.PhotoImage(file='trump_img/clubK.png')],
    'dia':
    [tk.PhotoImage(file='trump_img/diaA.png'),
    tk.PhotoImage(file='trump_img/dia2.png'),
    tk.PhotoImage(file='trump_img/dia3.png'),
    tk.PhotoImage(file='trump_img/dia4.png'),
    tk.PhotoImage(file='trump_img/dia5.png'),
    tk.PhotoImage(file='trump_img/dia6.png'),
    tk.PhotoImage(file='trump_img/dia7.png'),
    tk.PhotoImage(file='trump_img/dia8.png'),
    tk.PhotoImage(file='trump_img/dia9.png'),
    tk.PhotoImage(file='trump_img/dia10.png'),
    tk.PhotoImage(file='trump_img/diaJ.png'),
    tk.PhotoImage(file='trump_img/diaQ.png'),
    tk.PhotoImage(file='trump_img/diaK.png')],
    'heart':
    [tk.PhotoImage(file='trump_img/heartA.png'),
    tk.PhotoImage(file='trump_img/heart2.png'),
    tk.PhotoImage(file='trump_img/heart3.png'),
    tk.PhotoImage(file='trump_img/heart4.png'),
    tk.PhotoImage(file='trump_img/heart5.png'),
    tk.PhotoImage(file='trump_img/heart6.png'),
    tk.PhotoImage(file='trump_img/heart7.png'),
    tk.PhotoImage(file='trump_img/heart8.png'),
    tk.PhotoImage(file='trump_img/heart9.png'),
    tk.PhotoImage(file='trump_img/heart10.png'),
    tk.PhotoImage(file='trump_img/heartJ.png'),
    tk.PhotoImage(file='trump_img/heartQ.png'),
    tk.PhotoImage(file='trump_img/heartK.png')],
    }
    self.trump.shuffle()
    for y in range(4):
      trump = list()
      for x in range(13):
        trump.append(self.trump.deal_card())
      self.trump_list.append(trump)

  def draw_card(self):
    self.cvs.delete('TRUMP')
    for y in range(4):
      for x in range(13):
        if self.trump_back[y][x] == 0:
          self.cvs.create_image(x*100+53, y*150+230, image=self.img_trump['back'], tag='TRUMP')
        elif self.trump_back[y][x] == 1:
          num = Trump.digit[self.trump_list[y][x][-1]]
          if 'spade' in self.trump_list[y][x]:
            self.cvs.create_image(x*100+53, y*150+230, image=self.img_trump['spade'][num-1], tag='TRUMP')
          elif 'club' in self.trump_list[y][x]:
            self.cvs.create_image(x*100+53, y*150+230, image=self.img_trump['club'][num-1], tag='TRUMP')
          elif 'dia' in self.trump_list[y][x]:
            self.cvs.create_image(x*100+53, y*150+230, image=self.img_trump['dia'][num-1], tag='TRUMP')
          elif 'heart' in self.trump_list[y][x]:
            self.cvs.create_image(x*100+53, y*150+230, image=self.img_trump['heart'][num-1], tag='TRUMP')
          # なんか画像表示されない
          # self.cvs.create_image(x*100+53, y*150+230, image=tk.PhotoImage(file='trump_img/z01.png'), tag='TRUMP')
          # self.path = f'tk.PhotoImage(file="trump_img/{}.png")'

  def draw_scores(self):
    self.cvs.delete('PLAYER')
    self.draw_txt('PLAYER1', 450, 40, 50, 'red', 'PLAYER')
    self.draw_txt('PLAYER2', 850, 40, 50, 'blue', 'PLAYER')
    self.draw_txt(self.scores[0], 450, 100, 50, 'black', 'PLAYER')
    self.draw_txt(self.scores[1], 850, 100, 50, 'black', 'PLAYER')

  def turn_change(self):
    time.sleep(1)
    self.draw_card()
    self.cvs.delete('TURN')
    if self.turn == 0:
      self.turn = 1
      self.draw_txt('PLAYER2のターン', 150, 40, 25, 'blue', 'TURN')
    else:
      self.turn = 0
      self.draw_txt('PLAYER1のターン', 150, 40, 25, 'red', 'TURN')

  def check(self, before_x, before_y):
    Flag = True
    if before_x == self.cursor_x and before_y == self.cursor_y:
      Flag = False
    else:
      for i in range(len(self.check_x)):
        if self.check_x[i] == self.cursor_x and self.check_y[i] == self.cursor_y:
          Flag = False
          return Flag
    return Flag

  def check_card(self):
    check = list()
    check_x = list()
    check_y = list()
    for y in range(4):
      for x in range(13):
        if self.trump_back[y][x] == 1:
          check.append(self.trump_list[y][x][-1])
          check_x.append(x)
          check_y.append(y)
    if check[0] == check[1]:
      self.trump_back[check_y[0]][check_x[0]], self.trump_back[check_y[1]][check_x[1]] = 2, 2
      for i in check_x:
        self.check_x.append(i)
      for i in check_y:
        self.check_y.append(i)
      self.count += 2
      self.scores[self.turn] += 1
      self.draw_scores()
    else:
      self.trump_back[check_y[0]][check_x[0]], self.trump_back[check_y[1]][check_x[1]] = 0, 0
      self.turn_change()

  def draw_txt(self, txt, x, y, siz, col, tg):
    fnt = ('Times New Roman', siz, 'bold')
    self.cvs.create_text(x+2, y+2, text=txt, fill=col, font=fnt, tag=tg)

  def game_main(self):
    #タイトル画面
    if self.index == 0:
      self.draw_txt('神経衰弱', 650, 250, 100, 'black', 'TITLE')
    #カードとスコアの表示
    elif self.index == 1:
      self.draw_card()
      self.draw_scores()
      self.draw_txt('PLAYER1のターン', 150, 40, 25, 'red', 'TURN')
      self.index = 2
    #引くカードを選ぶ
    elif self.index == 2:
      if self.num == 2:
        self.num = 0
      if 3 < self.mouse_x < 3+100*13 and 157 < 157+150*4:
        self.cursor_x = int((self.mouse_x-3)/100)
        self.cursor_y = int((self.mouse_y-157)/150)
        check = self.check(self.before_x, self.before_y)
        if check:
          if self.mouse_c == True:
            self.before_x = self.cursor_x
            self.before_y = self.cursor_y
            self.trump_back[self.cursor_y][self.cursor_x] = 1
            self.draw_card()
            self.num += 1
            if self.num == 2:
              self.index = 3
              self.num = 0
              self.before_x = 20
              self.before_y = 20
    #カードのチェック
    elif self.index == 3:
      self.check_card()
      if self.count == 52:
        self.index = 4
      else:
        self.index = 2
    #勝敗の表示
    elif self.index == 4:
      if self.scores[0] > self.scores[1]:
        self.draw_txt('PLAYER1の勝利', 650, 400, 100, 'red', 'WIN')
      elif self.scores[0] < self.scores[1]:
        self.draw_txt('PLAYER2の勝利', 650, 400, 100, 'blue', 'WIN')
      else:
        self.draw_txt('DRAW', 650, 400, 100, 'yellow', 'WIN')
    self.root.after(100, self.game_main)

game = Game()
game.game_main()
game.root.mainloop()