# cell_types
# William Ciesialka

from enum import Enum

class CellType(Enum):
    EMPTY = 0
    ALIVE = 1
    DEAD = 2

    def __str__(self):
        return self.name

    def nick(self):
        v = self.value
        if v == self.EMPTY.value:
            return 'E'
        elif v == self.ALIVE.value:
            return 'A'
        elif v == self.DEAD.value:
            return 'D'
        else:
            return 'X'
