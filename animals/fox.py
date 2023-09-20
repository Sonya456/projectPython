from animal import Animal
from direction import Direction
from ground import Ground


class Fox(Animal):
    def __init__(self, _world, _x, _y, _age=0, _init=7, _power=3):
        super(Fox, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'F'

    def Color(self):
        return "orange red"

    def Split(self):
        dir = super().RandDir()
        if dir == Direction.UP and self.x > 0 or \
            dir == Direction.DOWN and self.x < self.world.height - 1 or \
            dir == Direction.RIGHT and self.y < self.world.width - 1 or \
            dir == Direction.LEFT and self.y > 0:
            if isinstance(super().Next(dir, 1), Ground):
                if dir == Direction.UP:
                    self.world.ToAdd(Fox(self.world, self.x-1, self.y))
                    return
                elif dir == Direction.DOWN:
                    self.world.ToAdd(Fox(self.world, self.x+1, self.y))
                    return
                elif dir == Direction.RIGHT:
                    self.world.ToAdd(Fox(self.world, self.x, self.y+1))
                    return
                elif dir == Direction.LEFT:
                    self.world.ToAdd(Fox(self.world, self.x, self.y-1))
                    return

    def Action(self):
        dir = super().RandDir()
        if dir == Direction.UP and self.x > 0 or \
        dir == Direction.DOWN and self.x < self.world.height - 1 or \
        dir == Direction.RIGHT and self.y < self.world.width - 1 or \
        dir == Direction.LEFT and self.y > 0:
            if isinstance(super().Next(dir, 1), Ground):
                super().Move(dir)
            else:
                if super().Next(dir, 1).power < self.power:
                    super().Next(dir, 1).Collision(self)
                    if isinstance(super().Next(dir, 1), Ground):
                        super().Move(dir)
