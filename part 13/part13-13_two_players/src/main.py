# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")
x = 640 // 2
y = 480// 2

x1 = 640 // 2
y1 = 260

to_right = False
to_left = False
to_up = False
to_down= False

to_right_r = False
to_left_r = False
to_up_r = False
to_down_r = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
    
        #using WSAD keys, W for up, S for down, A for left, D for right        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT: 
                to_left = True
            if event.key == pygame.K_a:
                to_left_r = True
                
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_d:
                to_right_r = True
            
            if event.key == pygame.K_UP:
                to_up = True
                
            if event.key == pygame.K_w:
                to_up_r = True
            
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_s:
                to_down_r = True
                
                

        if event.type == pygame.KEYUP:
            
          
            if event.key == pygame.K_LEFT: 
                to_left = False
            if event.key == pygame.K_a:
                to_left_r = False
                
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_d:
                to_right_r = False
            
            if event.key == pygame.K_UP:
                to_up = False
                
            if event.key == pygame.K_w:
                to_up_r = False
            
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_s:
                to_down_r = False
            

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2
    if to_right_r:
        x1 += 2
    if to_left_r:
        x1 -= 2
    if to_up_r:
        y1 -= 2
    if to_down_r:
        y1 += 2
        
    #to check boundaries
        
    if x <= 0:
        x = 0
    if x + robot1.get_width() >= 640:
        x = 640 - robot1.get_width()
    if y <= 0:
        y = 0
    if y + robot1.get_height() >= 480:
        y = 480 - robot1.get_height()
        
    if x1 <= 0:
        x1 = 0
    if x1 + robot2.get_width() >= 640:
        x1 = 640 - robot2.get_width()
    if y1 <= 0:
        y1 = 0
    if y1 + robot2.get_height() >= 480:
        y1 = 480 - robot2.get_height()


    window.fill((0, 0, 0))
    window.blit(robot1, (x, y))
    window.blit(robot2, (x1, y1))
    pygame.display.flip()
    
    clock.tick(60)
