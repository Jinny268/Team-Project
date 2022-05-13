# 메소드(9팀) - 팀 프로젝트

from turtle import done
import pygame
import random
from bomb import *

# 게임판 구성
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def runGame():
    bombs = []  # 폭탄들을 저장할 변수
    explosion = []  # 폭파 지점

    for _ in range(2):  # 처음 폭탄 수
        bombs.append(createBomb(SCREEN_WIDTH, SCREEN_HEIGHT))

    run = True

    while run:
        screen.fill((255, 255, 255))
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # bomb ----------
        for bomb in bombs:
            bomb = bomb_MoveEffect(bomb)
            if bomb['rect'].top > bomb['y']:
                explosion.append(changeExplosion(bomb))
                bombs.remove(bomb)
                bombs.append(createBomb(SCREEN_WIDTH, SCREEN_HEIGHT))

        for bomb in bombs:
            screen.blit(transformImage(bomb_shadow, bomb['scale'], bomb_rotate[bomb['rotate']]), bomb['shadow'])
            screen.blit(transformImage(bomb_image, bomb['scale'], bomb_rotate[bomb['rotate']]), bomb['rect'])
        for exp in explosion:
            screen.blit(explosionImage(exp['cnt']), exp['rect'])
            exp['cnt'] += 1
            if exp['cnt'] >= 15:
                explosion.remove(exp)
        # --------------

        pygame.display.update()
    pygame.quit()


runGame()
