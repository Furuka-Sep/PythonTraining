import tkinter
#上中央ボタン
"""
#画面作成
root = tkinter.Tk()
root.geometry('300x200')

#ボタン作成
btn = tkinter.Button(root, text='終了')
#配置
btn.pack()

root.mainloop()
"""
#ボタン横いっぱい
"""
#画面作成
root = tkinter.Tk()
root.geometry('300x200')

#ボタン作成
btn = tkinter.Button(root,text='終了')
#配置
btn.pack(fill = 'x')

root.mainloop()
"""
#ボタン横いっぱい+余白
"""
# 画面作成
root = tkinter.Tk()
root.geometry('300x200')

# ボタン作成
btn = tkinter.Button(root, text='終了')
# 配置
btn.pack(fill = 'x', padx=30)

root.mainloop()
"""
#ボタン横並び
"""
root = tkinter.Tk()
root.geometry('300x200')

#ボタン作成
btn = tkinter.Button(root,text='開始',width=14)
#配置
btn.pack(fikk = 'x',padx=20,side = 'left')
#ボタン作成
btn = tkinter.Button(root,text='終了',width=14)
#配置
btn.pack(fill = 'x',padx=20,side = 'left')

root.mainloop()
"""
#ボタン縦並び
"""
#画面作成
root = tkinter.Tk()
root.geometry('300x200')

#ボタン作成
btn = tkinter.Button(root,text='開始',width=14)
#配置
btn.pack(fill = 'x',padx=20,side = 'top')
#ボタン作成
btn = tkinter.Button(root,text='終了',width=14)
#配置
btn.pack(fill = 'x',padx=20,side = 'top')

root.mainloop()
"""
