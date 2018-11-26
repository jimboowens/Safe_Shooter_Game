import pygame

class Hero(object):
    def __init__(self):
        self.x = 96
        self.y = 96
        self.speed = 8
        self.should_move_up = False
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False
        self.has_weapon = True
    def should_move (self, direction, start = True):
        if direction == "up":
            self.should_move_up = start
        elif direction == "down":
            self.should_move_down = start
        if direction == "left":
            self.should_move_left = start
        elif direction == "right":
            self.should_move_right = start
    def draw_me(self):
        if self.should_move_up and self.y>=0:
            self.y -= self.speed
        elif self.should_move_down and self.y<=464:
            self.y += self.speed
        if self.should_move_left and self.x<=488:
            self.x += self.speed
        elif self.should_move_right and self.x>=8:
            self.x -= self.speed
    