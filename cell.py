# cell
# William Ciesialka

from cell_types import CellType

class Cell:
    
    def __init__(self,state=CellType.EMPTY,x=0,y=0,left=None,above=None,right=None,below=None):
        self.state = state
        self.nextState = None
        self.above = above
        self.left = left
        self.right = right
        self.below = below
        self.x = x
        self.y = y

    def __str__(self):
        return (f"{self.state} @ ({self.x},{self.y})")

    def live(self):
        self.state = CellType.ALIVE

    def die(self):
        self.state = CellType.DEAD

    def empty(self):
        self.state = CellType.EMPTY

    def isDead(self):
        return self.state is CellType.DEAD

    def isAlive(self):
        return self.state is CellType.ALIVE

    def isEmpty(self):
        return self.state is CellType.EMPTY

    def exists(self):
        return self != None

    def color(self):
        if self.isDead():
            return '#FF0000'
        elif self.isAlive():
            return '#00FF00'
        elif self.isEmpty():
            return '#FFFFFF'
        else:
            return '#000000'

    def queue_state(self,state):
        self.nextState = state

    def finish_queue(self):
        if self.nextState != None:
            self.state = self.nextState
            self.nextState = None

    def count_alive_neighbors(self):
        count = 0

        if self.above != None:
            if self.above.isAlive():
                count+=1
            if self.above.left != None:
                if self.above.left.isAlive():
                    count += 1
            if self.above.right != None:
                if self.above.right.isAlive():
                    count += 1
        if self.below != None:
            if self.below.isAlive():
                count += 1
            if self.below.left != None:
                if self.below.left.isAlive():
                    count += 1
            if self.below.right != None:
                if self.below.right.isAlive():
                    count += 1
        if self.left != None:
            if self.left.isAlive():
                count += 1
        if self.right != None:
            if self.right.isAlive():
                count += 1

        return count

    def update(self):
        n_alive = self.count_alive_neighbors()

        if self.isAlive() and n_alive < 2:
            self.queue_state(CellType.DEAD)
        elif self.isAlive() and (n_alive == 2 or n_alive == 3):
            pass
        elif self.isAlive() and n_alive > 3:
            self.queue_state(CellType.DEAD)
        elif (self.isDead() or self.isEmpty()) and n_alive == 3:
            self.queue_state(CellType.ALIVE)

    def setLeft(self,cell):
        self.left = cell
        self.x = cell.x + 1
        self.y = cell.y
        if cell.right != self:
            cell.setRight(self)

    def setRight(self,cell):
        self.right = cell
        self.x = cell.x - 1
        self.y = cell.y
        if cell.left != self:
            cell.setLeft(self)

    def setAbove(self,cell):
        self.above = cell
        self.x = cell.x
        self.y = cell.y + 1
        if cell.below != self:
            cell.setBelow(self)

    def setBelow(self,cell):
        self.below = cell
        self.x = cell.x
        self.y = cell.y - 1
        if cell.above != self:
            cell.setAbove(self)
