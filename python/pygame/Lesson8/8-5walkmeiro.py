import tkinter
import tkinter.messagebox

#8-5二次元画面のゲーム開発の基礎
#8-6ゲームとして完成させる
key = ''
def key_down(e):
  global key
  key = e.keysym

def key_up(e):
  global key
  key = ''

mx = 1 #キャラクターの横方向の位置を管理する変数
my = 1 #キャラクターの縦方向の位置を管理する変数
yuka = 0 #塗った床を数える変数
def main_proc():
  global mx, my, yuka
  if key == 'Shift_L' and yuka > 1: #左シフトキーを押しかつ2マス以上塗っていたら
    canvas.delete('PAINT') #塗った床を消す
    #キャラクターを初期位置に戻す
    mx = 1
    my = 1
    yuka = 0
    for y in range(7):
      for x in range(10):
        if maze[y][x] == 2: #塗った床があれば
          maze[y][x] = 0 #値を0にする
  if key == 'Up' and maze[my-1][mx] == 0: #方向キーの上が押されかつ上のマスが通路ならmyを1減らす
    my -= 1
  if key == 'Down' and maze[my+1][mx] == 0: #方向キーの下が押されかつ下のマスが通路ならmyを1増やす
    my += 1
  if key == 'Left' and maze[my][mx-1] == 0: #方向キーの左が押されかつ左のマスが通路ならmxを1減らす
    mx -= 1
  if key == 'Right' and maze[my][mx+1] == 0: #方向キーの右が押されかつ右のマスが通路ならmxを1増やす
    mx += 1
  if maze[my][mx] == 0:
    maze[my][mx] = 2 #リストの値を2にする
    yuka += 1
    canvas.create_rectangle(mx*80, my*80, mx*80+79, my*80+79, fill='pink', width=0, tag = 'PAINT') #ピンク色で塗る
    canvas.delete('MYCHR') #一旦キャラクターを消し、
    canvas.create_image(mx*80+40,my*80+40,image=img,tag='MYCHR') #再びキャラクターの画像を表示する
  #canvas.coords('MYCHR', mx*80+40, my*80+40) #指定した座標がキャラクターの中心になる
  if yuka == 30: #30箇所の床を塗ったら
    canvas.update() #キャンバスを更新
    tkinter.messagebox.showinfo('おめでとう！','すべての床を塗りました！') #クリアメッセージを表示
  else:
    root.after(100, main_proc)

root = tkinter.Tk()
root.title('迷路を塗るにゃん')
root.bind('<KeyPress>',key_down)
root.bind('<KeyRelease>',key_up)
canvas = tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

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
      canvas.create_rectangle(x*80, y*80, x*80+79, y*80+79, fill='skyblue', width=0)

img = tkinter.PhotoImage(file='./py_samples/Chapter8/mimi_s.png')
canvas.create_image(mx*80+40,my*80+40,image=img,tag='MYCHR')
main_proc()
root.mainloop()