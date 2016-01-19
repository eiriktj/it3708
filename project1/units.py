import numpy as np


class Boid():

    def __init__(self):
        self.velocity = np.array([0.0, 0.0])
        self.position = np.array([0.0, 0.0])
        self.neighbors = []

    def updateBoid(self, boids):
        self.neighbors = find_neighbors()

        seperation = separation_weight * calculate_separation_force()
        alignment = alignment_weight * calculate_alignment_force()
        cohesion = cohesion_weight * calculate_cohesion_force()

        velocity = velocity + separation + alignment + cohesion
        position = position + velocity

    def find_neighbors(self):

