# Complete your game here
import pygame, random, sys, time

class COIN:
    #Target of this game: Robot has to collect all the randomly generated coins within 10 seconds. 
    
    def __init__(self):
        pygame.init()
        self.won = False
        self.monster = False
        self.load_images()
        self.new_game()
        self.scores = 0
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()
        cell_size = 80
        
        #time starts
        self.last_move_time = time.time()
        
        window_width = cell_size * len(self.map[0])  
        window_height = cell_size * len(self.map) 

        # self.window = pygame.display.set_mode((window_width, window_height))
        self.window = pygame.display.set_mode((window_width+10, window_height+50))

        self.game_font = pygame.font.SysFont("Arial", 24)

        pygame.display.set_caption("Coin Quest")

        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["coin", "door", "robot", "monster"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):

        # self.map = [[0, 0, 0, 1, 0, 1, 0, 3, 0],
        #             [0, 1, 0, 3, 0, 0, 0, 0, 0],
        #             [3, 0, 0, 0, 3, 1, 0, 3, 0],
        #             [0, 1, 0, 0, 0, 0, 0, 0, 0],
        #             [2, 0, 0, 3, 0, 1, 0, 3, 0]]
        
        #most of the coins are generated randomly, only few coins are fixed to ensure that there aren’t too few coins available at any given time.
        self.map = [[random.choice([0,-1]), random.choice([0,-1]), random.choice([0,-1]), 1, random.choice([0,-1]), 1, random.choice([0,-1]), 3, random.choice([0,-1])],
                    [random.choice([0,-1]), 1, random.choice([0,-1]), 3, random.choice([0,-1]), 0, random.choice([0,-1]), random.choice([0,-1]), random.choice([0,-1])],
                    [3, random.choice([0,-1]), random.choice([0,-1]), 0, 3, 1, random.choice([0,-1]), 3, random.choice([0,-1])],
                    [random.choice([0,-1]), 1, 0, random.choice([0,-1]), random.choice([0,-1]), random.choice([0,-1]), 0, random.choice([0,-1]), random.choice([0,-1])],
                    [2, random.choice([0,-1]), 0, 3, random.choice([0,-1]), 1, random.choice([0,-1]), 3, random.choice([0,-1])]]
        self.coins = sum(row.count(0) for row in self.map)
        
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            
    def find_robot(self ):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 2:
                    return (y, x)

    def check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    self.play(0,-1)
                if event.key == pygame.K_RIGHT:
                    self.play(0,1)
                if event.key == pygame.K_UP:
                    self.play(-1,0)
                if event.key == pygame.K_DOWN:
                    self.play(1,0)
            if event.type == pygame.QUIT:
                exit()
                
    def play(self, play_y, play_x):
        robot_old_y, robot_old_x = self.find_robot() 
        robot_new_y = robot_old_y + play_y
        robot_new_x = robot_old_x + play_x
        
        #cannot exceed the perimeter
        if robot_new_x > 8 or robot_new_y > 4 or robot_new_y < 0 or robot_new_x < 0:
            return
        
        #collision with wall
        if self.map[robot_new_y][robot_new_x] == 1:
            return

        #coin collection  
        if self.map[robot_new_y][robot_new_x] == 0:
            self.scores += 1
            
            #print(self.scores)
            
        
        #collision with monster
        if self.map[robot_new_y][robot_new_x] == 3:
            
            self.monster = True

            
        self.map[robot_old_y][robot_old_x] = -1 # remove robot from old position
        self.map[robot_new_y][robot_new_x] = 2 #robot in new position
        self.check_scores()
        #self.draw_empty(robot_new_y,robot_new_x)
        
    def check_scores(self):
        if self.scores == self.coins:
            self.won = True
            return True
        return False
    

        
    def draw_window(self):
        self.window.fill((255, 255, 255))
        cell_size = 80  
         
    
        for y in range(self.height):
             for x in range(self.width):
                square = self.map[y][x]
            
            #position for each grid cell
                x_pos = x * cell_size
                y_pos = y * cell_size
                
            
            #uniform grid 
                pygame.draw.rect(self.window, (255, 255, 255), (x_pos, y_pos, cell_size, cell_size))
                if square >= 0 and square < len(self.images):
                    image = self.images[square]
                    image_width, image_height = image.get_size()
                    image_x = x_pos + (cell_size - image_width) // 2
                    image_y = y_pos + (cell_size - image_height) // 2
                    self.window.blit(image, (image_x, image_y))
                    
        
        #display scores            
        time_spent = time.time() - self.last_move_time
        if self.won == False and self.monster == False and time_spent < 10:
            
            game_text = self.game_font.render(f"Scores: {self.scores}, Time: {time_spent:.2f} seconds ", True, (0, 0, 0))
            self.window.blit(game_text, (10, self.height * self.scale + 200))
                    
        #check if won, collected all coins and took time less than 10 seconds
        if self.check_scores():
            game_text = self.game_font.render(f"Congratulations, you won!, Scored: {self.scores}, Time spent: {time_spent:.2f} seconds", True, (0, 255, 0))
            
            self.window.blit(game_text, (10, self.height * self.scale + 200))
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.quit()
            sys.exit()
        
        #check if collided with monster
        if self.monster:
            game_text = self.game_font.render(f"Collided With Monster!Game Over!", True, (255, 0, 0))
            
            self.window.blit(game_text, (10, self.height * self.scale + 200))
            pygame.display.flip()
            pygame.time.delay(1000)
            pygame.quit()
            sys.exit()
        
        #game over if time taken more than 10 seconds
        if not self.won and time.time() - self.last_move_time >= 10:
                game_text = self.game_font.render(f"Time Up!Game Over!", True, (255, 0, 0))
            
                self.window.blit(game_text, (10, self.height * self.scale + 200))
                pygame.display.flip()
                pygame.time.delay(1000)
                pygame.quit()
                sys.exit()
            

        pygame.display.flip()
        
if __name__ == "__main__":
    COIN()