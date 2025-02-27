import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 640 // 2
y = 480 // 2
velocity = 4

horizontal = True
vertical = True

clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if horizontal:
        x += velocity
    else:
        x -= velocity

    if vertical:
        y += velocity
    else:
        y -= velocity

    if x + ball.get_width() >= 640:
        horizontal = False  
    if y + ball.get_height() >= 480:
        vertical = False 
    if x <= 0:
        horizontal = True    
    if y <= 0:
        vertical = True  

    window.fill((0, 0, 0))  
    window.blit(ball, (x, y)) 
    pygame.display.flip()

    clock.tick(60)
