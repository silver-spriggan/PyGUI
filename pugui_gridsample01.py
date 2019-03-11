import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

entries = {} # this 'entries'is what you might want to specify a custom class to manage
             # for now,a dictionary will do

for j in range(10):
    for i in range(10):
        e = tkinter.Entry(frame)
        e.grid(column=i,row=j, borderwidth=0)
        es[i,j] = e
