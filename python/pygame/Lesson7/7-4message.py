import tkinter
import tkinter.messagebox

#7-4メッセージボックスを表示する
#メッセージボックスの使い方
def click_btn():
  tkinter.messagebox.showinfo('情報', 'ボタンを押しました') #メッセージボックスの表示

root = tkinter.Tk()
root.title('初めてのメッセージボックス')
root.geometry('400x200')
btn = tkinter.Button(text='テスト', command=click_btn)
btn.pack()
root.mainloop()

"""
showinfo() 情報を表示するメッセージボックス
showwarning() 警告を表示するメッセージボックス
showerror() エラーを表示するメッセージボックス
askyesno() 「はい」「いいえ」のボタンがあるメッセージボックス
askokcancel() 「OK」「キャンセル」のボタンがあるメッセージボックス
"""