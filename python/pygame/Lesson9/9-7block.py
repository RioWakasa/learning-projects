import tkinter
import random

#9-7ブロックが揃ったかを判定するアルゴリズム
#3つ並んだことを調べる

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
  global mouse_x, mouse_y
  mouse_x = e.x
  mouse_y = e.y

def mouse_press(e):
  global mouse_c
  mouse_c = 1

neko = []
for i in range(10):
  neko.append([0, 0, 0, 0, 0, 0, 0, 0])

def draw_neko():
  for y in range(10):
    for x in range(8):
      if neko[y][x] > 0:
        cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag='NEKO')

#ネコが3つ並んだか調べる関数
def yoko_neko():
  for y in range(10):
    for x in range(1, 7):
      #マスにネコが配置されていて
      if neko[y][x] > 0:
        #左右が同じネコなら
        if neko[y][x-1] == neko[y][x] and neko[y][x+1] == neko[y][x]:
          #それらのマスを肉球に変える
          neko[y][x-1] = 7
          neko[y][x] = 7
          neko[y][x+1] = 7

def game_main():
  global cursor_x, cursor_y, mouse_c
  #風船内の「テスト」という文字をクリックしたら
  if 640 <= mouse_x and mouse_x < 840 and 100 <= mouse_y and mouse_y < 160 and mouse_c == 1:
    mouse_c == 0 #クリックしたフラグを解除
    yoko_neko() #横に並んだか調べる関数を呼び出す
  if 24 <= mouse_x and mouse_x < 24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10:
    cursor_x = int((mouse_x-24)/72)
    cursor_y = int((mouse_y-24)/72)
    if mouse_c == 1:
      mouse_c = 0
      neko[cursor_y][cursor_x] = random.randint(1,2)
  cvs.delete('CURSOR')
  cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag='CURSOR')
  cvs.delete('NEKO')
  draw_neko()
  root.after(100, game_main)

root = tkinter.Tk()
root.title('横に3つ並んだか')
root.resizable(False,False)
root.bind('<Motion>', mouse_move)
root.bind('<ButtonPress>', mouse_press)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file='./py_samples/Chapter9/neko_bg.png')
cursor = tkinter.PhotoImage(file='./py_samples/Chapter9/neko_cursor.png')
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
cvs.create_rectangle(660, 100, 840, 160, fill='white') #風船内に枠を描き
cvs.create_text(750, 130, text='テスト', fill='red', font=('Times New Roman', 30)) #テストと表示する
game_main()
root.mainloop()