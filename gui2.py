from tkinter import *

root = Tk()
root.title("Button")
root.geometry("500x500")
root.config(bg="lightblue")

label = Label(root, text="Button",bg="lightblue",fg="red",font="arial 20 bold")
label.pack()


def onClick(userText):
    label.config(text=userText)

root.button = Button(root, text="Click me",fg="red", bg="blue",font="arial 20 bold", command=lambda:onClick(my_entry.get()))

my_entry = Entry(root, width=30, font="Helvetica 20", border=5)

my_entry.pack()


root.button.pack()


root.mainloop()