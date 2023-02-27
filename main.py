import tkinter as tk
import random
import pygame as pg
import time

class Molecule:
    def __init__(self, type, x0, y0):
        self.type = type
        self.r = None
        self.color = None
        self.x0 = x0
        self.y0 = y0
        self.vx = random.randint(1, 2)
        self.vy = random.randint(1, 2)
        match type:
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
                self.color = 'green'
            case 'O':
                self.r = 11
                self.color = 'DarkOrchid'
            case 'H2O':
                self.r = 20
                self.color = 'pink'

def MolMove(window):
    '''replace'''
    for mol in molList:
        mol.x0 += mol.vx
        mol.y0 += mol.vy
        mol.ball = window.create_oval(mol.x0 - mol.r, mol.y0 - mol.r, mol.x0 + mol.r, mol.y0 + mol.r, fill= mol.color)

def Spawn(defaultMol):
    '''original molecules'''
    O2_count = defaultMol[0]
    H2_count = defaultMol[1]
    break_out_flag = False
    for x_spawn in range(50, wx, 150):
        for y_spawn in range(50, wy, 150):
            if (O2_count > 0):
                type = 'O2'
                molList.append(Molecule(type, x_spawn, y_spawn))
                O2_count -= 1
                continue
            if (H2_count > 0):
                type = 'H2'
                molList.append(Molecule(type, x_spawn, y_spawn))
                H2_count -= 1
                continue
            if O2_count + H2_count == 0:
                break_out_flag = True
                break
        if break_out_flag:
            break

def Physics():
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
                    addMols.append(Molecule(allPair[tuple(molsPair)][0], mol1.x0 - mol1.vx * 3, mol1.y0 - mol1.vy * 3))
                    addMols.append(Molecule(allPair[tuple(molsPair)][1], mol2.x0 - mol2.vx * 3, mol2.y0 - mol2.vy * 3))
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

'''settings'''
wx = 1100
wy = 680
molList = []
allPair = {('H2', 'O2'):('OH', 'OH'), ('O2', 'H2'):('OH', 'OH'),('OH', 'H2'):('H2O', 'H'), ('H2', 'OH'):('H2O', 'H'),\
           ('H', 'O2'):('OH', 'O'), ('O2', 'H'):('OH', 'O'), ('O', 'H2'):('OH', 'H'), ('H2', 'O'):('OH', 'H')}

def simulate(defaultMol):
    '''window construct'''
    root = tk.Tk()
    root.title("Симуляция")
    window = tk.Canvas(root, width=wx, height=wy)
    window.pack()
    """main"""
    molList.clear()
    Spawn(defaultMol)
    while True:
        window.delete('all')
        Physics()
        MolMove(window)
        root.update()
        time.sleep(0.0001)
    root.mainloop()