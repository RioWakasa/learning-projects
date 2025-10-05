import tkinter

#リアルタイムにキャラクターを動かす
key = ''
#キーを押したときに実行する関数の宣言
def key_down(e):
  global key
  key = e.keysym #押されたキーの名称をkeyに代入
#キーを離した時に実行する関数の宣言
def key_up(e):
  global key
  key = ''

cx = 400 #キャラクターのx座標を定義する変数
cy = 300 #キャラクターのy座標を管理する変数
def main_proc():
  global cx, cy
  if key == 'Up':
    cy -= 20
  if key == 'Down':
    cy += 20
  if key == 'Left':
    cx -= 20
  if key == 'Right':
    cx += 20
  canvas.coords('MYCHR', cx, cy) #キャラクター画像を新しい位置に移動する
  #tag=タグ名 キャンバスに描画する図形や画像につけることができ、動かしたり消したりする時に用いる
  root.after(100, main_proc) #after命令で0.1秒後に実行する関数を指定

root = tkinter.Tk()
root.title('キャラクターの移動')
root.bind('<KeyPress>',key_down) #bind()命令でキーを押した時に実行する関数を指定
root.bind('<KeyRelease>',key_up) #bind()命令でキーを離した時に実行する関数を指定
canvas = tkinter.Canvas(width=800, height=600, bg='lightgreen')
canvas.pack()
img = tkinter.PhotoImage(file='./py_samples/Chapter8/mimi.png')
canvas.create_image(cx,cy,image=img,tag='MYCHR')
main_proc()
root.mainloop()