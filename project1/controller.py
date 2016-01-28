from random import randint
from math import sqrt

import numpy as np

from units import Boid


class Controller():

    def __init__(self, frame_width, frame_height, drawing_frame, root):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.drawing_frame = drawing_frame
        self.root = root
        self.boids = []
        self.boid_diameter = 10.0
        for i in range(100):
            self.boids.append(Boid(randint(0, self.frame_width), randint(0,
                self.frame_height)))

        self.run()

    def run(self):
        while True:
            # Enumerate makes it possible to both get index and item of a list.
            for index, boid in enumerate(self.boids):
                self.drawing_frame.draw_oval(boid.position[0],
                        boid.position[1], self.boid_diameter)
                self.find_neighbors(index)
                boid.update_boid()

                # Boids move to other side of frame instead of outside.
                boid.position[0] %= self.frame_width
                boid.position[1] %= self.frame_height

            # Updates frame.
            self.root.update()
            # Sleep 25ms.
            self.root.after(25)
            # Delete all canvas figures.
            self.drawing_frame.canvas.delete('all')

    def find_neighbors(self, i):
        self.boids[i].neighbors = []
        for index, boid in enumerate(self.boids):
            # np.linalg.norm(a-b) finds euclidean distance between two points.
            distance = np.linalg.norm(self.boids[i].position-boid.position)
            if  (index != i) and (distance < 15*self.boid_diameter):
                self.boids[i].neighbors.append(index)


