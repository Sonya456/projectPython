from random import random, randrange
from direction import Direction
from ground import Ground
from organism import Organism


class Animal(Organism):
    def __init__(self, _world, _x, _y, _age, _init, _power):
        super().__init__(_world, _x, _y, _age, _init, _power)

    def Action(self, dir=None):
        dir = self.NewDir()
        if dir == Direction.UP and self.x > 0 or \
            dir == Direction.DOWN and self.x < self.world.height - 1 or \
            dir == Direction.LEFT and self.y > 0 or \
            dir == Direction.RIGHT and self.y < self.world.width - 1:
            if isinstance(self.Next(dir, 1), Ground):
                self.Move(dir)
            else:
                self.Next(dir, 1).Collision(self)
                if isinstance(self.Next(dir, 1), Ground):
                    self.Move(dir)

    def NewDir(self):
        dir = None
        temp = None
        if self.y == 0:
            if self.x == 0:  # top left corner
                temp = randrange(2)
                if temp == 0:
                    dir = Direction.DOWN
                elif temp == 1:
                    dir = Direction.RIGHT
            elif self.x == self.world.height - 1:  # bottom left corner
                temp = randrange(2)
                if temp == 0:
                    dir = Direction.UP
                elif temp == 1:
                    dir = Direction.RIGHT
            else:
                temp = randrange(3)
                if temp == 0:
                    dir = Direction.DOWN
                elif temp == 1:
                    dir = Direction.RIGHT
                elif temp == 2:
                    dir = Direction.UP
        elif self.y == self.world.width - 1:
            if self.x == 0:  # top right corner
                temp = randrange(2)
                if temp == 0:
                    dir = Direction.DOWN
                elif temp == 1:
                    dir = Direction.LEFT
            elif self.x == self.world.height - 1:  # bottom right corner
                temp = randrange(2)
                if temp == 0:
                    dir = Direction.UP
                elif temp == 1:
                    dir = Direction.LEFT
            else:
                temp = randrange(3)
                if temp == 0:
                    dir = Direction.DOWN
                elif temp == 1:
                    dir = Direction.LEFT
                elif temp == 2:
                    dir = Direction.UP
        elif self.x == 0:
            temp = randrange(3)
            if temp == 0:
                dir = Direction.RIGHT
            elif temp == 1:
                dir = Direction.LEFT
            elif temp == 2:
                dir = Direction.DOWN
        elif self.x == self.world.height - 1:
            temp = randrange(3)
            if temp == 0:
                dir = Direction.UP
            elif temp == 1:
                dir = Direction.LEFT
            elif temp == 2:
                dir = Direction.RIGHT
        else:
            dir = super().RandDir()
        return dir

    def Move(self, _dir):
        if _dir == Direction.UP:
            if self.x == 0:
                return
            else:
                self.world.board[self.y][self.x - 1] = self.world.board[self.y][self.x]
                self.world.board[self.y][self.x] = Ground()
                self.x -= 1
                return
        elif _dir == Direction.DOWN:
            if self.x == self.world.height - 1:
                return
            else:
                self.world.board[self.y][self.x + 1] = self.world.board[self.y][self.x]
                self.world.board[self.y][self.x] = Ground()
                self.x += 1
                return
        elif _dir == Direction.LEFT:
            if self.y == 0:
                return
            else:
                self.world.board[self.y - 1][self.x] = self.world.board[self.y][self.x]
                self.world.board[self.y][self.x] = Ground()
                self.y -= 1
                return
        elif _dir == Direction.RIGHT:
            if self.y == self.world.width - 1:
                return
            else:
                self. world.board[self.y + 1][self.x] = self.world.board[self.y][self.x]
                self.world.board[self.y][self.x] = Ground()
                self.y += 1
                return

    def GetSign(self):
        return 'A'

    def Color(self):
        return "red"

    def Split(self):
        print("why i am here?")

    def Collision(self, _collider):
        if _collider.GetSign() == self.GetSign():
            self.Split()
        elif _collider.power > self.power:
            self.world.Log(_collider.GetSign() + " kills " + self.GetSign())
            self.world.board[self.y][self.x] = Ground()
        else:
            self.world.Log(self.GetSign() + " kills " + _collider.GetSign())
            self.world.board[_collider.y][_collider.x] = Ground()


