from animal import Animal
from direction import Direction
from ground import Ground


class Sheep(Animal):
    def __init__(self, _world, _x, _y, _age=0, _init=4, _power=4):
        super(Sheep, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'O'

    def Color(self):
        return "brown"

    def Split(self):
        dir = super().RandDir()
        if dir == Direction.UP and self.x > 0 or \
            dir == Direction.DOWN and self.x < self.world.height - 1 or \
            dir == Direction.RIGHT and self.y < self.world.width - 1 or \
            dir == Direction.LEFT and self.y > 0:
            if isinstance(super().Next(dir, 1), Ground):
                if dir == Direction.UP:
                    self.world.ToAdd(Sheep(self.world, self.x-1, self.y))
                    return
                elif dir == Direction.DOWN:
                    self.world.ToAdd(Sheep(self.world, self.x+1, self.y))
                    return
                elif dir == Direction.RIGHT:
                    self.world.ToAdd(Sheep(self.world, self.x, self.y+1))
                    return
                elif dir == Direction.LEFT:
                    self.world.ToAdd(Sheep(self.world, self.x, self.y-1))
                    return
