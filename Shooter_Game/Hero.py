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
    def should_move (self, direction):
        if direction == "up":
            self.should_move_up = True
        if direction == "down":
            self.should_move_down = True
        if direction == "left":
            self.should_move_left = True
        if direction == "right":
            self.should_move_right = True
