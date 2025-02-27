import pygame
import random

pygame.init()

width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot_img = pygame.image.load("robot.png")
robot_width, robot_height = robot_img.get_size()

# Falling robots list
falling_robot_list = []

clock = pygame.time.Clock()

# Create new falling robot
def create_robot():
    x = random.randint(0, width - robot_width)
    y = -robot_height
    velocity = 1
    falling_robot_list.append([x, y, velocity, random.choice([-1, 1]), False])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
    window.fill((0, 0, 0))
    
    # Create new robots at intervals
    if random.randint(1, 60) == 1:
        create_robot()

    # Update positions of falling robots
    for robot in falling_robot_list:
        
        if not robot[4]:  # If robot is still falling
            robot[1] += robot[2]
            if robot[1] > height - robot_height:
                robot[4] = True  # Robot has hit the ground
        else:
            if robot[0] <width//2:
                robot[3] = -1
                robot[0] += robot[3] * robot[2]  # Move left
            else:
                robot[3] = 1
                robot[0] += robot[3] * robot[2]  # Move right
            if robot[0] < -robot_width or robot[0] > width:
                falling_robot_list.remove(robot)  # Remove robot when off screen
            #print(robot[0], "\t", robot[1],"\t", robot[2],"\t",robot[3],'\t',robot[4])

    # Drawing robots
    for robot in falling_robot_list:
        window.blit(robot_img, (robot[0], robot[1]))

    

    pygame.display.flip()
    clock.tick(60)
