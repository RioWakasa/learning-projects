import tkinter

# #7-1テキスト入力欄を配置する
# #1行のテキスト入力欄
# root = tkinter.Tk()
# root.title('初めてのテキスト入力欄')
# root.geometry('400x200')
# entry = tkinter.Entry(width=20) #半角20文字分の入力欄の部品を作る
# entry.place(x=10, y=10) #入力欄の部品を配置
# root.mainloop()

# #Entryの文字列の操作
# def click_btn():
#   txt = entry.get() #入力欄の文字列を変数txtに代入
#   button['text'] = txt #ボタンの文字列をtxtの値にする

# root = tkinter.Tk()
# root.title('初めてのテキスト入力欄')
# root.geometry('400x200')
# entry = tkinter.Entry(width=20)
# entry.place(x=20, y=20)
# button = tkinter.Button(text='文字列の取得', command=click_btn)
# button.place(x=20,y=100)
# root.mainloop()

#Entry内の文字列の削除 delete()

#7-2複数行のテキスト入力欄を配置する
#複数行のテキスト入力欄
def click_btn():
  text.insert(tkinter.END, 'モンスターが現れた！') #テキスト入力欄の最後尾に文字列を追加
  #文字列の挿入 insert()
  #tkinter.ENDとして入力欄の最後尾に追加

root = tkinter.Tk()
root.title('初めてのテキスト入力欄')
root.geometry('400x200')
button = tkinter.Button(text='メッセージ', command=click_btn)
button.pack()
text = tkinter.Text() #複数行のテキスト入力欄の部品を作る
text.pack()
#text.place(x=20,y=50,width=160,height=120)
#配置位置とサイズを指定
root.mainloop()

#get(最初の位置, 終わりの位置)
#入力欄全体の文字列取得 get('1.0','end-1c)
#'1.0'は1行目の0文字目 'end-1c'はendだけでは最後尾の次の位置になるので、そこから1文字(icharacter)手前
#delete(最初の位置, 終わりの位置)
#import tkinter.scrolledtext
#ScrolledText() スクロールバー付きのテキスト入力欄