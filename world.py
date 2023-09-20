import os
from tkinter import *

from Settings import Settings
from animals.antylope import Antylope
from animals.cyberSheep import CyberSheep
from animals.fox import Fox
from animals.sheep import Sheep
from animals.turtle import Turtle
from animals.wolf import Wolf
from app import App
from ground import Ground
from animals.human import Human
from plants.guarana import Guarana
from plants.barszczSosnowskiego import barszczSosnowskiego
from plants.sowThistle import SowThistle
from plants.wolfBerries import WolfBerries


class World:
    sinceLastSuperAbility = 0
    width = None
    height = None
    organisms = []
    toAdd = []
    toRem = []
    log = ""
    humanAlive = False
    board = None
    window = App()

    def __init__(self, _width, _height, Settings,):
        self.Settings = Settings
        self.width = _width
        self.height = _height
        self.board = [[Ground(self, i, j) for i in range(self.height)] for j in range(self.width)]
        self.log = ""
        # print("H: " + str(self.height))
        # print("W: " + str(self.width))

    # def printAmounts(self):
    #     hum = 0
    #     print(str(len(self.organisms)))
    #     for it in self.organisms:
    #         sign = it.GetSign()
    #         if sign == self.Settings.symbol_antylopy:
    #             self.Settings.count_antylopy += 1
    #         elif sign == self.Settings.symbol_cyber_owcy:
    #             self.Settings.count_cyber_owcy += 1
    #         elif sign == self.Settings.symbol_person:
    #             hum += 1
    #         elif sign == self.Settings.symbol_owcy:
    #             self.Settings.count_owcy += 1
    #         elif sign == self.Settings.symbol_zolw:
    #             self.Settings.count_zolw += 1
    #         elif sign == self.Settings.symbol_lisa:
    #             self.Settings.count_lisa += 1
    #         elif sign == self.Settings.symbol_wilka:
    #             self.Settings.count_wilka += 1
    #         elif sign == self.Settings.symbol_jagody:
    #             self.Settings.count_jagody += 1
    #         elif sign == self.Settings.symbol_barszczy:
    #             self.Settings.count_barszczy += 1
    #         elif sign == self.Settings.symbol_trawy:
    #             self.Settings.count_trawy += 1
    #         elif sign == self.Settings.symbol_gurany:
    #             self.Settings.count_gurany += 1
    #         elif sign == self.Settings.symbol_mlecza:
    #             self.Settings.count_mlecza += 1
    #     #print(self.Settings.max_count_gurany)
    #     # if self.Settings.max_count_cyber_owcy > self.Settings.max_count_wilka :
    #     #     print("CyberSheeps:")
    #
    #     # print("Humans: " + str(hum))
    #     # print("Sheeps: " + str(self.Settings.count_owcy))
    #     # print("Turtles: " + str(self.Settings.count_zolw ))
    #     # print("Foxes: " + str(self.Settings.count_lisa))
    #     # print("Wolves: " + str(self.Settings.count_wilka))
    #     # print("Wolf Berries: " + str(self.Settings.count_jagody))
    #     # print("Sosnowskis hogeweed: " + str(self.Settings.count_barszczy))
    #     # print("Grass: " + str(self.Settings.count_trawy ))
    #     # print("Guaranas: " + str(self.Settings.count_gurany))
    #     # print("Sow Thistles: " + str(self.Settings.count_mlecza))

    def PrintWorld(self):
        self.window.addWorld(self)

    def StartHumanAbility(self):
        if self.sinceLastSuperAbility == 0:
            for it in self.organisms:
                if isinstance(it, Human):
                    it.UseAbility()
                    self.sinceLastSuperAbility = 10
                    print("Superability used!")

    def add(self, _newO):
        # print("Adding new organism!")
        self.board[_newO.y][_newO.x] = _newO
        if len(self.organisms) == 0:
            self.organisms.insert(len(self.organisms), _newO)
        else:
            added = False
            for it in self.organisms:
                if _newO.initiative > it.initiative:
                    self.organisms.insert(self.organisms.index(it), _newO)
                    return
            if not added:
                self.organisms.insert(len(self.organisms), _newO)

    def ToAdd(self, _newO):
        self.board[_newO.y][_newO.x] = _newO
        self.toAdd.insert(len(self.toAdd), _newO)

    def NextTurn(self, _dir=None):
        for it in self.organisms:
            if it.age > 0:
                if self.board[it.y][it.x].GetSign() == it.GetSign():
                    if isinstance(it, Human):
                        it.Action(_dir)
                    else:
                        it.Action()
        for it in self.toAdd:
            if not isinstance(it, Ground):
                self.add(it)
        self.toAdd.clear()
        for it in self.organisms:
            if isinstance(it, barszczSosnowskiego):
                it.Burn()
        for it in self.organisms:
            if isinstance(self.board[it.y][it.x], Ground):
                self.toRem.insert(len(self.toRem), it)
        for it in self.toRem:
            self.organisms.remove(it)
        self.toRem.clear()
        for it in self.organisms:
            it.age += 1
        for it in self.organisms:
            if isinstance(it, Human):
                if it.TurnsLeft() > 0:
                    it.Burn()
        if self.sinceLastSuperAbility > 0:
            self.sinceLastSuperAbility -= 1

    def Log(self, _log):
        self.log += _log
        self.log += '\n'

    def PrintLog(self):
        output = Tk()
        t = Text(output, height=100, width=100)
        t.pack()
        t.insert(END, self.log)
        print("Log:")
        print(self.log)

    def Save(self):
        name = "save.txt"
        self.SaveToFile(name)
        print("Saved to file:", name)

    def SaveToFile(self, name):
        file = open("saves/" + name, "w")
        file.write(str(self.width) + ":" + str(self.height) + ":" + str(len(self.organisms)) + ":" +
                   str(self.sinceLastSuperAbility) + '\n')
        for it in self.organisms:
            file.write(it.Print() + '\n')
        file.close()

    def Load(self):
        name = "save.txt"
        self.LoadFromFile(name)

    def LoadFromFile(self, name):
        if os.path.isfile("saves/" + name):
            file = open("saves/" + name, "r")
            self.log = ""
            self.board = []
            self.organisms.clear()
            data = file.readline()
            print(data)
            data = data.split(':')
            print(data)
            # print(data[0] + " " + str(int(data[0])))
            self.width = int(data[0])
            self.height = int(data[1])
            self.sinceLastSuperAbility = int(data[3])
            self.board = [[Ground(self, i, j) for i in range(self.height)] for j in range(self.width)]
            out = ""
            for i in range(self.height):
                for j in range(self.width):
                    out += self.board[j][i].GetSign()
                out += '\n'
            print(out)
            for i in range(int(data[2])):
                data = file.readline()
                data = data.split(':')
                _org = data[0]
                _x = int(data[1])
                _y = int(data[2])
                _age = int(data[3])
                _power = int(data[4])
                _init = int(data[5])
                if _org == 'A':  # antylope
                    self.add(Antylope(self, _x, _y, _age, _power, _init))
                elif _org == 'C':  # cyberSheep
                    self.add(CyberSheep(self, _x, _y, _age, _power, _init))
                elif _org == 'F':  # fox
                    self.add(Fox(self, _x, _y, _age, _power, _init))
                elif _org == 'H':  # human
                    self.add(Human(self, _x, _y, _age, _power, _init, int(data[6]), int(data[7])))
                elif _org == 'O':  # Sheep
                    self.add(Sheep(self, _x, _y, _age, _power, _init))
                elif _org == 'Z':  # Turtle
                    self.add(Turtle(self, _x, _y, _age, _power, _init))
                elif _org == 'W':  # Wolf
                    self.add(Wolf(self, _x, _y, _age, _power, _init))
                elif _org == 'G':  # Guarana
                    self.add(Guarana(self, _x, _y, _age, _power, _init))
                elif _org == '~':  # Sosnowski's hogeweed
                    self.add(barszczSosnowskiego(self, _x, _y, _age, _power, _init))
                elif _org == 'J':  # Wolf Berries
                    self.add(WolfBerries(self, _x, _y, _age, _power, _init))
                elif _org == 'M':  # Sow thistle
                    self.add(SowThistle(self, _x, _y, _age, _power, _init))
            self.window.printBoard()
            file.close()
        else:
            print("File doesn't exist!")



