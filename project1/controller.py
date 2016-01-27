from random import randint

from units import Boid


class Controller():

    def __init__(self, frame_width, frame_height, drawing_frame, root):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.drawing_frame = drawing_frame
        self.root = root
        self.boids = []
        for i in range(100):
            self.boids.append(Boid(randint(0, self.frame_width), randint(0,
                self.frame_height)))

        self.run()

    def run(self):
        while True:
        #    for boid in self.boids:
        #        boid.updateBoid(boids)
            for boid in self.boids:
                self.drawing_frame.draw_oval(boid.position[0],
                        boid.position[1], 10)
                boid.update_boid(self.boids)

            # Updates frame.
            self.root.update()
            # Sleep 25ms.
            self.root.after(25)
            # Delete all canvas figures.
            self.drawing_frame.canvas.delete('all')

