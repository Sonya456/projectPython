from random import randrange

from Settings import Settings
from animals.antylope import Antylope
from animals.cyberSheep import CyberSheep
from animals.fox import Fox
from animals.human import Human
from animals.turtle import Turtle
from animals.sheep import Sheep
from animals.wolf import Wolf
from plants.grass import Grass
from ground import Ground
from plants.guarana import Guarana
from plants.barszczSosnowskiego import barszczSosnowskiego
from plants.sowThistle import SowThistle
from plants.wolfBerries import WolfBerries
from world import World


def FillWithOrganisms(_world):
    _world.add(Grass(_world, 0, 0))
    _world.add(barszczSosnowskiego(_world, 1, 1))
    _world.add(Guarana(_world, 0, 5))
    _world.add(SowThistle(_world, 5, 7))
    _world.add(WolfBerries(_world, 3, 5))
    _world.add(Wolf(_world, 4, 9))
    _world.add(Fox(_world, 7, 7))
    _world.add(Sheep(_world, 8, 15))
    _world.add(Turtle(_world, 4, 15))
    _world.add(CyberSheep(_world, 3, 13))
    _world.add(Antylope(_world, 8, 12))


def SpawnRandomFew(world, amount):
    world.add(Human(world, 0, 0))
    for i in range(amount):
        x = randrange(world.height)
        y = randrange(world.width)
        print("Spawning in (" + str(x) + ", " + str(y) + ")")
        if isinstance(world.board[y][x], Ground):
            print("Spawned!")
            temp = randrange(11)
            if temp == 0:
                world.add(CyberSheep(world, x, y))
            elif temp == 1:
                world.add(barszczSosnowskiego(world, x, y))
            elif temp == 2:
                world.add(Antylope(world, x, y))
            elif temp == 3:
                world.add(Fox(world, x, y))
            elif temp == 4:
                world.add(Sheep(world, x, y))
            elif temp == 5:
                world.add(Turtle(world, x, y))
            elif temp == 6:
                world.add(Wolf(world, x, y))
            elif temp == 7:
                world.add(Guarana(world, x, y))
            elif temp == 8:
                world.add(SowThistle(world, x, y))
            elif temp == 9:
                world.add(WolfBerries(world, x, y))
            elif temp == 10:
                world.add(Grass(world, x, y))


def SpecificSpawn(world):
    world.add(CyberSheep(world, 0, 7))
    world.add(barszczSosnowskiego(world, 9, 0))
    world.add(barszczSosnowskiego(world, 9, 14))


if __name__ == '__main__':
    world = World(20, 15, Settings,)
    #FillWithOrganisms(world)
    SpawnRandomFew(world, 70)
    #SpecificSpawn(world)
    world.PrintWorld()
