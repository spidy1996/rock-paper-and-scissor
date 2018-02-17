import random

from tkinter import *


def compchoice():
    s = random.randrange(1, 4)
    if s == 1:
        return "Rock"
    elif s == 2:
        return "Paper"
    else:
        return "Scissor"


w = 0
l = 0


def game(first, second):
    global w,l
    if first == second:
        r.delete('1.0', END)
        r.insert(END, "You choose" + first + "\n")
        r.insert(END, "Comp chooses" + second + "\n")
        r.insert(END, "It is a tie!")
    elif first == "Rock":
        if second == "Scissor":
            r.delete('1.0', END)
            r.insert(END, "You choose" + first + "\n")
            r.insert(END, "Comp chooses" + second + "\n")
            r.insert(END, "You Won!")
            r2.delete('1.0', END)
            w += 1
            r2.insert(END, str(w))
        else:
            r.delete('1.0', END)
            r.insert(END, "You choose" + first + "\n")
            r.insert(END, "Comp chooses" + second + "\n")
            r.insert(END, "You Lose!")
            r3.delete('1.0', END)
            l += 1
            r3.insert(END, str(l))
    elif first == "Paper":
        if second == "Scissor":
            r.delete('1.0', END)
            r.insert(END, "You choose" + first + "\n")
            r.insert(END, "Comp chooses" + second + "\n")
            r.insert(END, "You Lose!")
            r3.delete('1.0', END)
            l += 1
            r3.insert(END, str(l))
        else:
            r.delete('1.0', END)
            r.insert(END, "You choose " + first + "\n")
            r.insert(END, "Comp chooses " + second + "\n")
            r.insert(END, "You Won!")
            r2.delete('1.0', END)
            w += 1
            r2.insert(END, str(w))
    else:
        if second == "Paper":
            r.delete('1.0', END)
            r.insert(END, "You choose " + first + "\n")
            r.insert(END, "Comp chooses " + second + "\n")
            r.insert(END, "You Won!")
            r2.delete('1.0', END)
            w += 1
            r2.insert(END, str(w))
        else:
            r.delete('1.0', END)
            r.insert(END, "You choose" + first + "\n")
            r.insert(END, "Comp chooses" + second + "\n")
            r.insert(END, "You Lose!")
            r3.delete('1.0', END)
            l += 1
            r3.insert(END, str(l))


root = Tk()
r = Text(root, width=20, height=5)
b1 = Button(root, text="Rock", command=lambda: game("Rock", compchoice()))
b2 = Button(root, text="Paper", command=lambda: game("Paper", compchoice()))
b3 = Button(root, text="Scissor", command=lambda: game("Scissor", compchoice()))
l1 = Label(root, text="Rock, Paper and Scissor!")
l2 = Label(root, text="Wins: ")
l3 = Label(root, text="Loses: ")
r2 = Text(root, width=3, height=1)
r3 = Text(root, width=3, height=1)
l1.grid(row=0, columnspan=4)
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
r.grid(row=2, column=1)
l2.grid(row=3, column=0)
r2.grid(row=3, column=1)
l3.grid(row=4, column=0)
r3.grid(row=4, column=1)
root.mainloop()
