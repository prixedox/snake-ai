class Snake:
    
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
        self.direction = 'RIGHT'
        self.change_to = 'RIGHT'

    def change_direction(self):
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
    
    def move(self):
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10