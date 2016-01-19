from units import Boid


class Controller():

    def __init__(self, frame_width, frame_heigth):
        self.frame_width = frame_width
        self.frame_heigth = frame_heigth
        self.boids = []
        for i in range(5):
            boids.append(Boid())

    def run(self):
        while True:
            for boid in self.boids:
                boid.updateBoid(boids)

