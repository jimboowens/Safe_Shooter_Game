import Hero
from math import hypot

class Arrow (object):
    def __init__(self, stringer, target):
        self.x = stringer.x
        self.y = stringer.y
        self.speed = 25
        self.aim_x = target.x
        self.aim_y = target.y
        self.damage = 2
        self.fire = False
    def fire (self, enemy):
        dx = self.x - enemy.x
        dy = self.y - enemy.y
        dist = hypot(dx,dy)
        dx = dx/dist
        dy = dy/dist
        self.x -= dx*self.speed
        self.y -= dy*self.speed
        enemy.health -= self.damage
        