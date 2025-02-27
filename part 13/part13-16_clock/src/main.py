# WRITE YOUR SOLUTION HERE:
import pygame, math, time

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

clock = pygame.time.Clock()
hour = 16
minute = 6
second = 38
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    display.fill((0, 0, 0))
    
    #print(x,y)
    angle = 0.1047 * second - 1.5708
    
    x = 320+math.cos(angle)*180
    y = 240+math.sin(angle)*180

    pygame.draw.circle(display, (255, 0, 0), (320, 240), 200, 10)
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 10)
    pygame.draw.line(display, (0, 0, 255), (320, 240), (450, 120), 2)
    pygame.draw.line(display, (0, 0, 255), (320, 240), (450, 320), 8)
    pygame.draw.line(display, (0, 0, 255), (320, 240), (x,y), 2)

    pygame.display.flip()
    
    second += 1
    if second == 59:
        second = 38
    pygame.display.set_caption(f"{hour}:{minute:02}:{second}")

    clock.tick(1)

