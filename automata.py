# automate
# William Ciesialka

from cell import Cell
from grid import Grid
from cell_types import CellType
from grid_generator import GridGenerator
from PIL import Image
import tkinter as tk
from math import floor
from tkinter import filedialog

root = tk.Tk()
root.title("Conway's Game of Life Cellular Automata")

class Automata(tk.Canvas):

    RULES = "If a cell is alive and has less than 2 alive cells neighboring it, it will die from underpopulation.\nIf a cell is alive and has over 3 alive cells neighboring it, it will die from overpopulation.\nIf a cell is dead or empty and has exactly three alive cells neighboring it, it will live again from reproduction."

    def __init__(self,master=None,grid=None,resolution=5):
        super().__init__(master=master, width = grid.width*resolution, height = grid.height*resolution)
        self.grid = grid
        self.resolution = resolution
        self.pack()

    def mainloop(self):
        self.shouldRun = True
        while self.shouldRun:
            for loc in self.grid.cells:
                cell = self.grid.cells[loc]
                x = cell.x*self.resolution
                ex = x+(self.resolution-1)
                y = cell.y*self.resolution
                ey = y+(self.resolution-1)
                box = (x,y,ex,ey)
                self.create_rectangle(box,fill=cell.color(),outline="")
            self.master.update()
            self.delete()
            self.grid.update()

    def delete(self):
        super().delete()
        
def main():
    ALLOWED = (("Image",("*.png","*.jpg","*.gif","*.jpeg","*.bmp")),("All Files","*.*"))
    fn = ""
    while(not fn):
        fn = filedialog.askopenfilename(defaultextension=".jpg",filetypes=ALLOWED, parent=root, title="Choose Image", initialdir="/")
 
    img = Image.open(fn)
    gridGen = GridGenerator(img)
    grid = gridGen.genGrid()
    res = floor(450/max(img.size))
    automata = Automata(master=root,grid=grid,resolution=res)
    automata.mainloop()

if __name__ == "__main__":
    main()
