from random import randint

import numpy as np


class Boid():

    def __init__(self, random_width, random_height):
        self.velocity = np.array([0.0, -5.0])
        self.position = np.array([random_width, random_height])
        self.neighbors = []

    def update_boid(self, boids):
        #self.neighbors = find_neighbors()

        #seperation = separation_weight * calculate_separation_force()
        #alignment = alignment_weight * calculate_alignment_force()
        #cohesion = cohesion_weight * calculate_cohesion_force()

        #self.velocity = self.velocity + separation + alignment + cohesion
        self.position = self.position + self.velocity

    #def find_neighbors(self):

