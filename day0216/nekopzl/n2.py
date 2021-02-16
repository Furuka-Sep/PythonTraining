import tkinter as tk

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def game_main():
    global cursor_x, cursor_y
    if 24 <=  mouse_x < 24+72*8 and 24 <= mouse_y < 24+72*10:
        cursor_x = int((mouse_x-24)/72)
        cursor_y = int((mouse_y-24)/72)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
    root.after(60, game_main)

root = tk.Tk()
root.title("カーソルの表示")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
cvs = tk.Canvas(root, width=912, height=768)
cvs.pack()

bg = tk.PhotoImage(file="neko_bg.png")
cursor = tk.PhotoImage(file="neko_cursor.png")
cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()
