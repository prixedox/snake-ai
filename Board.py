import random

class Board:

    def __init__(self):
        self.window_x = 720
        self.window_y = 480
        self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10, 
                  random.randrange(1, (self.window_y//10)) * 10]
 
        self.fruit_spawn = True