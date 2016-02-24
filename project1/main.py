from tkinter import Tk

from gui import DrawingFrame
from controller import Controller


# Main function.
def main():
    # Create GUI Frame
    root = Tk()
    drawing_frame = DrawingFrame(root)
    frame_width = 1280
    frame_height = 800
    root.geometry(str(frame_width)+'x'+str(frame_height)+'+0+0')

    # Initializes Controller class.
    controller = Controller(frame_width, frame_height, drawing_frame, root)

    # Starts loop after 5 seconds.
    root.after(500, controller.run())
    root.mainloop()

# Calls main function when the main module is run.
if __name__ == '__main__':
    main()

