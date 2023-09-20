from random import randrange

from animal import Animal
from direction import Direction
from plants.grass import Grass
from ground import Ground


class barszczSosnowskiego(Grass):
    def __init__(self, _world=None, _x=None, _y=None, _age=0, _init=0, _power=10):
        super(barszczSosnowskiego, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return '~'

    def Color(self):
        return "red4"

    def Divide(self, _chances):
        if len(_chances) == 0:
            return
        else:
            for i in range(randrange(len(_chances))):
                _chances.pop(0)
            if _chances[0] == Direction.UP:
                self.world.ToAdd(barszczSosnowskiego(self.world, self.x - 1, self.y))
            elif _chances[0] == Direction.DOWN:
                self.world.ToAdd(barszczSosnowskiego(self.world, self.x + 1, self.y))
            elif _chances[0] == Direction.RIGHT:
                self.world.ToAdd(barszczSosnowskiego(self.world, self.x, self.y + 1))
            elif _chances[0] == Direction.LEFT:
                self.world.ToAdd(barszczSosnowskiego(self.world, self.x, self.y - 1))

    def Collision(self, _collider):
        from animals.cyberSheep import CyberSheep
        if not isinstance(_collider, CyberSheep):
            self.world.Log(self.GetSign() + " burns " + _collider.GetSign())
            self.world.board[self.y][self.x] = Ground()
            self.world.board[_collider.y][_collider.x] = Ground()
        else:
            self.world.Log(_collider.GetSign() + " eats " + self.GetSign())
            self.world.board[self.y][self.x] = Ground()

    def Burn(self):
        from animals.cyberSheep import CyberSheep
        if self.y == 0:
            if self.x == 0:
                if isinstance(self.world.board[self.y][self.x + 1], Animal) and not \
                        isinstance(self.world.board[self.y][self.x + 1], CyberSheep):
                    self.world.board[self.y][self.x + 1] = Ground()
                if isinstance(self.world.board[self.y + 1][self.x + 1], Animal) and not \
                        isinstance(self.world.board[self.y + 1][self.x + 1], CyberSheep):
                    self.world.board[self.y + 1][self.x + 1] = Ground()
                if isinstance(self.world.board[self.y + 1][self.x], Animal) is not \
                        isinstance(self.world.board[self.y + 1][self.x], CyberSheep):
                    self.world.board[self.y + 1][self.x] = Ground()
            elif self.x == self.world.height - 1:  # bot left
                if isinstance(self.world.board[self.y][self.x - 1], Animal) and not \
                        isinstance(self.world.board[self.y][self.x - 1], CyberSheep):
                    self.world.board[self.y][self.x - 1] = Ground()
                if isinstance(self.world.board[self.y + 1][self.x - 1], Animal) and not \
                        isinstance(self.world.board[self.y + 1][self.x - 1], CyberSheep):
                    self.world.board[self.y + 1][self.x - 1] = Ground()
                if isinstance(self.world.board[self.y + 1][self.x], Animal) and not \
                        isinstance(self.world.board[self.y + 1][self.x], CyberSheep):
                    self.world.board[self.y + 1][self.x] = Ground()
            else:  # left edge
                if isinstance(self.world.board[self.y][self.x - 1], Animal) and not \
                        isinstance(self.world.board[self.y][self.x - 1], CyberSheep):
                    self.world.board[self.y][self.x - 1] = Ground()
                if isinstance(self.world.board[self.y + 1][self.x - 1], Animal) and not \
                        isinstance(self.world.board[self.y + 1][self.x - 1], CyberSheep):
                    self.world.board[self.y + 1][self.x - 1] = Ground()
                if isinstance(self.world.board[self.y + 1][self.x], Animal) and not \
                        isinstance(self.world.board[self.y + 1][self.x], CyberSheep):
                    self.world.board[self.y + 1][self.x] = Ground()
                if isinstance(self.world.board[self.y][self.x + 1], Animal) and not \
                        isinstance(self.world.board[self.y][self.x + 1], CyberSheep):
                    self.world.board[self.y][self.x + 1] = Ground()
                if isinstance(self.world.board[self.y + 1][self.x + 1], Animal) and not \
                        isinstance(self.world.board[self.y + 1][self.x + 1], CyberSheep):
                    self.world.board[self.y + 1][self.x + 1] = Ground()
        elif self.y == self.world.width - 1:
            if self.x == 0:  # top right
                if isinstance(self.world.board[self.y][self.x + 1], Animal) and not \
                        isinstance(self.world.board[self.y][self.x + 1], CyberSheep):
                    self.world.board[self.y][self.x + 1] = Ground()
                if isinstance(self.world.board[self.y - 1][self.x + 1], Animal) and not \
                        isinstance(self.world.board[self.y - 1][self.x + 1], CyberSheep):
                    self.world.board[self.y - 1][self.x + 1] = Ground()
                if isinstance(self.world.board[self.y - 1][self.x], Animal) and not \
                        isinstance(self.world.board[self.y - 1][self.x], CyberSheep):
                    self.world.board[self.y - 1][self.x] = Ground()
            elif self.x == self.world.height - 1:  # bot right
                if isinstance(self.world.board[self.y][self.x - 1], Animal) and not \
                        isinstance(self.world.board[self.y][self.x - 1], CyberSheep):
                    self.world.board[self.y][self.x - 1] = Ground()
                if isinstance(self.world.board[self.y - 1][self.x - 1], Animal) and not \
                        isinstance(self.world.board[self.y - 1][self.x - 1], CyberSheep):
                    self.world.board[self.y - 1][self.x - 1] = Ground()
                if isinstance(self.world.board[self.y - 1][self.x], Animal) and not \
                        isinstance(self.world.board[self.y - 1][self.x], CyberSheep):
                    self.world.board[self.y - 1][self.x] = Ground()
            else:  # right edge
                if isinstance(self.world.board[self.y][self.x - 1], Animal) and not \
                        isinstance(self.world.board[self.y][self.x - 1], CyberSheep):
                    self.world.board[self.y][self.x - 1] = Ground()
                if isinstance(self.world.board[self.y - 1][self.x - 1], Animal) and not \
                        isinstance(self.world.board[self.y - 1][self.x - 1], CyberSheep):
                    self.world.board[self.y - 1][self.x - 1] = Ground()
                if isinstance(self.world.board[self.y - 1][self.x], Animal) and not \
                        isinstance(self.world.board[self.y - 1][self.x], CyberSheep):
                    self.world.board[self.y - 1][self.x] = Ground()
                if isinstance(self.world.board[self.y][self.x + 1], Animal) and not \
                        isinstance(self.world.board[self.y][self.x + 1], CyberSheep):
                    self.world.board[self.y][self.x + 1] = Ground()
                if isinstance(self.world.board[self.y - 1][self.x + 1], Animal) and not \
                        isinstance(self.world.board[self.y - 1][self.x + 1], CyberSheep):
                    self.world.board[self.y - 1][self.x + 1] = Ground()
        elif self.x == 0:  # top without corners
            if isinstance(self.world.board[self.y][self.x + 1], Animal) and not \
                    isinstance(self.world.board[self.y][self.x + 1], CyberSheep):
                self.world.board[self.y][self.x + 1] = Ground()
            if isinstance(self.world.board[self.y + 1][self.x + 1], Animal) and not \
                    isinstance(self.world.board[self.y + 1][self.x + 1], CyberSheep):
                self.world.board[self.y + 1][self.x + 1] = Ground()
            if isinstance(self.world.board[self.y - 1][self.x + 1], Animal) and not \
                    isinstance(self.world.board[self.y - 1][self.x + 1], CyberSheep):
                self.world.board[self.y - 1][self.x + 1] = Ground()
            if isinstance(self.world.board[self.y + 1][self.x], Animal) and not \
                    isinstance(self.world.board[self.y + 1][self.x], CyberSheep):
                self.world.board[self.y + 1][self.x] = Ground()
            if isinstance(self.world.board[self.y - 1][self.x], Animal) and not \
                    isinstance(self.world.board[self.y - 1][self.x], CyberSheep):
                self.world.board[self.y - 1][self.x] = Ground()
        elif self.x == self.world.height - 1:  # bot without corners
            if isinstance(self.world.board[self.y][self.x - 1], Animal) and not \
                    isinstance(self.world.board[self.y][self.x - 1], CyberSheep):
                self.world.board[self.y][self.x - 1] = Ground()
            if isinstance(self.world.board[self.y + 1][self.x - 1], Animal) and not \
                    isinstance(self.world.board[self.y + 1][self.x - 1], CyberSheep):
                self.world.board[self.y + 1][self.x - 1] = Ground()
            if isinstance(self.world.board[self.y - 1][self.x - 1], Animal) and not \
                    isinstance(self.world.board[self.y - 1][self.x - 1], CyberSheep):
                self.world.board[self.y - 1][self.x - 1] = Ground()
            if isinstance(self.world.board[self.y + 1][self.x], Animal) and not \
                    isinstance(self.world.board[self.y + 1][self.x], CyberSheep):
                self.world.board[self.y + 1][self.x] = Ground()
            if isinstance(self.world.board[self.y - 1][self.x], Animal) and not \
                    isinstance(self.world.board[self.y - 1][self.x], CyberSheep):
                self.world.board[self.y - 1][self.x] = Ground()

        else:
            if isinstance(self.world.board[self.y][self.x - 1], Animal) and not \
                    isinstance(self.world.board[self.y][self.x - 1], CyberSheep):
                self.world.board[self.y][self.x - 1] = Ground()
            if isinstance(self.world.board[self.y + 1][self.x - 1], Animal) and not \
                    isinstance(self.world.board[self.y + 1][self.x - 1], CyberSheep):
                self.world.board[self.y + 1][self.x - 1] = Ground()
            if isinstance(self.world.board[self.y - 1][self.x - 1], Animal) and not \
                    isinstance(self.world.board[self.y - 1][self.x - 1], CyberSheep):
                self.world.board[self.y - 1][self.x - 1] = Ground()
            if isinstance(self.world.board[self.y + 1][self.x], Animal) and not \
                    isinstance(self.world.board[self.y + 1][self.x], CyberSheep):
                self.world.board[self.y + 1][self.x] = Ground()
            if isinstance(self.world.board[self.y - 1][self.x], Animal) and not \
                    isinstance(self.world.board[self.y - 1][self.x], CyberSheep):
                self.world.board[self.y - 1][self.x] = Ground()
            if isinstance(self.world.board[self.y][self.x + 1], Animal) and not \
                    isinstance(self.world.board[self.y][self.x + 1], CyberSheep):
                self.world.board[self.y][self.x + 1] = Ground()
            if isinstance(self.world.board[self.y + 1][self.x + 1], Animal) and not \
                    isinstance(self.world.board[self.y + 1][self.x + 1], CyberSheep):
                self.world.board[self.y + 1][self.x + 1] = Ground()
            if isinstance(self.world.board[self.y - 1][self.x + 1], Animal) and not \
                    isinstance(self.world.board[self.y - 1][self.x + 1], CyberSheep):
                self.world.board[self.y - 1][self.x + 1] = Ground()