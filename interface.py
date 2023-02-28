import tkinter as tk
from threading import Thread
import main

def set_params():
    defaultMols.clear()
    defaultMols.append(int(entry1.get()))
    defaultMols.append(int(entry2.get()))

def task():
    thr = Thread(target= main.simulate(defaultMols), daemon= True)
    thr.start()

defaultMols= []

root = tk.Tk()
root.title("Цепная реакция")
root.geometry("320x260")

text = tk.Label(text="Цепная реакция ввод параметров")
text.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)
text1 = tk.Label(text="Количество молекул Н2")
text1.grid(row=1, column=0, sticky=tk.W, pady=10, padx=10)
entry1 = tk.Entry()
entry1.insert(0, '0')
entry1.grid(row=2, column=0, sticky=tk.W, pady=10, padx=10)
text2 = tk.Label(text="Количество молекул O2")
text2.grid(row=3, column=0, sticky=tk.W, pady=10, padx=10)
entry2 = tk.Entry()
entry2.insert(0, '0')
entry2.grid(row=4, column=0, sticky=tk.W, pady=10, padx=10)

btn1 = tk.Button(text="Ввод", command=set_params)
btn1.grid(row=5, column=0, sticky=tk.W, pady=10, padx=10)
btn2 = tk.Button(text="Запуск", command=task)
btn2.place(x=70, y=210)

label1 = tk.Label(text="O2 ")
label1.place(x=250, y=10)
colour1 = tk.Label(text="   ", background = 'red', borderwidth=1, relief="solid")
colour1.place(x=285, y=10)

label2= tk.Label(text="H2 ")
label2.place(x=250, y=50)
colour2 = tk.Label(text="   ", background = 'blue', borderwidth=1, relief="solid")
colour2.place(x=285, y=50)

label3 = tk.Label(text="OH ")
label3.place(x=250, y=90)
colour3 = tk.Label(text="   ", background = 'LightSkyBlue2', borderwidth=1, relief="solid")
colour3.place(x=285, y=90)

label4 = tk.Label(text="H ")
label4.place(x=250, y=130)
colour4 = tk.Label(text="   ", background = 'green', borderwidth=1, relief="solid")
colour4.place(x=285, y=130)

label5 = tk.Label(text="O ")
label5.place(x=250, y=170)
colour5 = tk.Label(text="   ", background = 'DarkOrchid', borderwidth=1, relief="solid")
colour5.place(x=285, y=170)

label6 = tk.Label(text="H2O ")
label6.place(x=250, y=210)
colour6 = tk.Label(text="   ", background = 'pink', borderwidth=1, relief="solid")
colour6.place(x=285, y=210)

root.mainloop()