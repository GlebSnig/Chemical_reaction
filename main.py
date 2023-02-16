import tkinter as tk
import random
import pygame as pg
import time


class Molecule:
    def __init__(self, type, x0, y0):
        self.type = type
        self.vx = random.randint(-3, 3)
        self.vy = random.randint(-3, 3)
        self.x0 = x0
        self.y0 = y0
        self.r = 12
        match type: # убрать в спаун
            case 'O2':
                self.r = 15
                self.color = 'red'
            case 'H2':
                self.r = 13
                self.color = 'blue'
            case 'OH':
                self.r = 17
                self.color = 'LightSkyBlue2'
            case 'H':
                self.r = 9
                self.color = 'gray29'
            case 'O':
                self.r = 11
                self.color = 'DarkOrchid'


    def molMove(self):
        self.x0 += self.vx
        self.y0 += self.vy
        self.ball = window.create_oval(self.x0 - self.r, self.y0 - self.r, self.x0 + self.r, self.y0 + self.r, fill= self.color)

def Spawn(molList):
    '''original molecules'''
    O2_count = 15
    H2_count = 0
    OH_count = 0
    H_count = 0
    O_count = 0
    for x_spawn in range(30, wx, 30):
        for y_spawn in range(30, wy, 30):
            type = 'default'
            m = Molecule(type, x_spawn, y_spawn)
            if (O2_count > 0):
                m.type = 'O2'
                O2_count -= 1
                continue
            if (H2_count > 0):
                m.type = 'H2'
                H2_count -= 1
                continue
            if (OH_count > 0):
                m.type = 'OH'
                OH_count -= 1
                continue
            if (H_count > 0):
                m.type = 'H'
                H_count -= 1
                continue
            if (O_count > 0):
                m.type = 'O'
                O_count -= 1

            molList.append(m)
        #     if O2_count + H2_count + OH_count + O_count + H_count == 0:
        #         break_out_flag = True
        #         break
        # if break_out_flag:
        #     break

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
    delMols = set()
    addMols = []
    for i in range(size - 1):
        for j in range(i + 1, size):
            mol1 = molList[i]
            mol2 = molList[j]
            molsPair = [mol1.type, mol2.type]
            v1 = pg.math.Vector2(mol1.x0, mol1.y0)
            v2 = pg.math.Vector2(mol2.x0, mol2.y0)
            nv = v2 - v1
            if v1.distance_to(v2) < mol1.r + mol2.r and nv != [0, 0]:
                if tuple(molsPair) in allPair:
                    delMols.add(i)
                    delMols.add(j)

                    addMols.append(Molecule(allPair[tuple(molsPair)][0]))
                    addMols.append(Molecule(allPair[tuple(molsPair)][1]))

                else:
                    m1 = pg.math.Vector2(mol1.vx, mol1.vy).reflect(nv)
                    m2 = pg.math.Vector2(mol2.vx, mol2.vy).reflect(nv)
                    mol1.vx, mol1.vy = m1.x, m1.y
                    mol2.vx, mol2.vy = m2.x, m2.y
    delMols = list(delMols)
    delMols.sort()
    delta = 0
    for index in delMols:
        _ = molList.pop(index - delta)
        delta += 1
    for mol in addMols:
        molList.append(mol)

'''window construct'''
root = tk.Tk()
wx = 1000
wy = 600
window = tk.Canvas(root, width=wx, height=wy)
window.pack()

'''settings'''
molList = []
allPair = {('H2', 'O2'):('OH', 'OH'), ('O2', 'H2'):('OH', 'OH'),('OH', 'H2'):('H2O', 'H'), ('H2', 'OH'):('H2O', 'H'),\
           ('H', 'O2'):('OH', 'O'), ('O2', 'H'):('OH', 'O'), ('O', 'H2'):('OH', 'H'), ('H2', 'O'):('OH', 'H')}

"""main"""
Spawn(molList)
while True:
    window.delete('all')
    Physics(molList)
    for i in range(len(molList)):
        molList[i].molMove()
    root.update()
    time.sleep(0.0001)
root.mainloop()

#TODO сделать конструкторы для разых молекул, так чтобы подавался только тип и понему определялись остальные параметры
#TODO сделать спаун молекул матрицей