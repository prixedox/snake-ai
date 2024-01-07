# importing libraries
import pygame
import time
import random
from Snake import Snake

snake = Snake()
 
snake_speed = 15
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()

# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# initial score
score = 0
 
# displaying Score function
def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over():
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_to = 'UP'
            if event.key == pygame.K_DOWN:
                snake.change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                snake.change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake.change_to = 'RIGHT'
 
# Main Function
while True:
     
    # handling key events
    handle_input()
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two 
    # directions simultaneously
    snake.change_direction()
 
    # Moving the snake
    snake.move()
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake.body.insert(0, list(snake.position))
    if snake.position[0] == fruit_position[0] and snake.position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake.body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake.body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake.position[0] < 0 or snake.position[0] > window_x-10:
        game_over()
    if snake.position[1] < 0 or snake.position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake.body[1:]:
        if snake.position[0] == block[0] and snake.position[1] == block[1]:
            game_over()
 
    # displaying score continuously
    show_score(1, white, 'times new roman', 20)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)