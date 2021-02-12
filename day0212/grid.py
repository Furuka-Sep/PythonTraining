import tkinter

root = tkinter.Tk()
root.geometry('300x200')

# First Label
la = tkinter.Label(root, text='Hello everybody.',  bg='yellow', relief=tkinter.RIDGE, bd=2)
la.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Second Label
lb = tkinter.Label(root, text='Oh My God!', bg='red', relief=tkinter.RIDGE, bd=2)
lb.grid(row=1, column=0, padx=5, pady=5)

# Third Label
lc = tkinter.Label(root, text='See you tomorrow.', bg='LightSkyBlue', relief=tkinter.RIDGE, bd=2)
lc.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
