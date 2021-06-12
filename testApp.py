from tkinter import *
master = Tk()


def close_window():
    exit()

def testFunction():
    print("hi")

button = Button(master, text="hi", padx=10, pady=5, fg="white", bg="#263D42", command = testFunction())
button.pack(side=BOTTOM)
button.pack()
mainloop()