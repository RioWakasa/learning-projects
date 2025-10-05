import tkinter

# #6-4キャンバスの配置
# root = tkinter.Tk()
# root.title('初めてのキャンバス')
# canvas = tkinter.Canvas(root, width=400, height=600, bg='skyblue') #キャンバスの部品を作る
# #変数名 = tkonter.Canvas(ウィンドウのオブジェクト, width=幅, height=高さ, bg=背景色)
# canvas.pack() #ウィンドウにキャンバスを配置
# root.mainloop()

#キャンバスに画像を表示する
root = tkinter.Tk()
root.title('初めての画像表示')
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack() #ウィンドウにキャンバスを配置
gazou = tkinter.PhotoImage(file='py_samples/Chapter6/iroha.png') #gazouに画像ファイルを読み込む
canvas.create_image(200, 300, image=gazou) #キャンバスに画像を描画
#create_imge(x座標, y座標, image=画像を読み込んだ変数) x座標とy座標は画像の中心になる
root.mainloop()