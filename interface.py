from tkinter import *
from threading import Thread
import main

def set_params(defaultMols):
    defaultMols.append(int(entry1.get()))
    defaultMols.append(int(entry2.get()))
    defaultMols.append(int(entry3.get()))
    defaultMols.append(int(entry4.get()))
    defaultMols.append(int(entry5.get()))
    print(defaultMols)

def task():
    thr = Thread(target= main.simulate(defaultMols), daemon= True)
    thr.start()

defaultMols= []

root = Tk()
root.title("Цепная реакция. Ввод параметров")
root.geometry("600x600")

text = Label(text="Начальное число молекул каждого типа")
text.pack(anchor=NW, padx=10, pady=0)

text1 = Label(text="Н2")
text1.pack(anchor=NW, padx=10, pady=0)

entry1 = Entry()
entry1.insert(0, '0')
entry1.pack(anchor=NW, padx=10, pady=5)

text2 = Label(text="02")
text2.pack(anchor=NW, padx=10, pady=0)

entry2 = Entry()
entry2.insert(0, '0')
entry2.pack(anchor=NW, padx=10, pady=5)

text3 = Label(text="OH")
text3.pack(anchor=NW, padx=10, pady=0)

entry3 = Entry()
entry3.insert(0, '0')
entry3.pack(anchor=NW, padx=10, pady=5)

text4 = Label(text="H")
text4.pack(anchor=NW, padx=10, pady=0)

entry4 = Entry()
entry4.insert(0, '0')
entry4.pack(anchor=NW, padx=10, pady=5)

text5 = Label(text="O")
text5.pack(anchor=NW, padx=10, pady=0)

entry5 = Entry()
entry5.insert(0, '0')
entry5.pack(anchor=NW, padx=10, pady=5)

btn1 = Button(text="Ввод", command=set_params(defaultMols))
btn1.pack(anchor=NW, padx=10, pady=5)

label1 = Label()
label1.pack(anchor=NW, padx=6, pady=6)

label2 = Label()
label2.pack(anchor=NW, padx=6, pady=6)


btn2 = Button(text="Запуск", command=task)
btn2.pack(anchor=NW, padx=10, pady=5)


root.mainloop()