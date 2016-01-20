from tkinter import Tk

from gui import DrawingFrame
from controller import Controller


# Main function.
def main():
    # Create GUI Frame
    root = Tk()
    drawing_frame = DrawingFrame(root)
    frame_width = 1920
    frame_height = 1200
    root.geometry(str(frame_width)+'x'+str(frame_height)+'+0+0')

    drawing_frame.draw_frame()

    # Initializes Controller class.
    #controller = Controller(frame_width, frame_heigth)

    # Starts loop after 5 seconds.
    #root.after(500, controller.run())
    root.mainloop()

# Calls main function when the main module is run.
if __name__ == '__main__':
    main()

