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

    # x and y coordinates of the center of the circle, r is radius of circle, d is direction of boid.
    def draw_boid(self, x, y, r, d):
        #self.boid_figures.append(self.canvas.create_oval(x, y, x+s, y+s, fill='blue'))
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='blue')
        start_x = x+d[0]*r*0.8
        start_y = y+d[1]*r*0.8
        self.canvas.create_line(start_x, start_y, start_x+d[0]*r,
                start_y+d[1]*r, fill='blue')

    def move_figure(self, i, x_length, y_length):
        self.canvas.move(self.boid_figures[i], x_length, y_length)

