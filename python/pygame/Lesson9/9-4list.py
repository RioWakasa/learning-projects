import tkinter

#9-4マス上のデータを管理する
#二次元リストで管理する

#マス目を管理する二次元リスト
neko = [
  [1, 0, 0, 0, 0, 0, 7, 7],
  [0, 2, 0, 0, 0, 0, 7, 7],
  [0, 0, 3, 0, 0, 0, 0, 0],
  [0, 0, 0, 4, 0, 0, 0, 0],
  [0, 0, 0, 0, 5, 0, 0, 0],
  [0, 0, 0, 0, 0, 6, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 2, 3, 4, 5, 6]
]

#ネコを表示する関数
def draw_neko():
  for y in range(10):
    for x in range(8):
      if neko[y][x] > 0:
        cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]])

root = tkinter.Tk()
root.title('二次元リストでマスを管理する')
root.resizable(False,False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file='./py_samples/Chapter9/neko_bg.png')
img_neko = [
  None, #img_neko[0]は何もない値とする
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko1.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko2.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko3.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko4.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko5.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko6.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter9/neko_niku.png')
]

cvs.create_image(456, 384, image=bg) #キャンバス上に背景を描く
draw_neko()
root.mainloop()