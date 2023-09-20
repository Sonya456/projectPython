import math

from animal import Animal
from direction import Direction
from ground import Ground
from plants.barszczSosnowskiego import barszczSosnowskiego


class CyberSheep(Animal):
    def __init__(self, _world=None, _x=None, _y=None, _age=0, _init=4, _power=11):
        super(CyberSheep, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'C'

    def Color(self):
        return "cyan"

    def Split(self):
        dir = super().RandDir()
        if dir == Direction.UP and self.x > 0 or \
                dir == Direction.DOWN and self.x < self.world.height - 1 or \
                dir == Direction.RIGHT and self.y < self.world.width - 1 or \
                dir == Direction.LEFT and self.y > 0:
            if isinstance(super().Next(dir, 1), Ground):
                if dir == Direction.UP:
                    self.world.ToAdd(CyberSheep(self.world, self.x - 1, self.y))
                    return
                elif dir == Direction.DOWN:
                    self.world.ToAdd(CyberSheep(self.world, self.x + 1, self.y))
                    return
                elif dir == Direction.RIGHT:
                    self.world.ToAdd(CyberSheep(self.world, self.x, self.y + 1))
                    return
                elif dir == Direction.LEFT:
                    self.world.ToAdd(CyberSheep(self.world, self.x, self.y - 1))
                    return

    def Action(self, dir=None):
        dir = self.FindClosestSH()
        if dir == Direction.UP and self.x > 0 or \
            dir == Direction.DOWN and self.x < self.world.height-1 or \
            dir == Direction.LEFT and self.y > 0 or \
            dir == Direction.RIGHT and self.y < self.world.width-1:
            if isinstance(super().Next(dir, 1), Ground):
                super().Move(dir)
            else:
                super().Next(dir, 1).Collision(self)
                if isinstance(super().Next(dir, 1), Ground):
                    super().Move(dir)

    def FindClosestSH(self):
        distance = math.sqrt(math.pow(self.world.height, 2) + math.pow(self.world.width, 2))
        temp = None
        SHexist = False
        X=0
        Y=0
        dir = None
        for it in self.world.organisms:
            if isinstance(it, barszczSosnowskiego) and isinstance(self.world.board[it.y][it.x], barszczSosnowskiego):
                print("found")
                SHexist = True
                break
        if SHexist:
            for it in self.world.organisms:
                if isinstance(it, barszczSosnowskiego) and isinstance(self.world.board[it.y][it.x], barszczSosnowskiego):
                    temp = math.sqrt(math.pow(it.x - self.x, 2) + math.pow(it.y-self.y, 2))
                    if temp < distance:
                        distance = temp
                        self.X = it.x
                        self.Y = it.y
            # print("CS location: (", str(self.x) + ", " + str(self.y) + ")")
            # print("SH location: (", str(self.X) + ", " + str(self.Y) + ")")
            if abs(self.x - self.X) > abs(self.y - self.Y):
                if self.x > self.X:
                    dir = Direction.UP
                else:
                    dir = Direction.DOWN
            else:
                if self.y > self.Y:
                    dir = Direction.LEFT
                else:
                    dir = Direction.RIGHT
            # print(str(dir) + "(" + str(self.x) + ", " + str(self.y) + ")")
            return dir
        else:
            return super().NewDir()
