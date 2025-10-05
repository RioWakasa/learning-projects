import tkinter

#9-3ゲーム用のカーソルの表示
#ゲーム画面のサイズを設計する
cursor_x = 0 #カーソルの横方向の位置(左から何マス目にあるか)
cursor_y = 0 #カーソルの縦方向の位置(上から何マス目にあるか)
mouse_x = 0 #マウスポインタのx座標
mouse_y = 0 #マウスポインタのy座標

def mouse_move(e):
  global mouse_x, mouse_y
  mouse_x = e.x
  mouse_y = e.y

def game_main():
  global cursor_x,cursor_y
  #マウスポインタの座標が盤面上であれば
  if 24 <= mouse_x and mouse_x < 24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10:
    cursor_x = int((mouse_x-24)/72) #ポインタのx座標からカーソルの横の位置を計算
    cursor_y = int((mouse_y-24)/72) #ポインタのy座標からカーソルの横の位置を計算
  cvs.delete('CURSOR')
  cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag='CURSOR') #新たな位置にカーソルを表示する
  root.after(100, game_main)

root = tkinter.Tk()
root.title('カーソルの表示')
root.resizable(False,False)
root.bind('<Motion>', mouse_move)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file='./py_samples/Chapter9/neko_bg.png')
cursor = tkinter.PhotoImage(file='./py_samples/Chapter9/neko_cursor.png')
cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()