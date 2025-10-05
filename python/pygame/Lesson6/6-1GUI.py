#6-1GUIについて
import tkinter
import tkinter.font

#ウィンドウを表示する
#root = tkinter.Tk() #ウィンドウの部品(オブジェクト)を作る

#タイトルとサイズを指定する
root = tkinter.Tk() #ウィンドウの部品(オブジェクト)を作る
root.title('初めてのウィンドウ') #ウィンドウのタイトルを指定
root.geometry('800x600') #ウィンドウのサイズを指定(width800xheight600) 
#ウィンドウのサイズはgeometry()の他に minsize(幅, 高さ) maxsize(幅, 高さ) で最小サイズ、最大サイズを指定できる

#6-2ラベルの配置
label = tkinter.Label(root, text='ラベルの文字列', font=('system', 24)) #ラベルの部品を作る
#変数名 = tkinter.Label(ウィンドウのオブジェクト, text='ラベルの文字列', font('フォント名', フォントサイズ)
label.place(x=200, y=100) #ウィンドウにラベルを配置
#label.place(x=x座標, y=y座標)

#使えるフォントを調べる
print(tkinter.font.families())

root.mainloop() #ウィンドウを表示