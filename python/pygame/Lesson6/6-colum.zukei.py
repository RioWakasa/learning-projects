import tkinter
root = tkinter.Tk()
root.title('キャンバスに図形を表示する')
root.geometry('500x400')
cvs = tkinter.Canvas(root, width=500, height=400, bg='white')
cvs.pack()
cvs.create_text(250, 25, text='文字列', fill='green', font=('Times New Roman', 24))
#直線
#create_line(x1,y1,x2,y2,fill='色',width=線の太さ) 
#3つ目の点、4つ目の点と複数の点を指定可能
#3点以上を指定しsmooth=Trueとすると曲線になる
cvs.create_line(30, 30, 70, 80, fill='navy', width=5)
cvs.create_line(120, 20, 80, 50, 200, 80, 140, 120, fill='blue', smooth=True)
#矩形
#create_rectangle(x1,y1,x2,y2,fill=塗り色,outline=枠線の色,width=枠線の太さ)
cvs.create_rectangle(40, 140, 160, 200, fill='lime')
cvs.create_rectangle(60, 240, 120, 360, fill='pink', outline='red',width=5)
#楕円
#create_oval(x1,y1,x2,y2,fill=塗り色,outline=枠線の色,width=枠線の太さ)
cvs.create_oval(250-40, 100-40, 250+40, 100+40, fill='silver', outline='purple')
cvs.create_oval(250-80, 200-40, 250+80, 200+40, fill='cyan', width=0)
#多角形
#create_polygon(x1,y1,x2,y2,x3,y3,...,fill=塗り色,outline=枠線の色,width=枠線の太さ)
#複数の点を指定可能
cvs.create_polygon(250, 250,150, 350, 350, 350, fill='magenta', width=0)
cvs.create_arc(400-50, 100-50, 400+50, 100+50, fill='yellow', start=30, extent=300)
cvs.create_arc(400-50, 250-50, 400+50, 250+50, fill='gold', start=0, extent=120, style=tkinter.CHORD)
cvs.create_arc(400-50, 350-50, 400+50, 350+50, fill='orange', start=0, extent=120, style=tkinter.ARC)
cvs.mainloop()