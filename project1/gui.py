from tkinter import Canvas, Frame, BOTH
from random import randint


class DrawingFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.boid_figures = []
        self.init_ui()

    def init_ui(self):
        self.parent.title('Flying boids')
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.configure(background='#181818')
        self.canvas.pack(fill=BOTH, expand=1)

    # x and y coordinates of the top-left, s is sides of box which circle is
    # drawn.
    def draw_oval(self, x, y, s):
        #self.boid_figures.append(self.canvas.create_oval(x, y, x+s, y+s, fill='blue'))
        self.canvas.create_oval(x, y, x+s, y+s, fill='blue')

    def move_figure(self, i, x_length, y_length):
        self.canvas.move(self.boid_figures[i], x_length, y_length)

