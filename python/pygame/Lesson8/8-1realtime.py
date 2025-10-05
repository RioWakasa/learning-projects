import tkinter

#8-1リアルタイム処理を実現する
#after()命令を使う
tmr = 0 #時間をカウントする変数tmrの定義
def count_up():
  global tmr #tmrをグローバル変数として扱うと宣言
  tmr += 1
  label['text'] = tmr #ラベルにtmrの値を表示
  root.after(1000, count_up) #1秒後に再びこの関数を実行する
  #after(1000ミリ秒,実行する関数)

root = tkinter.Tk()
label = tkinter.Label(font=('Times New Roman', 80))
label.pack()
root.after(1000, count_up) #1秒後に指定した関数を呼び出す
root.mainloop()