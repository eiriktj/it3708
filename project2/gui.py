from tkinter import Canvas, Frame, BOTH


class DrawingFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title('')
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.configure(background='#181818')
        self.canvas.pack(fill=BOTH, expand=1)

    def draw(self):

