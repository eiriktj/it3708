from tkinter import Canvas, Frame, BOTH
from random import randint


class DrawingFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title('Flying boids')
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

    # x and y coordinates of the top-left, s is sides of box which circle is
    # drawn.
    def draw_oval(self, x, y, s):
        self.canvas.create_oval(x, y, x+s, y+s, outline='blue', fill='blue', width=0)

