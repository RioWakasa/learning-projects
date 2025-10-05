import tkinter

#8-4迷路のデータを定義する
#リストで迷路を定義する
root = tkinter.Tk()
root.title('迷路の表示')
canvas = tkinter.Canvas(width=800, height=560, bg='white')
canvas.pack()
#リストで迷路を定義
maze = [
  [1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,1,0,0,1],
  [1,0,1,1,0,0,1,0,0,1],
  [1,0,0,1,0,0,0,0,0,1],
  [1,0,0,1,1,1,1,1,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1]
]
for y in range(7):
  for x in range(10):
    if maze[y][x] == 1:
      canvas.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill='grey') #灰色の四角を描画する

root.mainloop()