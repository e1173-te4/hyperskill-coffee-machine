class Sphere:
    # finish class Sphere here
    PI = 3.1415
    def __init__(self, r):
        self.radius = r
        self.volume = 4 * self.PI * self.radius ** 3 / 3
