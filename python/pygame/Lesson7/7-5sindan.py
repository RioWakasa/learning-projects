import tkinter

# #7-5診断ゲームを作る
# #Step1 GUIの配置
# root = tkinter.Tk()
# root.title('ネコ度診断アプリ')
# root.resizable(False,False)
# canvas = tkinter.Canvas(root, width=800, height=600)
# canvas.pack()
# gazou = tkinter.PhotoImage(file='./py_samples/Chapter7/sumire.png')
# canvas.create_image(400, 300, image=gazou)
# button = tkinter.Button(text='診断する', font=('Times New Roman', 32), bg='lightgreen')
# button.place(x=400,y=480)
# text = tkinter.Text(width=40, height=5, font=('Times New Roman', 16))
# text.place(x=320,y=30)
# root.mainloop()

# #Step2 複数のチェックボタンの配置
# root = tkinter.Tk()
# root.title('ネコ度診断アプリ')
# root.resizable(False,False)
# canvas = tkinter.Canvas(root, width=800, height=600)
# canvas.pack()
# gazou = tkinter.PhotoImage(file='./py_samples/Chapter7/sumire.png')
# canvas.create_image(400, 300, image=gazou)
# button = tkinter.Button(text='診断する', font=('Times New Roman', 32), bg='lightgreen')
# button.place(x=400,y=480)
# text = tkinter.Text(width=40, height=5, font=('Times New Roman', 16))
# text.place(x=320,y=30)

# BooleanVarのオブジェクト用のリストチェックボタン用のリスト
# bvar = [None]*7
# cbtn = [None]*7
# #チェックボタンの質問を定義
# ITEM = [
# '高いところが好き',
# 'ボールを見ると転がしたくなる',
# 'びっくりすると髪の毛が逆立つ',
# 'ネズミの玩具が気になる',
# '匂いに敏感',
# '魚の骨をしゃぶりたくなる',
# '夜、元気になる'
# ]
# #繰り返しでチェックボタンを配置
# for i in range(7):
#   bvar[i] = tkinter.BooleanVar() #BooleanVarのオブジェクトを作る
#   bvar[i].set(False) #そのオブジェクトにFalseを配置
#   cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=('Times New Roman', 12), variable=bvar[i], bg='#dfe')
#   cbtn[i].place(x=400,y=160+40*i)
# root.mainloop()

#Step3 チェックされたボタンを教える

# #ボタンをクリックした時に働く関数の定義
# def click_btn():
#   pts = 0 #チェックしたボタンを数える変数
# #繰り返し命令でチェックされていたら変数の値を1増やす
#   for i in range(7):
#     if bvar[i].get() == True:
#       pts += 1
#   text.delete('1.0', tkinter.END) #入力欄の文字列を削除する
#   text.insert('1.0', 'チェックの数は' + str(pts)) #入力欄に変数の値を挿入

# root = tkinter.Tk()
# root.title('ネコ度診断アプリ')
# root.resizable(False,False)
# canvas = tkinter.Canvas(root, width=800, height=600)
# canvas.pack()
# gazou = tkinter.PhotoImage(file='./py_samples/Chapter7/sumire.png')
# canvas.create_image(400, 300, image=gazou)
# button = tkinter.Button(text='診断する', font=('Times New Roman', 32), bg='lightgreen', command=click_btn)
# button.place(x=400,y=480)
# text = tkinter.Text(width=40, height=5, font=('Times New Roman', 16), bg='white', fg='black')
# text.place(x=320,y=30)

# bvar = [None]*7
# cbtn = [None]*7
# ITEM = [
# '高いところが好き',
# 'ボールを見ると転がしたくなる',
# 'びっくりすると髪の毛が逆立つ',
# 'ネズミの玩具が気になる',
# '匂いに敏感',
# '魚の骨をしゃぶりたくなる',
# '夜、元気になる'
# ]
# for i in range(7):
#   bvar[i] = tkinter.BooleanVar()
#   bvar[i].set(False)
#   cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=('Times New Roman', 12), variable=bvar[i], bg='#dfe', fg='black')
#   cbtn[i].place(x=400,y=160+40*i)
# root.mainloop()

#Step4 コメントを入力する

#診断結果のコメントをリストで定義
KEKKA = [
  '前世がネコだった可能性は極めて低いです',
  'いたって普通の人間です',
  '特別おかしなところはありません',
  'やや、ネコっぽいところがあります',
  'ネコに近い性格のようです',
  'ネコにかなり近い性格です',
  '前世はネコだったかもしれません',
  '見た目は人間、中身はネコの可能性があります',
]

def click_btn():
  pts = 0
  for i in range(7):
    if bvar[i].get() == True:
      pts += 1
  nekodo = int(100*pts/7) #ネコ度を計算,小数部分は切り捨て
  text.delete('1.0', tkinter.END)
  text.insert('1.0', f'<診断結果>\nあなたのネコ度は{nekodo}%です。\n{KEKKA[pts]}') #入力に診断結果の文字列を挿入

root = tkinter.Tk()
root.title('ネコ度診断アプリ')
root.resizable(False,False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file='./py_samples/Chapter7/sumire.png')
canvas.create_image(400, 300, image=gazou)
button = tkinter.Button(text='診断する', font=('Times New Roman', 32), bg='lightgreen', command=click_btn)
button.place(x=400,y=480)
text = tkinter.Text(width=40, height=5, font=('Times New Roman', 16), bg='white', fg='black')
text.place(x=320,y=30)

bvar = [None]*7
cbtn = [None]*7
ITEM = [
'高いところが好き',
'ボールを見ると転がしたくなる',
'びっくりすると髪の毛が逆立つ',
'ネズミの玩具が気になる',
'匂いに敏感',
'魚の骨をしゃぶりたくなる',
'夜、元気になる'
]
for i in range(7):
  bvar[i] = tkinter.BooleanVar()
  bvar[i].set(False)
  cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=('Times New Roman', 12), variable=bvar[i], bg='#dfe', fg='black')
  cbtn[i].place(x=400,y=160+40*i)
root.mainloop()