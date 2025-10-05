import tkinter

#8-3キー入力で画像を動かす
#リアルタイムキー入力
#key = 0
key = '' #キーを入れる変数の定義
def key_down(e):
  global key
  #key = e.keycode
  key = e.keysym #押されたキーの名称をkeyに代入

def main_proc():
  label['text'] = key
  root.after(100, main_proc)

root = tkinter.Tk()
root.title('リアルタイムキー入力')
root.bind('<KeyPress>',key_down)
label = tkinter.Label(font=('Times New Roman', 80))
label.pack()
main_proc()
root.mainloop()