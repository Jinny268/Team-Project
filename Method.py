print('메소드(9팀) - 팀 프로젝트')

import imp
from turtle import done
import pygame
import random

pygame.init()
size = [600, 900]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill((0, 200, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pygame.display.update()
       
runGame() 
pygame.quit()
               
    
