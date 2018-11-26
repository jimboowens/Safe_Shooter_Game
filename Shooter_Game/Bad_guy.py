from math import hypot

class Bad_guy(object):
    def __init__(self):
        self.x = 200
        self.y = 200
        self.speed = 1
        self.has_weapon = False
        self.health = 10
    def update_me(self, enemy):
        dx = self.x - enemy.x
        dy = self.y - enemy.y
        dist = hypot(dx,dy)
        dx = dx/dist
        dy = dy/dist
        self.x -= dx*self.speed
        self.y -= dy*self.speed