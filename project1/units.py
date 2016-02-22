from random import random
from math import pi
from math import cos
from math import sin

import numpy as np


class Boid():

    def __init__(self, random_width, random_height):
        random_direction = random()*2*pi
        self.direction = np.array([cos(random_direction), sin(random_direction)])
        self.velocity = 20*self.direction
        self.position = np.array([random_width, random_height])
        self.neighbors = []
        self.separation = np.array([0.0, 0.0])
        self.alignment = np.array([0.0, 0.0])
        self.cohesion = np.array([0.0, 0.0])
        self.velocity_limit = 30.0

    def update_boid(self, separation_weight, alignment_weight, cohesion_weight):
        self.separation *= separation_weight
        self.alignment *= alignment_weight
        self.cohesion *= cohesion_weight
        self.velocity += self.separation + self.alignment + self.cohesion
        # np.linalg.norm calculates the magnitude of the vector.
        velocity_magnitude = np.linalg.norm(self.velocity)
        if velocity_magnitude > 0:
            self.direction = self.velocity/velocity_magnitude
        if velocity_magnitude > self.velocity_limit:
            self.velocity = self.direction*self.velocity_limit

        self.position += self.velocity

