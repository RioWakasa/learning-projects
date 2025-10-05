import tkinter

#9-2申す入力を組み込む
#pythonのマウス入力
mouse_x = 0 #マウスポインタのx座標
mouse_y = 0 #マウスポインタのy座標
mouse_c = 0 #マウスボタンをクリックした時の変数(フラグ)

#マウスを動かした時に実行する処理
def mouse_move(e):
  global mouse_x, mouse_y
  mouse_x = e.x #mouse_xにマウスポインタのx座標を代入
  mouse_y = e.y #mouse_yにマウスポインタのy座標を代入

#マウスボタンを押した時に実行する処理
def mouse_press(e):
  global mouse_c
  mouse_c = 1

#マウスボタンを離した時に実行する処理
def mouse_release(e):
  global mouse_c
  mouse_c = 0

#リアルタイム処理を行う関数
def game_main():
  fnt = ('Times New Roman', 30)
  txt = f'mouse({mouse_x},{mouse_y}){mouse_c}'
  cvs.delete('TEST')
  cvs.create_text(456, 384, text=txt, fill='black', font=fnt, tag='TEST')
  root.after(100, game_main)

root = tkinter.Tk()
root.title('マウス入力')
root.resizable(False, False)
root.bind('<Motion>', mouse_move)
root.bind('<ButtonPress>', mouse_press)
root.bind('<ButtonRelease>', mouse_release)
cvs = tkinter.Canvas(root, width=912, height=756) #画面サイズオーバーしないようにDockありならheight756がmax
cvs.pack()
game_main()
root.mainloop()
