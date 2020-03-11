from tkinter import *
root = Tk()

root.title("Simple GUI")
root.geometry("500x500")

frame = Frame(root, bg = "GREEN")
frame.grid()


lbl = Label(frame, text = "cockroack gang cockroach gang", bg = "GREEN")
lbl.grid()

photo = PhotoImage(file = r"C:\Users\benjamin.vielstich\Downloads\cockroach.gif")

photoimage = photo.subsample(3,3)
text_entry = Entry(frame)
text_entry.grid()

bttn1 = Button(frame,bg = "PURPLE", text = "kill", image = photoimage, compound = LEFT)
bttn1.grid()


frame2 = Frame(root, bg = "RED")
frame2.grid()

lbl2 = Label(frame2, text = "who do you want to heal", bg = "RED")
lbl2.grid()

text_entry2 = Entry(frame2)
text_entry2.grid()

bttn2 = Button(frame2, bg = "GREEN", text = "heal")
bttn2.grid()




root.mainloop()