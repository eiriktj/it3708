from random import random
from math import sqrt
import multiprocessing as mp

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
        self.neighbor_radius = 5*self.boid_diameter
        self.separation_weight=1.0
        self.alignment_weight=0.125
        self.cohesion_weight=0.01
        #Create boids.
        for i in range(100):
            self.boids.append(Boid(random()*self.frame_width, random()*self.frame_height))
        self.run()

    def run(self):
        while True:
            #p1 = mp.Process(target=self.draw_boids)
            #p2 = mp.Process(target=self.calculate_forces)
            self.draw_boids()
            self.calculate_forces()

            #p1.start()
            #p2.start()
            #p1.join()
            #p2.join()

            # Update the position of each boid.
            for boid in self.boids:
                boid.update_boid(self.separation_weight, self.alignment_weight,
                                 self.cohesion_weight)

                # Boids move to other side of frame instead of outside.
                boid.position[0] %= self.frame_width
                boid.position[1] %= self.frame_height

            # Updates frame.
            self.root.update()
            # Sleep 25ms.
            # self.root.after(25)
            # Delete all canvas figures.
            self.drawing_frame.canvas.delete('all')

    def draw_boids(self):
        # Paint the boids on the frame.
        for boid in self.boids:
            self.drawing_frame.draw_boid(boid.position[0], boid.position[1], self.boid_radius, boid.direction)

    def calculate_forces(self):
        # Find neighbors and calculate new forces for each boid
        for index in range(len(self.boids)):
            self.find_neighbors(index)
            if len(self.boids[index].neighbors) > 0:
                self.calculate_separation_force(index)
                self.calculate_alignment_force(index)
                self.calculate_cohesion_force(index)

    def find_neighbors(self, index):
        # Remove old neighbors.
        self.boids[index].neighbors = []
        # Enumerate makes it possible to both get index and item of a list.
        for boid_index, boid in enumerate(self.boids):
            # np.linalg.norm(a-b) finds euclidean distance between two points.
            distance = np.linalg.norm(self.boids[index].position-boid.position)
            if (boid_index != index) and (distance < self.neighbor_radius):
                self.boids[index].neighbors.append(boid_index)

    def calculate_separation_force(self, index):
            self.boids[index].separation = np.array([0.0, 0.0])
            for neighbor in self.boids[index].neighbors:
                self.boids[index].separation -= (self.boids[neighbor].position - 
                                         self.boids[index].position)

    def calculate_alignment_force(self, index):
            self.boids[index].alignment = np.array([0.0, 0.0])
            for neighbor in self.boids[index].neighbors:
                self.boids[index].alignment += self.boids[neighbor].velocity

    def calculate_cohesion_force(self, index):
            self.boids[index].cohesion = np.array([0.0, 0.0])
            for neighbor in self.boids[index].neighbors:
                self.boids[index].cohesion += self.boids[neighbor].position
                self.boids[index].cohesion /= len(self.boids[index].neighbors)
                self.boids[index].cohesion -= self.boids[index].position

