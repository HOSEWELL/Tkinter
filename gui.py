from tkinter import *
from datetime import *

root = Tk()

root.title("DIGITAL CLOCK")

root.geometry("800x600")

root.config(bg="steel blue")

label = Label(root,text="Digital Clock", bg="steel blue",fg="red", font="arial 58 bold")

label.pack(anchor='center')
def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.config(text=time)
    label.after(1000,clock)
clock()


root.mainloop()