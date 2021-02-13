import tkinter as tk
def btn_click():
    amount = int(ent1.get())
    people = int(ent2.get())
    dnum = amount / people
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = int(pay + 100)
    payorg = amount - pay * (people - 1)
    lab3['text']=('1人あたり{}円({}人)、幹事は{}円です'.format(pay,people - 1,payorg))

root = tk.Tk()
root.title('割り勘くん')

canvas = tk.Canvas(root,width=300,height=500,bg='light blue')
canvas.pack()

text = tk.StringVar()
lab1 = tk.Label(root,text='金額',bg='light blue')
lab1.place(x=20,y=20)
ent1 = tk.Entry(width=20,bg='white')
ent1.place(x=20,y=45)
lab2 = tk.Label(root,text='人数',bg='light blue')
lab2.place(x=20,y=70)
ent2 = tk.Entry(width=20,bg='white')
ent2.place(x=20,y=95)
btn = tk.Button(text='計算する',command=btn_click)
btn.place(x=20,y=125)
lab3 = tk.Label(root,text='',bg='light blue')
lab3.place(x=20,y=150)

root.mainloop()
