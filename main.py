import tkinter as tk
import random
import pygame as pg
import time


class Molecule:
    def __init__(self, type, r, color):
        self.type = type
        self.r = r
        self.color = color
        self.x0 = random.randint(50, wx - 50)
        self.y0 = random.randint(50, wy - 50)
        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)
    def molMove(self):
        self.x0 += self.vx
        self.y0 += self.vy
        self.ball = window.create_oval(self.x0 - self.r, self.y0 - self.r, self.x0 + self.r, self.y0 + self.r, fill= self.color)

def Physics(molList):
    '''blows on walls'''
    for mol in molList:
        if mol.x0 + mol.r >= wx and mol.vx > 0:
            mol.vx = - mol.vx
        if mol.y0 + mol.r >= wy and mol.vy > 0:
            mol.vy = - mol.vy
        if mol.x0 - mol.r <= 0 and mol.vx < 0:
            mol.vx = - mol.vx
        if mol.y0 - mol.r <= 0 and mol.vy < 0:
            mol.vy = - mol.vy
    '''contemption of balls'''
    size = len(molList)
    for i in range(size - 1):
        for j in range(i + 1, size):
            mol1 = molList[i]
            mol2 = molList[j]

            v1 = pg.math.Vector2(mol1.x0, mol1.y0)
            v2 = pg.math.Vector2(mol2.x0, mol2.y0)
            if v1.distance_to(v2) < mol1.r + mol2.r:
                nv = v2 - v1
                m1 = pg.math.Vector2(mol1.vx, mol1.vy).reflect(nv)
                m2 = pg.math.Vector2(mol2.vx, mol2.vy).reflect(nv)
                mol1.vx, mol1.vy = m1.x, m1.y
                mol2.vx, mol2.vy = m2.x, m2.y

'''window construct'''
root = tk.Tk()
wx = 1000
wy = 600
window = tk.Canvas(root, width=wx, height=wy)
window.pack()

molList = []
for _ in range(5):
    m = Molecule("O", 20, 'blue')
    molList.append(m)

for _ in range(5):
    m = Molecule("H", 20, 'red')
    molList.append(m)

while True:
    window.delete('all')
    Physics(molList)
    for i in range(len(molList)):


        molList[i].molMove()

    root.update()
    time.sleep(0.0001)

root.mainloop()
