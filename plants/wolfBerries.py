from random import randrange

from direction import Direction
from plants.grass import Grass


class WolfBerries(Grass):
    def __init__(self,  _world=None, _x=None, _y=None, _age=0, _init=0, _power=99):
        super(WolfBerries, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'J'

    def Color(self):
        return "dark slate blue"

    def Divide(self, _chances):
        if len(_chances) == 0:
            return
        else:
            for i in range(randrange(len(_chances))):
                _chances.pop(0)
            if _chances[0] == Direction.UP:
                self.world.ToAdd(WolfBerries(self.world, self.x-1, self.y))
            elif _chances[0] == Direction.DOWN:
                self.world.ToAdd(WolfBerries(self.world, self.x+1, self.y))
            elif _chances[0] == Direction.RIGHT:
                self.world.ToAdd(WolfBerries(self.world, self.x, self.y + 1))
            elif _chances[0] == Direction.LEFT:
                self.world.ToAdd(WolfBerries(self.world, self.x, self.y - 1))
