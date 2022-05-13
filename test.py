import pygame  # 파이 게임 모듈 임포트
import random

pygame.init()  # 파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 화면 크기 설정
clock = pygame.time.Clock()

# 변수
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

bombs = []  # 폭탄들을 저장할 변수
bomb_image = pygame.image.load('bomb.png')
bomb_shadow = pygame.image.load('shadow.png')
bomb_rotate = [30, 0, -30, 0]


def transformImage(image, scale, rotate):
    transScale = pygame.transform.scale(image, scale)
    return pygame.transform.rotate(transScale, rotate)


def createBomb():
    posX = random.randint(0, SCREEN_WIDTH)  # 떨어질 X좌표
    posY = random.randint(30, SCREEN_HEIGHT - 200)  # 떨어질 Y좌표
    rect = pygame.Rect(bomb_image.get_rect())
    rect.top = posY - 200  # 100 위부터 시작
    rect.left = posX
    speed = random.randint(3, 7)  # 속도
    shadow = pygame.Rect(bomb_shadow.get_rect())  # 그림자
    shadow.top = posY
    shadow.left = posX
    scale = (0, 0)
    rotate = 0
    return {'rect': rect, 'x': posX, 'y': posY, 'scale': scale, 'speed': speed, 'shadow': shadow, 'rotate': rotate}


for _ in range(5):
    bombs.append(createBomb())

while True:  # 게임 루프
    screen.fill(WHITE)  # 단색으로 채워 화면 지우기

    # 변수 업데이트
    event = pygame.event.poll()  # 이벤트 처리
    if event.type == pygame.QUIT:
        break

    # bomb start ----------------------------------------
    for bomb in bombs:
        bomb['rect'].top += bomb['speed']
        sc = (200 - ((bomb['y'] - bomb['rect'].top) if bomb['rect'].top < bomb['y'] else 200)) // 4
        bomb['scale'] = (sc, sc)
        bomb['rect'].left = bomb['x'] + ((50 - sc) / 2)
        bomb['shadow'].top = bomb['y'] + ((50 - sc) / 2)
        bomb['shadow'].left = bomb['x'] + ((50 - sc) / 2)

        bomb['rotate'] = (bomb['rotate'] + 1) % 3

        if bomb['rect'].top > bomb['y']:
            bombs.remove(bomb)
            bombs.append(createBomb())

    for bomb in bombs:
        screen.blit(transformImage(bomb_shadow, bomb['scale'], bomb_rotate[bomb['rotate']]), bomb['shadow'])
        screen.blit(transformImage(bomb_image, bomb['scale'], bomb_rotate[bomb['rotate']]), bomb['rect'])
        # bomb end ----------------------------------------

    pygame.display.update()  # 모든 화면 그리기 업데이트
    clock.tick(30)  # 30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값
