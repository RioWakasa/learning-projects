import tkinter

# #7-3チェックボタンを配置する
# #チェックボタンの配置
# root = tkinter.Tk()
# root.title('チェックボタンを扱う')
# root.geometry('400x200')
# cbtn = tkinter.Checkbutton(text='チェックボタン') #チェックボタンの部品を作る
# cbtn.pack()
# root.mainloop()

# #チェックの有無を知る
# root = tkinter.Tk()
# root.title('最初からチェックされた状態にする')
# root.geometry('400x200')
# cval = tkinter.BooleanVar() #BooleanVar()のオブジェクトを用意
# cval.set(True) #それにTrueをセットする Trueでチェックあり
# cbtn = tkinter.Checkbutton(text='チェックボタン', variable=cval)
# #variable=でBoolearnVar()のオブジェクトとチェックボックスが結びつく
# cbtn.pack()
# root.mainloop()

def check():
  if cval.get() == True:
    print('チェックされています')
  else:
    print('チェックされていません')

root = tkinter.Tk()
root.title('最初からチェックの状態を知る')
root.geometry('400x200')
cval = tkinter.BooleanVar()
cval.set(False)
cbtn = tkinter.Checkbutton(text='チェックボタン', variable=cval, command=check)
cbtn.pack()
root.mainloop()