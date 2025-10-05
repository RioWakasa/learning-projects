import tkinter

#9-5ブロックを落下させるアルゴリズム
#リストの値を調べる

neko = [
  [1, 0, 0, 0, 0, 0, 1, 2],
  [0, 2, 0, 0, 0, 0, 3, 4],
  [0, 0, 3, 0, 0, 0, 0, 0],
  [0, 0, 0, 4, 0, 0, 0, 0],
  [0, 0, 0, 0, 5, 0, 0, 0],
  [0, 0, 0, 0, 0, 6, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 2, 3, 4, 5, 6]
]

def draw_neko():
  for y in range(10):
    for x in range(8):
      if neko[y][x] > 0:
        cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag='NEKO')

#ネコを落下させる関数
def drop_neko():
  for y in range(8, -1, -1): #yは8から0まで1ずつ増える
    for x in range(8): #xは0から7まで1ずつ増える
      #ネコのあるマスの下が空白なら
      if neko[y][x] != 0 and neko[y+1][x] == 0:
        neko[y+1][x] = neko[y][x] #空白にネコを入れ
        neko[y][x] = 0 #元のネコのマスは空白にする

def game_main():
  drop_neko() #ネコを落下させる関数を呼び出す
  cvs.delete('NEKO')
  draw_neko()
  root.after(100, game_main)

root = tkinter.Tk()
root.title('ネコを落下させる')
root.resizable(False,False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file='./py_samples/Chapter9/neko_bg.png')
img_neko = [
  None,
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko1.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko2.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko3.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko4.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko5.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko6.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko_niku.png')
]

cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()