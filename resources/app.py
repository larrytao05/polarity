import tkinter
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import pygame
import os
from colour import Color
from PIL import Image, ImageTk

root = Tk()
root.title('polarity')
root.iconbitmap(r'c:\Users\jackk\Downloads\p.ico')

root.minsize(height=540, width=960)
# chat_btn = PhotoImage(file="image needed here")
# img_label = Label(image=chat_btn)
# img_label.pack(pady=5, padx=10)
issues = ["Abortion", "Gun Ownership", "LGBTQ Rights", "Tax Increases", "Vaccines"]
opinions = ["Strongly Against", "Against", "Neutral", "Support", "Strongly Support"]
topic = {}
opinion = {}
messageRecieved = False


def start():
    def opinionTab(currentTopic):
        topic[0] = currentTopic
        # we need to have the code recognize the user choice for topic and then have that be stored in the "topic" variable
        frame.destroy()
        frame1 = tk.Frame(root, bg="white")
        frame1.place(relwidth=1, relheight=1)

        opinionlabel = Label(frame1, text="What Are Your Opinions on " + topic[0] + ":", font=("Helvetica", 20,),
                             fg="#cf9fff", bg="white")

        photo1 = PhotoImage(file=r"C:\Users\jackk\Downloads\button (5).png")
        strongAgainst = Button(root, highlightthickness=0, bd=0, image=photo1,command=lambda: waitingScreen(frame1, opinions[0]))
        strongAgainst.place(x=40, y=200)

        photo2 = PhotoImage(file=r"C:\Users\jackk\Downloads\button (2).png")
        against = Button(root, highlightthickness=0, bd=0, image=photo2,command=lambda: waitingScreen(frame1, opinions[1]))
        against.place(x=40 + (180 * 1), y=200)

        photo3 = PhotoImage(file=r"C:\Users\jackk\Downloads\button (1).png")
        neutral = Button(root, highlightthickness=0, bd=0, image=photo3,command=lambda: waitingScreen(frame1, opinions[2]))
        neutral.place(x=40 + (180 * 2), y=200)

        photo4 = PhotoImage(file=r"C:\Users\jackk\Downloads\button (3).png")
        support = Button(root, highlightthickness=0, bd=0, image=photo4,command=lambda: waitingScreen(frame1, opinions[3]))
        support.place(x=40 + (180 * 3), y=200)

        photo5 = PhotoImage(file=r"C:\Users\jackk\Downloads\button (4).png")
        strongSupport= Button(root,highlightthickness = 0, bd = 0, image=photo5, command=lambda: waitingScreen(frame1, opinions[4]))
        strongSupport.place(x=40 + (180 * 4), y=200)


        opinionlabel.pack(side=TOP)
        returnToStart = Button(frame1, text="Back", padx=10, pady=5, fg="white", bg="#cf9fff", command=start)
        returnToStart.place(x=0, y=0)




    def waitingScreen(oldFrame, currentOpinion):
        opinion[0] = currentOpinion
        oldFrame.destroy()

        waitingFrame = Frame(root, bg="white")
        waitingFrame.place(relwidth=1, relheight=1)
        waitingLabel = Label(waitingFrame, text="Pairing you with a random person...", font=('Helvetica', 25),
                             fg="#cf9fff", bg="white")
        waitingLabel.pack(side=TOP)

        cancelChat = Button(waitingFrame, text="Cancel", padx=10, pady=5, fg="white", bg="#cf9fff",
                            command=lambda: opinionTab(topic[0]))
        cancelChat.place(x=0, y=0)

        cancelChat = Button(waitingFrame, text="Skip", padx=10, pady=5, fg="white", bg="#cf9fff",
                            command=lambda: createChat(waitingFrame))
        cancelChat.place(x=500, y=500)

    def createChat(frame3):
        frame3.destroy()
        chatFrame = Frame(root, bg="white")
        chatFrame.place(relwidth=1, relheight=1)
        chatLabel = Label(chatFrame, text="Discussion", font=('Helvetica', 25), fg="#cf9fff", bg="white")
        chatLabel.pack(side=TOP)
        exitChat = Button(chatFrame, text="Exit", padx=10, pady=5, fg="white", bg="#cf9fff", command=start)
        exitChat.place(x=0, y=50)
        returnToOpinions = Button(chatFrame, text="Back", padx=10, pady=5, fg="white", bg="#cf9fff",
                                  command=lambda: opinionTab(topic[0]))
        returnToOpinions.place(x=0, y=0)

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=1, relheight=1)

    label1 = Label(frame, text="Welcome to polarity!"
                   , font=("Helvetica", 20), fg="#cf9fff", bg="white")
    label1.place(relx=0.36, rely=0.01)
    polarity = PhotoImage(file=r"C:\Users\jackk\Downloads\polarity font.png")
    logo = Button(root, highlightthickness=0, bd=0, image=polarity)
    logo.place(x=250, y=280)

    label2 = Label(frame,
                   text="We want to bring our nation together through a series of honest discussion and open communication"
                   , font=("Helvetica", 15), fg="#cf9fff", bg="white")
    label2.place(relx=0.042, rely=0.08)
    label3 = Label(frame, text="Please select a current event or political issue to get started!"
                   , font=("Helvetica", 15), fg="#cf9fff", bg="white")
    label3.place(relx=0.22, rely=0.15)

    issue1 = PhotoImage(file=r"C:\Users\jackk\Downloads\babies.png")
    abortion = Button(root, highlightthickness=0, bd=0, image=issue1, command=lambda: opinionTab(issues[0]))
    abortion.place(x=(570 - (len(issues) * 150) + (1 * 195)), y=200)


    issue2 = PhotoImage(file=r"C:\Users\jackk\Downloads\guns.png")
    guns = Button(root, highlightthickness=0, bd=0, image=issue2, command=lambda: opinionTab(issues[1]))
    guns.place(x=(570 - (len(issues) * 150) + (2 * 195)), y=200)

    issue3 = PhotoImage(file=r"C:\Users\jackk\Downloads\lgbt.png")
    lgbt = Button(root, highlightthickness=0, bd=0, image=issue3, command=lambda: opinionTab(issues[2]))
    lgbt.place(x=(570 - (len(issues) * 150) + (3 * 195)), y=200)

    issue4 = PhotoImage(file=r"C:\Users\jackk\Downloads\tax.png")
    tax = Button(root, highlightthickness=0, bd=0, image=issue4, command=lambda: opinionTab(issues[3]))
    tax.place(x=(570 - (len(issues) * 150) + (4 * 195)), y=200)

    issue5 = PhotoImage(file=r"C:\Users\jackk\Downloads\vaccines.png")
    vaccines = Button(root, highlightthickness=0, bd=0, image=issue5, command=lambda: opinionTab(issues[4]))
    vaccines.place(x=(570 - (len(issues) * 150) + (5 * 195)), y=200)


    mainloop()




start()
root.mainloop()
