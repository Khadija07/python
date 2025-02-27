# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
i = 0
angle = 0
angle1 = 150
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            


    x = 320+math.cos(angle)*130-robot.get_width()/2
    y = 240+math.sin(angle)*130-robot.get_height()/2
    x1 = 320+math.cos(angle+0.628)*130-robot.get_width()/2
    y1 = 240+math.sin(angle+0.628)*130-robot.get_height()/2
    x2 = 320+math.cos(angle+1.256)*130-robot.get_width()/2
    y2 = 240+math.sin(angle+1.256)*130-robot.get_height()/2
    x3 = 320+math.cos(angle+1.884)*130-robot.get_width()/2
    y3 = 240+math.sin(angle+1.884)*130-robot.get_height()/2
    x4 = 320+math.cos(angle+2.512)*130-robot.get_width()/2
    y4 = 240+math.sin(angle+2.512)*130-robot.get_height()/2
    x5 = 320+math.cos(angle+3.14)*130-robot.get_width()/2
    y5 = 240+math.sin(angle+3.14)*130-robot.get_height()/2
    x6 = 320+math.cos(angle+3.768)*130-robot.get_width()/2
    y6 = 240+math.sin(angle+3.768)*130-robot.get_height()/2
    x7 = 320+math.cos(angle+4.396)*130-robot.get_width()/2
    y7 = 240+math.sin(angle+4.396)*130-robot.get_height()/2
    x8 = 320+math.cos(angle+5.024)*130-robot.get_width()/2
    y8 = 240+math.sin(angle+5.024)*130-robot.get_height()/2
    x9 = 320+math.cos(angle+5.652)*130-robot.get_width()/2
    y9 = 240+math.sin(angle+5.652)*130-robot.get_height()/2
    
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    window.blit(robot, (x3, y3))
    window.blit(robot, (x4, y4))
    window.blit(robot, (x5, y5))
    window.blit(robot, (x6, y6))
    window.blit(robot, (x7, y7))
    window.blit(robot, (x8, y8))
    window.blit(robot, (x9, y9))
    pygame.display.flip()


    angle += 0.01
    clock.tick(60)