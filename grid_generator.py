# grid_generator
# William Ciesialka

from PIL import Image
from grid import Grid

class GridGenerator:

    def __init__(self,image = None):
        self.image = image.convert('1')

    def setImage(self,image):
        self.image = image.convert('1')

    def genGrid(self):
        w,h = self.image.size
        g = Grid(width=w,height=h)
        for y in range(h):
            for x in range(w):
                px = self.image.getpixel((x,y))
                if px == 255:
                    g.cell(x,y).empty()
                else:
                    g.cell(x,y).live()
        return g
