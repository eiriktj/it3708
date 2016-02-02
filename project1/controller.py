from random import random
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
        self.boid_radius = self.boid_diameter/2
        self.neighbor_radius = 15*self.boid_diameter
        self.separation_weight=1.0
        self.alignment_weight=1.0
        self.cohesion_weight=1.0
        #Create boids and paint them on the frame.
        for i in range(100):
            self.boids.append(Boid(random()*self.frame_width, random()*self.frame_height))
            self.drawing_frame.draw_boid(self.boids[-1].position[0],
                    self.boids[-1].position[1], self.boid_diameter,
                    self.boid_radius, self.boids[-1].direction)

        self.run()

    def run(self):
        while True:
            # Calculate new forces for each boid
            for index in range(len(self.boids)):
                self.find_neighbors(index)
                self.calculate_separation_force(index)
                self.calculate_alignment_force(index)
                self.calculate_cohesion_force(index)

            # Update the position of each boid.
            for boid in self.boids:
                boid.update_boid()

                # Boids move to other side of frame instead of outside.
                boid.position[0] %= self.frame_width
                boid.position[1] %= self.frame_height
                self.drawing_frame.draw_boid(boid.position[0],
                        boid.position[1], self.boid_diameter, self.boid_radius,
                        boid.direction)
                #self.drawing_frame.move_figure(index, boid.velocity[0], boid.velocity[1])

            # Updates frame.
            self.root.update()
            # Sleep 25ms.
            # self.root.after(25)
            # Delete all canvas figures.
            self.drawing_frame.canvas.delete('all')

    def find_neighbors(self, i):
        # Remove old neighbors.
        self.boids[i].neighbors = []
        # Enumerate makes it possible to both get index and item of a list.
        for index, boid in enumerate(self.boids):
            # np.linalg.norm(a-b) finds euclidean distance between two points.
            distance = np.linalg.norm(self.boids[i].position-boid.position)
            if (index != i) and (distance < 15*self.boid_diameter):
                self.boids[i].neighbors.append(index)

    def calculate_separation_force(self, i):
        self.boids[i].separation = np.array([0.0, 0.0])
        for neighbor in self.boids[i].neighbors:
            self.boids[i].separation -= (self.boids[i].position - 
                                         self.boids[neighbor].position)
        magnitude = np.linalg.norm(self.boids[i].separation) 
        if magnitude > 0:
            self.boids[i].separation /= magnitude

    def calculate_alignment_force(self, i):
        self.boids[i].alignment = np.array([0.0, 0.0])
        for neighbor in self.boids[i].neighbors:
            self.boids[i].alignment += self.boids[neighbor].direction
        magnitude = np.linalg.norm(self.boids[i].alignment) 
        if magnitude > 0:
            self.boids[i].alignment /= magnitude

    def calculate_cohesion_force(self, i):
        self.boids[i].cohesion = np.array([0.0, 0.0])
        for neighbor in self.boids[i].neighbors:
            self.boids[i].cohesion += self.boids[neighbor].position
        if len(self.boids[i].neighbors) > 1:
            self.boids[i].cohesion /= len(self.boids[i].neighbors)
        magnitude = np.linalg.norm(self.boids[i].cohesion) 
        if magnitude > 0:
            self.boids[i].cohesion /= magnitude

