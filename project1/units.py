from random import random
from math import pi
from math import cos
from math import sin

import numpy as np


class Boid():

    def __init__(self, random_width, random_height):
        random_direction = random()*2*pi
        self.direction = np.array([cos(random_direction), sin(random_direction)])
        self.velocity = 2*self.direction
        self.position = np.array([random_width, random_height])
        self.neighbors = []
        self.separation = np.array([0.0, 0.0])
        self.alignment = np.array([0.0, 0.0])
        self.cohesion = np.array([0.0, 0.0])
        self.separation_weight = 1.0
        self.alignment_weight = 1.0
        self.cohesion_weight = 1.0
        self.velocity_limit = 5.0

    def update_boid(self):
        #seperation = self.separation_weight * calculate_separation_force()
        alignment = self.alignment_weight * self.alignment
        #cohesion = self.cohesion_weight * calculate_cohesion_force()

        #self.velocity += self.separation + self.alignment + self.cohesion

        self.velocity += self.alignment
        # np.linalg.norm calculates the magnitude of the vector.
        velocity_magnitude = np.linalg.norm(self.velocity)
        self.direction = self.velocity/velocity_magnitude
        if velocity_magnitude > self.velocity_limit:
            self.velocity = self.direction*self.velocity_limit

        self.position += self.velocity

