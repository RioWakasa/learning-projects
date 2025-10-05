import tkinter

def transition_button(widget):
    widget.place_forget() # canvas(widget)を隠す                          
    canvas2 = tkinter.Canvas(background="#eca", width=400, height=400)
    canvas2.place(x=0, y=0)
    label2 = tkinter.Label(canvas2, text="遷移後の画面です。")
    label2.place(x=200, y=150, anchor=tkinter.CENTER)
    print("clicked")

# ウィンドウの作成                                                              
window = tkinter.Tk()
window.geometry("400x400")
window.title("Screen Transition")

# 遷移前の画面の作成                                                            
canvas1 = tkinter.Canvas(background="#cea", width=400, height=400)
canvas1.place(x=0, y=0) # キャンバス                                            
label1 = tkinter.Label(canvas1, text="遷移する前の画面です。") # テキスト       
label1.place(x=200, y=150, anchor=tkinter.CENTER)
button = tkinter.Button(canvas1, text="遷移するボタン", command=lambda:transition_button(canvas1)) # 遷移ボタン                                                
button.place(x=200, y=250, anchor=tkinter.CENTER)

window.mainloop()