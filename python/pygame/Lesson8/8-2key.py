import tkinter

#8-2キー入力を受け付ける
#bind()命令を使う
key = 0 #キーコードを入れる変数の宣言
def key_down(e):
  global key
  key = e.keycode #押されたキーのコードをkeyに代入
  print(f'KEY{key}') #シェルウィンドウにkeyの値を出力

root = tkinter.Tk()
root.title('キーコードを取得')
root.bind('<KeyPress>', key_down) #bind()命令でキーを押した時に実行する関数を指定
#bind('<イベント>', イベント発生時に実行する関数名)
#<KeyPress>あるいは<Key> キーを押した
#<KeyRelease> キーを離した
#<Motion> マウスポインタを動かした
#<ButtonPress>あるいは<Button> マウスボタンをクリックした
root.mainloop()