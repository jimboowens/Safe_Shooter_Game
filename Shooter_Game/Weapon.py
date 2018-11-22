import hero

class Weapon (object):
    def __init__(self, stringer, target):
        self.x = stringer.x
        self.y = stringer.y
        self.speed = 100
        self.aim_x = target.x
        self.aim_y = target.y
        self.fire = False
    def fire (self, target):
        dx = self.x - enemy.x
        dy = self.y - enemy.y
        dist = hypot(dx,dy)
        dx = dx/dist
        dy = dy/dist
        self.x -= dx*self.speed
        self.y -= dy*self.speed
        