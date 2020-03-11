from tkinter import *
root = Tk()

root.title("windows")
root.geometry("500x500")
root.config(bg = "BLACK")

base_frame = Frame(root, width = 499, height = 499, bg = "Black")
base_frame.grid(sticky = NSEW)

frame1 = Frame(base_frame, width = 200, height = 150, background = "Blue")
frame1.grid(row = 1, column = 0)
lbl1 = Label(base_frame, text = "blue", bg = "blue")
lbl1.grid(row = 1, column = 0)

frame2 = Frame(base_frame, width = 200, height = 150, background = "Red")
frame2.grid(row = 2, column = 0)
lbl2 = Label(base_frame, text = "red", bg = "red")
lbl2.grid(row = 2, column = 0)

frame3 = Frame(base_frame, width = 200, height = 150, background = "Green")
frame3.grid(row = 1, column = 1)
lbl3 = Label(base_frame, text = "green", bg = "green")
lbl3.grid(row = 1, column = 1)

frame4 = Frame(base_frame, width = 200, height = 150, background = "Yellow")
frame4.grid(row = 2, column = 1)
lbl4 = Label(base_frame, text = "yellow", bg = "yellow")
lbl4.grid(row = 2, column = 1)

frame5 = Frame(base_frame, width = 400, height = 150, background = "purple")
frame5.grid(row = 0, columnspan = 2)
lbl5 = Label(base_frame, text = "purple", bg = "purple")
lbl5.grid(row = 0, columnspan = 2)


root.mainloop()