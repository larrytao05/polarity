import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import pygame
import os
from colour import Color

root = Tk()
root.title('polarity')
# root.iconbitmap(r'c:\Users\jackk\Downloads\polarity font - Copy.ico')

root.minsize(height=540, width=960)
# chat_btn = PhotoImage(file="image needed here")
# img_label = Label(image=chat_btn)
# img_label.pack(pady=5, padx=10)
issues = ["Abortion", "Guns Ownership", "LGBTQ Rights", "Taxes", "Vaccines"]
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
        n=0

        opinionlabel = Label(frame1, text="What Are Your Opinions on "+topic[0]+":", font=("Helvetica", 20,), fg="#cf9fff", bg="white")
        b1 = Button(frame1, text=opinions[0], font=("Helvetica", 12), padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: confirmOpinion(frame1, currentTopic, opinions[0]))
        b2 = Button(frame1, text=opinions[1], font=("Helvetica", 12), padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: confirmOpinion(frame1, currentTopic, opinions[1]))
        b3 = Button(frame1, text=opinions[2], font=("Helvetica", 12), padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: confirmOpinion(frame1, currentTopic, opinions[2]))
        b4 = Button(frame1, text=opinions[3], font=("Helvetica", 12), padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: confirmOpinion(frame1, currentTopic, opinions[3]))
        b5 = Button(frame1, text=opinions[4], font=("Helvetica", 12), padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: confirmOpinion(frame1, currentTopic, opinions[4]))

        b1.place(x=40,y=200)
        b2.place(x=40+180,y=200)
        b3.place(x=40+(180*2),y=200)
        b4.place(x=40+(180*3),y=200)
        b5.place(x=40+(180*4),y=200)
        opinionlabel.pack(side=TOP)
        returnToStart = Button(frame1, text="Back", padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=start)
        returnToStart.place(x=0, y=0)


        for i in opinions:
            opinion = Button(frame1, text=i, font=("Helvetica", 12), padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: confirmOpinion(frame1, topic[0]))
            opinion.place(x=40+(180*n),y=200)
            n+=1

    def confirmOpinion(framee, currentOpinion):
        opinion[0] = currentOpinion
        framee.destroy()
        confirmFrame = Frame(root, bg="white")
        confirmFrame.place(relwidth=1, relheight=1)

        chat = Button(confirmFrame, text="Chat about "+topic[0], padx=20, font=("Helvetica", 25), highlightbackground="#cf9fff", pady=10, fg="white", bg="#cf9fff", command=lambda: waitingScreen(confirmFrame))
        chat.place(x=250, y=540 / 4)
        returnToOpinions = Button(confirmFrame, text="Back", padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: opinionTab(topic[0]))
        returnToOpinions.place(x=0, y=0)

    def waitingScreen(oldFrame):
        oldFrame.destroy()

        waitingFrame = Frame(root, bg="white")
        waitingFrame.place(relwidth=1, relheight=1)
        waitingLabel = Label(waitingFrame, text="Pairing you with a random person...", font=('Helvetica', 25),fg="#cf9fff", bg="white")
        waitingLabel.pack(side=TOP)

        cancelChat = Button(waitingFrame, text="Cancel", padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff",
                                  command=lambda: opinionTab(topic[0]))
        cancelChat.place(x=0, y=0)

        cancelChat = Button(waitingFrame, text="Skip", padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff",
                            command=lambda: createChat(waitingFrame))
        cancelChat.place(x=500, y=500)

    def createChat(frame3):
        frame3.destroy()
        chatFrame = Frame(root, bg="white")
        chatFrame.place(relwidth=1, relheight=1)
        chatLabel = Label(chatFrame, text="Discussion", font=('Helvetica', 25),fg="#cf9fff", bg="white")
        chatLabel.pack(side=TOP)
        exitChat = Button(chatFrame, text="Exit", padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=start)
        exitChat.place(x=0, y=50)
        returnToOpinions = Button(chatFrame, text="Back", padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: opinionTab(topic[0]))
        returnToOpinions.place(x=0,y=0)

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=1, relheight=1)

    label1 = Label(frame, text="Welcome to polarity!"
                  , font=("Helvetica", 20), fg="#cf9fff", bg="white")
    label1.place(relx=0.36, rely=0.01)
    label2 = Label(frame, text="We want to bring our nation together through a series of honest discussion and open communication"
                   , font=("Helvetica", 15), fg="#cf9fff", bg="white")
    label2.place(relx=0.042, rely=0.08)
    label3 = Label(frame, text="Please select a current event or political issue to get started!"
                   , font=("Helvetica", 15), fg="#cf9fff", bg="white")
    label3.place(relx=0.22, rely=0.15)

    issue1 = Button(frame, text=issues[0], padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: opinionTab(issues[0]))

    issue1.place(x=(600 - (len(issues) * 150) + 200), y=200)

    issue2 = Button(frame, text=issues[1], padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: opinionTab(issues[1]))
    issue2.place(x=(600 - (len(issues) * 150) + (2 * 200)), y=200)

    issue3 = Button(frame, text=issues[2], padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: opinionTab(issues[2]))
    issue3.place(x=(600 - (len(issues) * 150) + (3 * 200)), y=200)

    issue4 = Button(frame, text=issues[3], padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: opinionTab(issues[3]))
    issue4.place(x=(600 - (len(issues) * 150) + (4 * 200)), y=200)

    issue5 = Button(frame, text=issues[4], padx=10, pady=5, fg="white", bg="#cf9fff", highlightbackground="#cf9fff", command=lambda: opinionTab(issues[4]))
    issue5.place(x=(600 - (len(issues) * 150) + (5 * 200)), y=200)


start()
root.mainloop()
