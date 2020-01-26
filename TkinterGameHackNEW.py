#coding: utf-8
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Radiobutton
import random

Freeze = False
Score = 0
BattleShipScore = 20



window = Tk()
window.title("Main")
window.geometry("1000x525")
#frame = Frame(window, width=1000, height=450, bg="blue")
#frame.pack()
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
             
#def MISS():
#    messagebox.showinfo("Miss", "Miss")
#    matr = Button(tab1, text="", padx=5.5, pady=5.5, bg="blue")
#    matr.grid(column=0, row=0)

quest_set = []
for _0_ in range(1, 21):
    quest_set.append(_0_)

class Variant:
    def __init__(self, txt, win, row, val, right, btn, a):
        self.btn = btn
        self.ANOTHER = a
        self.txt = txt
        self.right = right
        self.win = win
        self.value = val
        self.radiobtn = Radiobutton(self.win, text=self.txt, command=self.TRUE if self.right==True else self.FALSE, value=self.value)
        self.radiobtn.grid(column=0, row=row)

    def TRUE(self):
        global Score
        Score += 5
        global BattleShipScore
        BattleShipScore -= 1
        self.btn["command"] = self.ANOTHER
        self.btn["activebackground"] = "red"
        self.btn["bg"] = "red"
        self.btn.update()
        if BattleShipScore == 0:
            messagebox.showinfo("WIN", "You're Win.\nYour score is "+str(Score))
            exit()
        else:
            messagebox.showinfo("Right", "You're right.\nYour score is "+str(Score))
            self.win.destroy()

    def FALSE(self):
        global Score
        Score -= 2
        messagebox.showinfo("Wrong", "Your move turns to your enemy.")
        self.win.destroy()


class WindowMSG:
    def __init__(self, question, btn, a):
        self.btn = btn
        self.a = a
        self.question = question
        self.OpenedFile = open(str(self.question)+'.txt')
        self.txt = []
        self.variante = []
        for self.num in range(int(self.OpenedFile.readline())):
            self.txt.append(self.OpenedFile.readline())
        for self.num in range(int(self.OpenedFile.readline())):
            self.variante.append(self.OpenedFile.readline())
            if self.num == 0:
                self.right = self.variante[0]
        self.variant = random.shuffle(self.variante)
        self.radiobuttons = []
        self.window = Tk()
        self.window.title("Question")
        self.window.geometry("450x450")
        self.num = 0
        self.text = []
        for self.t in self.txt:
            self.text = Label(self.window, text=self.t, padx=0, pady=0, font="Times 15")
            self.text.grid(column = 0, row = self.num)
            self.num += 1
        self.n = 0
        for self.var in self.variante:
            self.radiobuttons.append(Variant(self.var, self.window, self.num, self.n, True if self.var == self.right else False, self.btn, self.a))
            self.num += 1
        self.window.mainloop()
        
        
                
class ButtonOnField:
    def __init__(self, ButtonType, xPos, yPos):
        self.ButtonType = ButtonType
        self.xPos = xPos
        self.yPos = yPos
        self.btn = Button(tab1, text="", command=self.HIT if ButtonType == 'H' else self.MISS, padx=18, pady=10)
        self.Question = random.choice(quest_set) if ButtonType == 'H' else None
        if self.Question != None:
            quest_set.index(self.Question)
        self.btn.grid(column=xPos, row=yPos)

    def MISS(self):
        if not Freeze:
            self.btn["command"] = self.ANOTHER
            self.btn["activebackground"] = "blue"
            self.btn["bg"] = "blue"
            messagebox.showinfo("Miss", "Miss")
            self.btn.update()

    def HIT(self):
        if not Freeze:
            self.btn["activebackground"] = "yellow"
            self.btn["bg"] = "yellow"
            self.btn.update()
            WindowMSG(self.Question, self.btn, self.ANOTHER)
            

    def ANOTHER(self):
        pass

matr = []
rad = []
for i in range(10):
    matr.append([None, None, None, None, None, None, None, None, None, None])



OpenedField = open('main.txt', 'r')
for y in range(10):
    LINE = OpenedField.readline()
    for x in range(10):
        matr[y][x] = ButtonOnField(LINE[x], x+1, y+1)
        



#a = open('main.txt', 'r')
#for i in range(10):
#    s = a.readline()
#    for j in range(10):
#        if s[j] == 'H':
#            popal(i, j)
#        else:
#            promah(i, j)
#            print("AAAAAAAAAAAAAAAAAAAA")

lbl1 = Label(tab1, text="A", padx=10, pady=10)
lbl1.grid(column=0, row=1)
lbl2 = Label(tab1, text="B", padx=10, pady=10)
lbl2.grid(column=0, row=2)
lbl3 = Label(tab1, text="C", padx=10, pady=10)
lbl3.grid(column=0, row=3)
lbl4 = Label(tab1, text="D", padx=10, pady=10)
lbl4.grid(column=0, row=4)
lbl5 = Label(tab1, text="E", padx=10, pady=10)
lbl5.grid(column=0, row=5)
lbl6 = Label(tab1, text="F", padx=10, pady=10)
lbl6.grid(column=0, row=6)
lbl7 = Label(tab1, text="G", padx=10, pady=10)
lbl7.grid(column=0, row=7)
lbl8 = Label(tab1, text="H", padx=10, pady=10)
lbl8.grid(column=0, row=8)
lbl9 = Label(tab1, text="I", padx=10, pady=10)
lbl9.grid(column=0, row=9)
lbl10 = Label(tab1, text="J", padx=10, pady=10)
lbl10.grid(column=0, row=10)
lbl11 = Label(tab1, text="1", padx=10, pady=10)
lbl11.grid(column=1, row=0)
lbl12 = Label(tab1, text="2", padx=10, pady=10)
lbl12.grid(column=2, row=0)
lbl13 = Label(tab1, text="3", padx=10, pady=10)
lbl13.grid(column=3, row=0)
lbl14 = Label(tab1, text="4", padx=10, pady=10)
lbl14.grid(column=4, row=0)
lbl15 = Label(tab1, text="5", padx=10, pady=10)
lbl15.grid(column=5, row=0)
lbl16 = Label(tab1, text="6", padx=10, pady=10)
lbl16.grid(column=6, row=0)
lbl17 = Label(tab1, text="7", padx=10, pady=10)
lbl17.grid(column=7, row=0)
lbl18 = Label(tab1, text="8", padx=10, pady=10)
lbl18.grid(column=8, row=0)
lbl19 = Label(tab1, text="9", padx=10, pady=10)
lbl19.grid(column=9, row=0)
lbl20 = Label(tab1, text="10", padx=10, pady=10)
lbl20.grid(column=10, row=0)
OpenedField.close()
tab_control.pack(expand=1, fill="both")
window.mainloop()
