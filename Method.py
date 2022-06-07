# 메소드(9팀) - 팀 프로젝트

from turtle import done
import pygame
import random
import StartScreen
import bomb
import person
import gift

# 게임판 구성
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

StartScreen.init(SCREEN_WIDTH, SCREEN_HEIGHT)
bomb.init(SCREEN_WIDTH, SCREEN_HEIGHT)
person.init(SCREEN_WIDTH, SCREEN_HEIGHT)
gift.init(SCREEN_WIDTH, SCREEN_HEIGHT)
# 배경이미지
background = pygame.transform.scale(pygame.image.load("src/bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# 추가 점수
score_add = 0

# 게임 플레이 총 시간
totalTime = 10
startTicks = pygame.time.get_ticks()

font = pygame.font.SysFont("arial", 30, True, True)
heart3 = font.render("♥ ♥ ♥", True, (0, 0, 0))
heart2 = font.render("  ♥ ♥", True, (0, 0, 0))
heart1 = font.render("    ♥", True, (0, 0, 0))

smallfont = pygame.font.SysFont("arial", 25, True, True)
pause = smallfont.render("(p) pause", True, (0, 0, 0))
restart = smallfont.render("(r) restart", True, (0, 0, 0))
exit = smallfont.render("(x) end game", True, (0, 0, 0))

screenCover = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
screenCover.set_alpha(128)
screenCover.fill((150, 150, 150))


def runGame():
    run = True

    Game_Start = 0
    heart = 0
    score = 0
    cnt = 0

    file = open('record.txt', 'r')
    records = list(map(int, file.read().split()))
    file.close()

    while run:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        dt = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # game 실행 start -------------------
            if Game_Start == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game_Start = 1
                        heart = 3
                        score = 0
                        cnt = 0
                        bomb.init(SCREEN_WIDTH, SCREEN_HEIGHT)
                    if event.key == 114:  # r키를 눌렀을 경우
                        Game_Start = 3
                        # 기록 출력 부분
            elif Game_Start == 2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game_Start = 0
                    if event.key == 114:  # r키를 눌렀을 경우
                        Game_Start = 3
                        # 기록 출력 부분
            elif Game_Start == 3:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game_Start = 0
            elif Game_Start == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        person.moveX(-1)
                    if event.key == pygame.K_RIGHT:
                        person.moveX(1)
                    if event.key == pygame.K_UP:
                        person.moveY(-1)
                    if event.key == pygame.K_DOWN:
                        person.moveY(1)
                    if event.key == 112:
                        Game_Start = 4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        person.toX = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        person.toY = 0
            elif Game_Start == 4:
                if event.type == pygame.KEYDOWN:
                    if event.key == 114:
                        Game_Start = 1
                    if event.key == 120:
                        Game_Start = 2
        if Game_Start == 0:
            StartScreen.startScreen(screen)
        elif Game_Start == 1:
            gift.run(screen)
            person.run(screen)
            bomb.run(screen)
            pp = person.getPos()

            for g in gift.gifts:
                if (g['x'] - g['scale'] // 2 <= pp['x'] <= g['x'] + g['scale'] // 2) and (
                        g['y'] - g['scale'] // 2 <= pp['y'] <= g['y'] + g['scale'] // 2):
                    gift.gifts.remove(g)
                    score += random.randint(1, 10) * 10

            for b in bomb.explosion:
                if b['hit']:
                    continue
                if (b['rect'].left <= pp['x'] <= b['rect'].left + b['scale']) and (
                        b['rect'].top <= pp['y'] <= b['rect'].top + b['scale']):
                    heart -= 1
                    b['hit'] = True
                    if heart <= 0:
                        Game_Start = 2
                        file = open('record.txt', 'w')
                        records.append(score)
                        records.sort(key=lambda x: -int(x))
                        file.write("\n".join(map(str, records)))
                        file.write("\n")
                        file.close()
                    break
            if heart == 3:
                screen.blit(heart3, (500, 10))
            elif heart == 2:
                screen.blit(heart2, (500, 10))
            elif heart == 1:
                screen.blit(heart1, (500, 10))

            screen.blit(pause, ((SCREEN_WIDTH - pause.get_width()) // 2, 15))

            cnt += 1
            if cnt % 10 == 0:
                score += 10
            if cnt % 50 == 0:
                gift.addGift()
            if cnt % 100 == 0:
                bomb.addBomb()
            sc = font.render(str(score), True, (0, 0, 0))
            screen.blit(sc, (100 - sc.get_width(), 10))
            # 게임 실행 End -------------------------
        elif Game_Start == 2:
            StartScreen.endScreen(screen, score)
        elif Game_Start == 3:
            StartScreen.recordScreen(screen, records)
        elif Game_Start == 4:
            if heart == 3:
                screen.blit(heart3, (500, 10))
            elif heart == 2:
                screen.blit(heart2, (500, 10))
            elif heart == 1:
                screen.blit(heart1, (500, 10))

            sc = font.render(str(score), True, (0, 0, 0))
            screen.blit(sc, (100 - sc.get_width(), 10))
            gift.display(screen)
            person.display(screen)
            bomb.display(screen)
            screen.blit(screenCover, (0, 0))

            screen.blit(restart, ((SCREEN_WIDTH - restart.get_width()) // 2, 15))
            screen.blit(exit, ((SCREEN_WIDTH - exit.get_width()) // 2, 550))

        pygame.display.update()
    pygame.quit()
    # 점수


runGame()
