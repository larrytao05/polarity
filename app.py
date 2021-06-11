import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import os
from colour import Color

root = tk.Tk()
canvas = tk.Canvas(root, height=540, width=960, bg="#FFFFFF")
canvas.pack()

frame = tk.Frame(root, bg="dark red")
frame.place(relwidth=0.15, relheight=0.1, relx=0.05, rely=0.5)

frame = tk.Frame(root, bg="red")
frame.place(relwidth=0.15, relheight=0.1, relx=0.24, rely=0.5)

frame = tk.Frame(root, bg="grey")
frame.place(relwidth=0.15, relheight=0.1, relx=0.43, rely=0.5)

frame = tk.Frame(root, bg="light green")
frame.place(relwidth=0.15, relheight=0.1, relx=0.62, rely=0.5)

frame = tk.Frame(root, bg="green")
frame.place(relwidth=0.15, relheight=0.1, relx=0.81, rely=0.5)


# Create text widget and specify size.
T = Text(root, height=5, width=52)



# Create button for next text.
b1 = Button(root, text="Strongly Against", bg="dark red", font=("Arial", 12))
b2 = Button(root, text="Against", bg="red", font=("Arial", 12))
b3 = Button(root, text="Neutral", bg="grey", font=("Arial", 12))
b4 = Button(root, text="Support", bg="light green", font=("Arial", 12))
b5 = Button(root, text="Strongly Support", bg="green", font=("Arial", 12))

# Create an Exit button.


T.pack()
b1.place(relwidth=0.15, relheight=0.1, relx=0.05, rely=0.5)
b2.place(relwidth=0.15, relheight=0.1, relx=0.24, rely=0.5)
b3.place(relwidth=0.15, relheight=0.1, relx=0.43, rely=0.5)
b4.place(relwidth=0.15, relheight=0.1, relx=0.62, rely=0.5)
b5.place(relwidth=0.15, relheight=0.1, relx=0.81, rely=0.5)




root.mainloop()
