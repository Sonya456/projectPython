from random import random, randrange

from animal import Animal
from direction import Direction
from ground import Ground


class Turtle(Animal):
    def __init__(self, _world, _x, _y, _age=0, _init=1, _power=2):
        super(Turtle, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'Z'

    def Color(self):
        return "dark green"

    def Split(self):
        dir = super().RandDir()
        if dir == Direction.UP and self.x > 0 or \
            dir == Direction.DOWN and self.x < self.world.height - 1 or \
            dir == Direction.RIGHT and self.y < self.world.width - 1 or \
            dir == Direction.LEFT and self.y > 0:
            if isinstance(super().Next(dir, 1), Ground):
                if dir == Direction.UP:
                    self.world.ToAdd(Turtle(self.world, self.x-1, self.y))
                    return
                elif dir == Direction.DOWN:
                    self.world.ToAdd(Turtle(self.world, self.x+1, self.y))
                    return
                elif dir == Direction.RIGHT:
                    self.world.ToAdd(Turtle(self.world, self.x, self.y+1))
                    return
                elif dir == Direction.LEFT:
                    self.world.ToAdd(Turtle(self.world, self.x, self.y-1))
                    return

    def Action(self):
        temp = randrange(4)
        if temp == 0:
            super().Action()

    def Collision(self, _collider):
        if isinstance(_collider, Turtle):
            self.Split()
        elif _collider.power < 5:
            self.world.Log("t blocks " + _collider.GetSign())
            return
        elif _collider.power > self.power:
            self.world.Log(_collider.GetSign() + " kills " + self.GetSign())
            self.world.board[self.y][self.x] = Ground()
        else:
            self.world.Log(self.GetSign() + " kills " + _collider.GetSign())
            self.world.board[_collider.y][_collider.x] = Ground()