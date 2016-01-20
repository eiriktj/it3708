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

    def draw_frame(self):
        for i in range(100):
            rw = randint(0, 1920)
            rh = randint(0, 1200)
            self.canvas.create_oval(rw, rh, rw+20, rh-20, outline='blue', fill='blue',
                    width=0)
        self.canvas.pack(fill=BOTH, expand=1)

