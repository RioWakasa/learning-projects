import tkinter

#デジタルフォトフレームを作る
pnum = 0
def photograph():
  global pnum
  canvas.delete('PH') #画像の削除
  canvas.create_image(400, 300, image=photo[pnum], tag='PH') #画像の表示
  pnum += 1
  if pnum >= len(photo): #最後の画像まで行ったら
    pnum=0 #最初の画像に戻す
  root.after(1000, photograph)

root = tkinter.Tk()
root.title('デジタルフォトフレーム')
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()
#リストで画像を配置
photo = [
  tkinter.PhotoImage(file='./py_samples/Chapter8/cat00.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter8/cat01.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter8/cat02.png'),
  tkinter.PhotoImage(file='./py_samples/Chapter8/cat03.png')
  ]
photograph()
root.mainloop()