from random import random

from animal import Animal
from direction import Direction
from ground import Ground


class Human(Animal):
    id = None
    turnsLeft = None

    def __init__(self,  _world=None, _x=None, _y=None, _age=0, _init=4, _power=5, _id=171619, _turnsLeft=0):
        super(Human, self).__init__(_world, _x, _y, _age, _init, _power)
        self.id = _id
        self.turnsLeft = _turnsLeft

    def GetSign(self):
        return 'H'

    def Color(self):
        return "DodgerBlue3"

    def TurnsLeft(self):
        return self.turnsLeft

    def Action(self, dir=None):
        if dir == Direction.UP and self.x > 0 or\
            dir == Direction.DOWN and self.x < self.world.height-1 or\
            dir == Direction.LEFT and self.y > 0 or\
            dir == Direction.RIGHT and self.y < self.world.width-1:
            if isinstance(super().Next(dir, 1), Ground):
                super().Move(dir)
                if self.turnsLeft > 3:
                    super().Move(dir)
                elif self.turnsLeft > 1:
                    if random() <= 0.5:
                        super().Move(dir)
            else:
                super().Next(dir, 1).Collision(self)
                if isinstance(super().Next(dir, 1), Ground):
                    super().Move(dir)
        if self.turnsLeft > 0:
            # self.Burn()
            self.turnsLeft -= 1

    def UseAbility(self):
        if self.turnsLeft == 0:
            self.turnsLeft = 6

    def Burn(self):
       pass

    def Print(self):
        out = super().Print()
        out += ":" + str(self.id) + ":" + str(self.turnsLeft)
        return out