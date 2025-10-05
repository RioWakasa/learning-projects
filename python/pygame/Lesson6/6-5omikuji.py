import tkinter
import random

# #6-5おみくじソフトを作る
# #Step1 画像の表示
# root = tkinter.Tk()
# root.title('おみくじソフト')
# root.resizable(False, False) #ウィンドウサイズを固定する 1つ目が横方向,2つ目が縦方向のサイズ変更を許可するかの指定
# canvas = tkinter.Canvas(root, width=800, height=600)
# canvas.pack()
# gazou = tkinter.PhotoImage(file='py_samples/Chapter6/miko.png')
# canvas.create_image(400, 300, image=gazou)
# root.mainloop()

# #Step2 GUIの配置
# root = tkinter.Tk()
# root.title('おみくじソフト')
# root.resizable(False, False)
# canvas = tkinter.Canvas(root, width=800, height=600)
# canvas.pack()
# gazou = tkinter.PhotoImage(file='py_samples/Chapter6/miko.png')
# canvas.create_image(400, 300, image=gazou)
# label = tkinter.Label(root, text='？？', font=('Times New Roman', 120), fg = 'black', bg='white')
#fg = foreground(文字の色) bg = background(背景色)
# label.place(x=380, y=60)
# button = tkinter.Button(root, text='おみくじを引く',font=('Times New Roman', 36), fg='skyblue')
# button.place(x=360, y=400)
# root.mainloop()

#Step3 ボタンを反応させる
def click_btn():
  label['text']=random.choice(['大吉', '中吉', '小吉', '凶'])
  label.update() #文字の更新を即座に行う

root = tkinter.Tk()
root.title('おみくじソフト')
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file='./py_samples/Chapter6/miko.png')
canvas.create_image(400, 300, image=gazou)
label = tkinter.Label(root, text='？？', font=('Times New Roman', 120), fg = 'black', bg='white')
label.place(x=380, y=60)
button = tkinter.Button(root, text='おみくじを引く',font=('Times New Roman', 36), command=click_btn, fg='skyblue')
button.place(x=360, y=400)
root.mainloop()