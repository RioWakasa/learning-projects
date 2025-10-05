import tkinter

class App(tkinter.Tk):
  def __init__(self, *args, **kwargs):
    tkinter.Tk.__init__(self, *args, **kwargs)
    self.title('神経衰弱')
    self.geometry('800x600')
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.main_frame = tkinter.Frame(bg='lightgreen')
    self.main_frame.grid(row=0, column=0, sticky="nsew")
    self.titleLabel = tkinter.Label(self.main_frame, text="神経衰弱", font=('Times New Roman', 72, 'bold'), fg='pink', bg='white')
    self.titleLabel.pack(anchor='center', expand=True)
    self.changePageButton = tkinter.Button(self.main_frame, text="GAME START",bd=0, font=('Times New Roman', 36, 'italic'), fg='black', activebackground='pink', command=lambda : self.changePage(self.frame1))
    self.changePageButton.pack(anchor='center',expand=True)

    self.frame1 = tkinter.Frame()
    self.frame1.grid(row=0, column=0, sticky="nsew")
    self.titleLabel = tkinter.Label(self.frame1, text="Frame 1", font=('Helvetica', '35'))
    self.titleLabel.pack(anchor='center', expand=True)
    #self.back_button = tkinter.Button(self.frame1, text="Back", command=lambda : self.changePage(self.main_frame))
    #self.back_button.pack(anchor=tkinter.E)
    
    self.main_frame.tkraise()

  def changePage(self, page):
    page.tkraise()

app = App()
app.mainloop()

# root = tkinter.Tk()
# root.title('神経衰弱')
# #root.resizable('False','False')
# root.geometry('800x600+350+100')
# #'widthxhieght+x軸+y軸'
# label=tkinter.Label(root, text='神経衰弱', font=('Times New Roman', 72), fg='blue')
# label.pack(anchor='center', expand=True)
# button = tkinter.Button(root, text='GAME START', font=('Times New Roman', 36), activebackground='gray')
# button.pack(anchor='center',expand=True)
# #button.pack(side=tkinter.BOTTOM,expand=True,ipadx=10,ipady=10)
# #side どの方向から順にウィジェットを詰め込んでいくかを設定
# #tkinter.TOP：上から順に（デフォルト）
# #tkinter.BOTTOM：下から順に
# #tkinter.LEFT：左から順に
# #tkinter.RIGHT：右から順に
# #expand Trueに指定することで、親ウィジェットで使用されていないスペースを利用してウィジェットを配置するスペースを拡大することができる
# root.mainloop()