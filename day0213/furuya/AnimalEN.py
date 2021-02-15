import tkinter as tk
import random
JA=["いぬ","ねこ","らいおん","ぞう","かんがるー","しろくま","ぺんぎん","あり","くじら","ひと"]
EN=["dog","cat","lion","elephant","kangaroo","polarbear","penguin","ant","whale","human"]
count=0
score=0
def btn1():
    global count,score,EN,JA,imgl
    ans = ent.get()
    if count == 10:
        canvas.delete("animal")
        canvas.create_image(300,100,image=Animals[9],tag="animal")
    elif count == 9:
        if ans == EN[count]:
            score += 1
            judge['text']="正解!\nあなたは10問中{}問正解しました!".format(score)
        else:
            judge['text']="不正解!\n{}の答えは{}\nあなたは10問中{}問正解しました!".format(JA[count-1],EN[count],score)
        
    elif ans == EN[count]:
        score += 1
        judge['text']="正解!"
        count += 1
        canvas.delete("animal")
        canvas.create_image(300,100,image=Animals[count],tag="animal")
    else:
        judge['text']="不正解!\n{}の答えは{}".format(JA[count],EN[count])
        count += 1
        canvas.delete("animal")
        canvas.create_image(300,100,image=Animals[count],tag="animal")
    ja["text"]=JA[count]
root = tk.Tk()
root.title("動物英語で書けるかな")

canvas=tk.Canvas(root,width=600,height=300)
Animals=list()
for i in range(len(JA)*10):
    rnd1=random.randint(0,9)
    rnd2=random.randint(0,9)
    JA[rnd1],JA[rnd2] = JA[rnd2],JA[rnd1]
    EN[rnd1],EN[rnd2] = EN[rnd2],EN[rnd1]
for i in range(len(EN)):
    img = tk.PhotoImage(file=EN[i]+".png",)
    img = img.subsample(2)
    Animals.append(img)
img = tk.PhotoImage(file=EN[count]+".png")
img = img.subsample(2)
canvas.create_image(300,100,image=img,tag="animal")

ja = tk.Label(root,text="{}".format(JA[count]), font=("Times New Roman", 40))
ja.pack(anchor='center')

judge = tk.Label(font=("Times New Roman", 30))
judge.pack(anchor='center')

ent = tk.Entry(width=10,font=("Times New Roman",30))
ent.pack(anchor='center')

judge = tk.Label(root,text="", font=("Times New Roman", 25)) 
judge.pack(anchor='center',side=tk.BOTTOM)

btn = tk.Button(text="こたえ", font=("Times New Roman", 25), bg="pink", command=btn1)
btn.pack(anchor='center',side=tk.BOTTOM)

canvas.pack()

root.mainloop()    
