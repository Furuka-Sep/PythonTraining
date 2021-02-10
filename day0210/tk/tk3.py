import tkinder as tk
root = tk.Tk()
root.title('My Window')
root.geometry('600×400')
# 文字出力のためのラベルを作成
label = tk.Label(root,text = 'Hello World!',font = ('Arial',50))
#labelを配置
label.place(x=100,y=100)
root.mainloop()
