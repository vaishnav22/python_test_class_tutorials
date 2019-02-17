from tkinter import *
win = Tk()
b = Label(win,text="enter the name:")
b.grid(row=0,column=0)

def show_data():
    char1 = b1.get()
    print(char1)

    


b1 = Entry(win)
b1.grid(row=0,column=1)
win.geometry("500x270")

next_lable1 = Label(win,text="enter the age:")
next_lable1.grid(row=1,column=0)

button1 = Button(win,text="enter",command=show_data)
button1.grid(row=4,column=2)

next_entry = Entry(win)
next_entry.grid(row=1,column=1)




win.mainloop()