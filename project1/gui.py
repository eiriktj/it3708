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
    # drawn, r is radius of circle, d is direction of boid.
    def draw_boid(self, x, y, s, r, d):
        #self.boid_figures.append(self.canvas.create_oval(x, y, x+s, y+s, fill='blue'))
        self.canvas.create_oval(x, y, x+s, y+s, fill='blue')
        start_x = x+r+d[0]*r*0.8
        start_y = y+r+d[1]*r*0.8
        self.canvas.create_line(start_x, start_y, start_x+d[0]*r,
                start_y+d[1]*r, fill='blue')

    def move_figure(self, i, x_length, y_length):
        self.canvas.move(self.boid_figures[i], x_length, y_length)

