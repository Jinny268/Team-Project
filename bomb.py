import pygame
import random

bomb_image = pygame.image.load('src/bomb.png')
bomb_shadow = pygame.image.load('src/bomb_shadow.png')

bomb_rotate = [0, 0, 0, 0]


def transformImage(image, scale, rotate):
    transScale = pygame.transform.scale(image, scale)
    return pygame.transform.rotate(transScale, rotate)


def createBomb(width, height):
    posX = random.randint(0, width)  # 떨어질 X좌표
    posY = random.randint(30, height - 200)  # 떨어질 Y좌표
    rect = pygame.Rect(bomb_image.get_rect())
    rect.top = posY - 200  # 200 위부터 시작
    rect.left = posX
    speed = random.randint(3, 9)  # 속도
    shadow = pygame.Rect(bomb_shadow.get_rect())  # 폭탄 그림자
    shadow.top = posY
    shadow.left = posX
    # 떨어지는 효과
    scale = (0, 0)
    rotate = 0
    return {'rect': rect, 'x': posX, 'y': posY, 'scale': scale, 'speed': speed, 'shadow': shadow, 'rotate': rotate}


def bomb_MoveEffect(bomb):
    bomb['rect'].top += bomb['speed']
    sc = (200 - ((bomb['y'] - bomb['rect'].top) if bomb['rect'].top < bomb['y'] else 200)) // 4
    bomb['scale'] = (sc, sc)
    bomb['rect'].left = bomb['x'] + ((50 - sc) / 2)
    bomb['shadow'].top = bomb['y'] + ((50 - sc) / 2)
    bomb['shadow'].left = bomb['x'] + ((50 - sc) / 2)
    bomb['rotate'] = (bomb['rotate'] + 1) % 3
    return bomb


def changeExplosion(bomb):
    bomb['rect'].top = bomb['y']-25
    bomb['rect'].left = bomb['x']-25
    return {'rect': bomb['rect'], 'cnt': 0}


def explosionImage(cnt): # 폭발 이미지
    return pygame.transform.scale(pygame.image.load('src/bomb_explosion' + str(cnt // 3 + 1) + '.png'), (100, 100))
