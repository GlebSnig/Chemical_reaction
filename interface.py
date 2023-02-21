from tkinter import *
from threading import Thread
import main

def set_params():
    global H2, O2, OH, H2O, H, O
    H2 = entry1.get()
    O2 = entry2.get()
    OH = entry3.get()
    H2O = entry4.get()
    H = entry5.get()
    O = entry6.get()

def task():
    thr = Thread(target= main.simulate(), daemon= True)
    thr.start()

H2 = None
O2 = None
OH = None
H2O = None
H = None
O = None


root = Tk()
root.title("Цепная реакция. Ввод параметров")
root.geometry("600x600")

text = Label(text="Начальное число молекул каждого типа")
text.pack(anchor=NW, padx=10, pady=0)

text1 = Label(text="Н2")
text1.pack(anchor=NW, padx=10, pady=0)

entry1 = Entry()
entry1.pack(anchor=NW, padx=10, pady=5)

text2 = Label(text="02")
text2.pack(anchor=NW, padx=10, pady=0)

entry2 = Entry()
entry2.pack(anchor=NW, padx=10, pady=5)

text3 = Label(text="OH")
text3.pack(anchor=NW, padx=10, pady=0)

entry3 = Entry()
entry3.pack(anchor=NW, padx=10, pady=5)

text4 = Label(text="H2O")
text4.pack(anchor=NW, padx=10, pady=0)

entry4 = Entry()
entry4.pack(anchor=NW, padx=10, pady=5)

text5 = Label(text="H")
text5.pack(anchor=NW, padx=10, pady=0)

entry5 = Entry()
entry5.pack(anchor=NW, padx=10, pady=5)

text6 = Label(text="O")
text6.pack(anchor=NW, padx=10, pady=0)

entry6 = Entry()
entry6.pack(anchor=NW, padx=10, pady=5)

btn = Button(text="Ввод", command=set_params)
btn.pack(anchor=NW, padx=10, pady=5)

label1 = Label()
label1.pack(anchor=NW, padx=6, pady=6)

label2 = Label()
label2.pack(anchor=NW, padx=6, pady=6)

btn = Button(text="Запуск", command=task)
btn.pack(anchor=NW, padx=10, pady=5)


root.mainloop()