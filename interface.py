import tkinter as tk
from threading import Thread
import main

def set_params():
    defaultMols.clear()
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

root = tk.Tk()
root.title("Цепная реакция. Ввод параметров")
root.geometry("200x400")

text = tk.Label(text="Начальное число молекул каждого типа")
text.pack(anchor=tk.NW, padx=10, pady=0)
text1 = tk.Label(text="Н2")
text1.pack(anchor=tk.NW, padx=10, pady=0)
entry1 = tk.Entry()
entry1.insert(0, '0')
entry1.pack(anchor=tk.NW, padx=10, pady=5)
text2 = tk.Label(text="02")
text2.pack(anchor=tk.NW, padx=10, pady=0)
entry2 = tk.Entry()
entry2.insert(0, '0')
entry2.pack(anchor=tk.NW, padx=10, pady=5)
text3 = tk.Label(text="OH")
text3.pack(anchor=tk.NW, padx=10, pady=0)
entry3 = tk.Entry()
entry3.insert(0, '0')
entry3.pack(anchor=tk.NW, padx=10, pady=5)
text4 = tk.Label(text="H")
text4.pack(anchor=tk.NW, padx=10, pady=0)
entry4 = tk.Entry()
entry4.insert(0, '0')
entry4.pack(anchor=tk.NW, padx=10, pady=5)
text5 = tk.Label(text="O")
text5.pack(anchor=tk.NW, padx=10, pady=0)
entry5 = tk.Entry()
entry5.insert(0, '0')
entry5.pack(anchor=tk.NW, padx=10, pady=5)
btn1 = tk.Button(text="Ввод", command=set_params)
btn1.pack(anchor=tk.NW, padx=10, pady=5)
label1 = tk.Label()
label1.pack(anchor=tk.NW, padx=6, pady=6)
label2 = tk.Label()
label2.pack(anchor=tk.NW, padx=6, pady=6)
btn2 = tk.Button(text="Запуск", command=task)
btn2.pack(anchor=tk.NW, padx=30, pady=6)

root.mainloop()