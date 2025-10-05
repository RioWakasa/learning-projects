import tkinter

def click(event):
    global figure
    global before_x, before_y

    x = event.x
    y = event.y

    # クリックされた位置に一番近い図形のID取得
    figure = canvas.find_closest(x, y)

    # マウスの座標を記憶
    before_x = x
    before_y = y

def drag(event):
    global before_x, before_y

    x = event.x
    y = event.y

    # 前回からのマウスの移動量の分だけ図形も移動
    canvas.move(
        figure,
        x - before_x, y - before_y
    )

    # マウスの座標を記憶
    before_x = x
    before_y = y

def main():
    global canvas

    app = tkinter.Tk()

    # キャンバス作成
    canvas = tkinter.Canvas(
        app,
        width=500, height=300,
        highlightthickness=0,
        bg="white"
    )
    canvas.grid(row=0, column=0)


    # 色を用意
    colors = (
        "red", "green", "yellow", "blue", "purple", "pink", "orange"
    )

    # 色の数だけ適当に位置をずらしながら長方形（正方形）を描画
    for i, color in enumerate(colors):
        rect = canvas.create_rectangle(
            i * 60 + 20, 20, i * 60 + 70, 70,
            fill=color,
        )

        # 描画した図形にイベント処理設定
        canvas.tag_bind(rect, "<ButtonPress-1>", click)
        canvas.tag_bind(rect, "<Button1-Motion>", drag)

    app.mainloop()

if __name__ == "__main__":
    main()