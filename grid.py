# grid
# William Ciesialka

from cell import Cell

class Grid:
    
    def __init__(self,width=100,height=100):
        self.width = width
        self.height = height
        self.cells = {}
        self.fill_grid()

    def getCell(self,x,y):
        return self.cells[f"{x},{y}"]

    def cell(self,x,y):
        return self.getCell(x,y)

    def setCell(self,x,y,cell):
        self.cells[f"{x},{y}"] = cell

    def fill_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                self.setCell(x,y, Cell(x=x,y=y))
        self.link_cells()

    def offset_cell(self,cell,x=0,y=0):
        cX = cell.x
        cY = cell.y
        try:
            c = self.cell(cX+x,cY+y)
        except:
            c = None
        finally:
            return c

    def link_cells(self):
        for loc in self.cells:
            cell = self.cells[loc]
            x = cell.x
            y = cell.y
            above = self.offset_cell(cell,y=1)
            below = self.offset_cell(cell,y=-1)
            left = self.offset_cell(cell,x=-1)
            right = self.offset_cell(cell,x=1)
            if above != None:
                cell.setAbove(above)
            if below != None:
                cell.setBelow(below)
            if left != None:
                cell.setLeft(left)
            if right != None:
                cell.setRight(right)

    def update(self):
        for loc in self.cells:
            self.cells[loc].update()
        for loc in self.cells:
            self.cells[loc].finish_queue()

    def __str__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += self.cell(x,y).state.nick()
            s += "\n"
        return s
