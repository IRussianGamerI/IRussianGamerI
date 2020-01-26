from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Radiobutton
import random

shiplist = []

# for i in range(20):
# file = open(str(i) + '.txt', 'r')

# zlines

window = Tk()
window.title("Main")
window.geometry("1000x450")
# frame = Frame(window, width=1000, height=450, bg="blue")
# frame.pack()
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
tab_control.pack(expand=1, fill="both")


# def clicked1():
#  i, j = shiplist[0][0], shiplist[0][1]
# click_list = [clicked1()]

def clicked():
    messagebox.showinfo("Miss", "Miss")


def promah(i, j):
    btn3 = Button(tab1, text="", command=clicked, padx=10, pady=10)
    btn3.grid(column=j + 1, row=i + 1)


def popal(i, j):
    matr[i][j] = Button(tab1, text="", command=knopka(i, j), padx=10, pady=10)
    matr[i][j].grid(column=j + 1, row=i + 1)
    r = random.choice(quest_set)
    rec_file = open(str(r) + '.txt', 'r')
    right = rec_file.readline()
    intzad = int(rec_file.readline())
    zad = ''
    for z in range(intzad):
        zad += rec_file.readline()
    intvar = int(rec_file.readline())
    for v in range(intvar):
        buttext = rec_file.readline()


def promah(i, j):
    btn = Button(tab1, text="", command=clicked, padx=10, pady=10)
    btn.grid(column=j + 1, row=i + 1)


shiplist = []

a = open('main.txt', 'r')
for i in range(10):
    s = a.readline()
    for j in range(10):
        if s[j] == 'H':
            shiplist.append([i, j])
        else:
            promah(i, j)


def clicked3():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="My brother ____ his homework in the evening.", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="makes", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="has", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="does", command=clicked4, value=3)
    rad3.grid(column=0, row=3)


def clicked5():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="After dinner Jane ____ the washing up.", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="watch", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="cleans", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="does", command=clicked4, value=3)
    rad3.grid(column=0, row=3)


def clicked6():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Do they ____their beds in the morning?", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="make", command=clicked4, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="clean", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="wash", command=clicked2, value=3)
    rad3.grid(column=0, row=3)


def clicked7():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="We like to ___ the stars in the evening", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="lay", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="watch", command=clicked4, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="clean", command=clicked2, value=3)
    rad3.grid(column=0, row=3)


def clicked8():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="The girls usually ____ lunch at 2 pm.", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="makes", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="watch", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="have", command=clicked4, value=3)
    rad3.grid(column=0, row=3)


def clicked9():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="I always ______ my homework in the evening.", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="have", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="do", command=clicked4, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="make", command=clicked2, value=3)
    rad3.grid(column=0, row=3)


def clicked9():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="I always ______ my homework in the evening.", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="have", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="do", command=clicked4, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="make", command=clicked2, value=3)
    rad3.grid(column=0, row=3)


def clicked10():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Mag ______ the flowers every morning.", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="washes", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="waters", command=clicked4, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="cleans", command=clicked2, value=3)
    rad3.grid(column=0, row=3)


def clicked11():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="When do you usually ______ lunch?", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="go", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="have", command=clicked4, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="do", command=clicked2, value=3)
    rad3.grid(column=0, row=3)


def clicked12():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="______ you do your homework two days ago?", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="Do", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="Will", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="Did", command=clicked4, value=3)
    rad3.grid(column=0, row=3)


def clicked13():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="His sister ______ puzzles yesterday.", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="didn't play", command=clicked4, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="doesn't play", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="won't play", command=clicked2, value=3)
    rad3.grid(column=0, row=3)


def clicked14():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="sofa", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="chair", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="table", command=clicked2, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="bed", command=clicked2, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="answer", command=clicked4, value=5)
    rad5.grid(column=0, row=5)

def clicked15():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="like", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="want", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="ask", command=clicked2, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="bad", command=clicked4, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="live", command=clicked2, value=5)
    rad5.grid(column=0, row=5)

def clicked16():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="red", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="black", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="big", command=clicked4, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="grey", command=clicked2, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="brown", command=clicked2, value=5)
    rad5.grid(column=0, row=5)

def clicked17():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="living room", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="bag", command=clicked4, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="bedroom", command=clicked2, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="hall", command=clicked2, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="flat", command=clicked2, value=5)
    rad5.grid(column=0, row=5)

def clicked18():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="rainy", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="windy", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="spring", command=clicked4, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="sunny", command=clicked2, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="cold", command=clicked2, value=5)
    rad5.grid(column=0, row=5)

def clicked19():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="windy", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="cold", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="summer", command=clicked4, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="sunny", command=clicked2, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="rainy", command=clicked2, value=5)
    rad5.grid(column=0, row=5)

def clicked20():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="cat", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="dog", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="rabbit", command=clicked2, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="stone", command=clicked4, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="elephant", command=clicked2, value=5)
    rad5.grid(column=0, row=5)

def clicked21():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="car", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="truck", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="train", command=clicked2, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="plane", command=clicked2, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="fly", command=clicked4, value=5)
    rad5.grid(column=0, row=5)

def clicked22():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="heart", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="brain", command=clicked2, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="lungs", command=clicked2, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="egg", command=clicked4, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="stomach", command=clicked2, value=5)
    rad5.grid(column=0, row=5)

def clicked23():
    window = Tk()
    window.title("Que")
    window.geometry("1000x450")
    lbl1 = Label(window, text="Выпишите лишнее слово", padx=0, pady=0, font="Times 15")
    lbl1.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="keyboard", command=clicked2, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="field", command=clicked4, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="mouse", command=clicked2, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="monitor", command=clicked2, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="printer", command=clicked2, value=5)
    rad5.grid(column=0, row=5)

btn1 = Button(tab1, text="", command=clicked3, padx=10, pady=10)
btn1.grid(column=2, row=1)
btn2 = Button(tab1, text="", command=clicked5, padx=10, pady=10)
btn2.grid(column=4, row=2)
btn3 = Button(tab1, text="", command=clicked6, padx=10, pady=10)
btn3.grid(column=5, row=2)
btn4 = Button(tab1, text="", command=clicked7, padx=10, pady=10)
btn4.grid(column=10, row=2)
btn5 = Button(tab1, text="", command=clicked8, padx=10, pady=10)
btn5.grid(column=7, row=3)
btn6 = Button(tab1, text="", command=clicked9, padx=10, pady=10)
btn6.grid(column=2, row=4)
btn7 = Button(tab1, text="", command=clicked10, padx=10, pady=10)
btn7.grid(column=3, row=4)
btn8 = Button(tab1, text="", command=clicked11, padx=10, pady=10)
btn8.grid(column=7, row=4)
btn9 = Button(tab1, text="", command=clicked12, padx=10, pady=10)
btn9.grid(column=7, row=5)
btn10 = Button(tab1, text="", command=clicked13, padx=10, pady=10)
btn10.grid(column=7, row=6)
btn11 = Button(tab1, text="", command=clicked14, padx=10, pady=10)
btn11.grid(column=4, row=7)
btn12 = Button(tab1, text="", command=clicked15, padx=10, pady=10)
btn12.grid(column=4, row=8)
btn13 = Button(tab1, text="", command=clicked16, padx=10, pady=10)
btn13.grid(column=7, row=8)
btn14 = Button(tab1, text="", command=clicked17, padx=10, pady=10)
btn14.grid(column=8, row=8)
btn15 = Button(tab1, text="", command=clicked18, padx=10, pady=10)
btn15.grid(column=9, row=8)
btn16 = Button(tab1, text="", command=clicked19, padx=10, pady=10)
btn16.grid(column=1, row=9)
btn17 = Button(tab1, command=clicked20, padx=10, pady=10)
btn17.grid(column=4, row=9)
btn18 = Button(tab1, text="", command=clicked21, padx=10, pady=10)
btn18.grid(column=6, row=10)
btn19 = Button(tab1, text="", command=clicked22, padx=10, pady=10)
btn19.grid(column=7, row=10)
btn20 = Button(tab1, text="", command=clicked23, padx=10, pady=10)
btn20.grid(column=9, row=10)

def clicked4():
    messagebox.showinfo("Right", "You're right.")


def clicked2():
    messagebox.showinfo("Неправильно", "Wrong. Your move turns to your enemy.")


def fileread():
    flrd = open()


matr = []
rad = []
for i in range(10):
    matr.append([None, None, None, None, None, None, None, None, None, None])
print(matr)
quest_set = []
for l in range(1, 16):
    quest_set.append(l)

    # rad.append(Radiobutton(tab1, text=buttext, value=v+1))
    # rad[v].grid(column=0, row=0)
    # rad.clear()

'''

def clicked3():
    messagebox.showinfo("Wrong", "Неверно. Ход переходит к сопернику.")
def clicked4():
    messagebox.showinfo("Wrong", "Неверно. Ход переходит к сопернику.")
def clicked5():
    messagebox.showinfo("Wrong", "Неверно. Ход переходит к сопернику.")
def clicked6():
    messagebox.showinfo("Wrong", "Неверно. Ход переходит к сопернику.")
def clicked7():
    messagebox.showinfo("Right", "Абсолютно верно. Продолжай в том же духе. Твой следующий ход.")
    btn = Button(btn2, text="", padx=5.5, pady=5.5, bg="red")
    btn.grid(column=0, row=0)

def clicked2():
    window = Tk()
    window.title("Question")
    window.geometry("1000x450")
    lbl = Label(window, text="Выпишите лишнее слово", padx=10, pady=5)
    lbl.grid(column=0, row=0)
    rad1 = Radiobutton(window, text="sofa", command=clicked3, value=1)
    rad1.grid(column=0, row=1)
    rad2 = Radiobutton(window, text="chair", command=clicked4, value=2)
    rad2.grid(column=0, row=2)
    rad3 = Radiobutton(window, text="table", command=clicked5, value=3)
    rad3.grid(column=0, row=3)
    rad4 = Radiobutton(window, text="bed", command=clicked6, value=4)
    rad4.grid(column=0, row=4)
    rad5 = Radiobutton(window, text="answer", command=clicked7, value=5)
    rad5.grid(column=0, row=5)
'''

'''
btn2 = Button(tab1, text="", command=clicked2, padx=10, pady=10)
btn2.grid(column=1, row=0)
btn3 = Button(tab1, text="", command=clicked8, padx=10, pady=10)
btn3.grid(column=2, row=0)
btn4 = Button(tab1, text="", command=clicked9, padx=10, pady=10)
btn4.grid(column=3, row=0)
Button(tab1, text="", command=clicked10, padx=10, pady=10).grid(column=4, row=0)
btn6 = Button(tab1, text="", command=clicked11, padx=10, pady=10)
btn6.grid(column=5, row=0)
btn7 = Button(tab1, text="", command=clicked12, padx=10, pady=10)
btn7.grid(column=6, row=0)
btn8 = Button(tab1, text="", command=clicked13, padx=10, pady=10)
btn8.grid(column=7, row=0)
btn9 = Button(tab1, text="", command=clicked14, padx=10, pady=10)
btn9.grid(column=8, row=0)
btn10 = Button(tab1, text="", command=clicked15, padx=10, pady=10)
btn10.grid(column=9, row=0)
btn11 = Button(tab1, text="", padx=10, pady=10)
btn11.grid(column=0, row=1)
btn12 = Button(tab1, text="", padx=10, pady=10)
btn12.grid(column=1, row=1)
'''
lbl1 = Label(tab1, text="A")
lbl1.grid(column=0, row=1)
lbl2 = Label(tab1, text="B")
lbl2.grid(column=0, row=2)
lbl3 = Label(tab1, text="C")
lbl3.grid(column=0, row=3)
lbl4 = Label(tab1, text="D")
lbl4.grid(column=0, row=4)
lbl5 = Label(tab1, text="E")
lbl5.grid(column=0, row=5)
lbl6 = Label(tab1, text="F")
lbl6.grid(column=0, row=6)
lbl7 = Label(tab1, text="G")
lbl7.grid(column=0, row=7)
lbl8 = Label(tab1, text="H")
lbl8.grid(column=0, row=8)
lbl9 = Label(tab1, text="I")
lbl9.grid(column=0, row=9)
lbl10 = Label(tab1, text="J")
lbl10.grid(column=0, row=10)
lbl11 = Label(tab1, text="1")
lbl11.grid(column=1, row=0)
lbl12 = Label(tab1, text="2")
lbl12.grid(column=2, row=0)
lbl13 = Label(tab1, text="3")
lbl13.grid(column=3, row=0)
lbl14 = Label(tab1, text="4")
lbl14.grid(column=4, row=0)
lbl15 = Label(tab1, text="5")
lbl15.grid(column=5, row=0)
lbl16 = Label(tab1, text="6")
lbl16.grid(column=6, row=0)
lbl17 = Label(tab1, text="7")
lbl17.grid(column=7, row=0)
lbl18 = Label(tab1, text="8")
lbl18.grid(column=8, row=0)
lbl19 = Label(tab1, text="9")
lbl19.grid(column=9, row=0)
lbl20 = Label(tab1, text="10")
lbl20.grid(column=10, row=0)
a.close()
tab_control.pack(expand=1, fill="both")
window.mainloop()
