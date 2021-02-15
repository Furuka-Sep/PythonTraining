import tkinter as tk
	
index = 0 #画像indexはglobal

def btn_click():
    global index
    index=(index+1) % len(photos)
    canvas.delete('p1')	
    canvas.create_image(320,213,image=photos[index],tag='p1')

root = tk.Tk()
root.geometry('700x560')
root['bg'] = 'lightgrey'

#画像用キャンバス
canvas = tk.Canvas(width=640,height=426,bd=0,highlightthickness=0,relief='ridge')
#設置
canvas.pack(pady=20)
"""
#image用意
photo1 = tk.PhotoImage(file='cat1.png')
#image描画(x,y,image)
canvas.create_image(320,213,image=photo1,tag='p1')
photo2 = tk.PhotoImage(file='cat2.png')
canvas.create_image(340,233,image=photo2,tag='p2')
canvas.delete('p2')
"""

photos = [
        tk.PhotoImage(file='cat1.png'),
        tk.PhotoImage(file='cat2.png'),
        tk.PhotoImage(file='cat3.png'),
]
canvas.create_image(320,213,image=photos[index],tag='p1')

#ボタン
btn = tk.Button(text='Click',command=btn_click)
btn.pack(ipadx=10,ipady=5)

root.mainloop()
