from random import random
from math import pi
from math import cos
from math import sin

import numpy as np


class Boid():

    def __init__(self, random_width, random_height):
        random_direction = random()*2*pi
        self.direction = np.array([cos(random_direction), sin(random_direction)])
        self.velocity = 5*self.direction
        self.position = np.array([random_width, random_height])
        self.neighbors = []
        self.separation = 0
        self.alignment = 0
        self.cohesion = 0

    def update_boid(self):
        #seperation = separation_weight * calculate_separation_force()
        #alignment = alignment_weight * calculate_alignment_force()
        #cohesion = cohesion_weight * calculate_cohesion_force()

        #self.velocity += self.separation + self.alignment + self.cohesion
        self.position += self.velocity

