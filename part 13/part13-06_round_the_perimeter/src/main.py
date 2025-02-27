# # WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")


x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()
t = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if t==0:
        y += velocity
        if velocity > 0 and y+robot.get_height() >= 480:
            velocity = -velocity
            t = 1
            
        if velocity < 0 and y <= 0:
            velocity = 1
            t = 1
        
            
    if t==1:
        x += velocity
        if velocity > 0 and x+robot.get_width() >= 640:
            velocity = 1
            y = 0
            t = 0
        
        if velocity < 0 and x <= 0:
            velocity = -1
            t = 0
        
        

    

    clock.tick(60)