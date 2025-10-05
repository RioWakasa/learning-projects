import tkinter

# #6-3ボタンの配置
# root = tkinter.Tk()
# root.title('初めてのボタン')
# root.geometry('800x600')
# button = tkinter.Button(root, text='ボタンの文字列', font=('Times New Roman',24)) #ボタンの部品を作る
# button.place(x=200, y=100) #ウィンドウにボタンを配置
# #変数名.place(x=x座標, y=y座標)
# root.mainloop()

#ボタンをクリックした時の反応
def click_btn():
  button['text'] = 'クリックしました' #ボタンの文字列を変更

root = tkinter.Tk()
root.title('初めてのボタン')
root.geometry('800x600')
button = tkinter.Button(root, text='クリックしてください', font=('Times New Roman',24), command=click_btn)
#変数名 = tkinter.Button(ウィンドウのオブジェクト, text='ボタンの文字列', font('フォント名', フォントサイズ), command=でクリックした時に働く関数を指定
button.place(x=200, y=100) #ウィンドウにボタンを配置
#変数名.place(x=x座標, y=y座標)
root.mainloop()