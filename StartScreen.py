import pygame


def init():
    global message1, message2, message3
    # 글자 크기 설정
    Big_font = pygame.font.SysFont(None, 80)
    Small_font = pygame.font.SysFont(None, 40)
    Mini_font = pygame.font.SysFont(None, 20)
    # 문구와 색상 설정
    message1 = Big_font.render("BOMB DODGE", True, (0, 0, 0))
    message2 = Small_font.render("Press the space bar to start the game..", True, (0, 191, 255))
    message3 = Mini_font.render("- Made by METHOD -", True, (102, 102, 102))


# 스페이스바를 누르지 않았을 경우 -> 처음 시작 화면
def startScreen(screen):
    global message1, message2, message3
    screen.fill((255, 255, 255))
    screen.blit(message1, (110, 230))
    screen.blit(message2, (45, 310))
    screen.blit(message3, (240, 500))
    pygame.display.update()


def endScreen(screen, score):
    screen.fill((0, 0, 0))
    Big_font = pygame.font.SysFont(None, 80)
    Small_font = pygame.font.SysFont(None, 40)
    message1 = Big_font.render("End", True, (255, 255, 255))
    message2 = Small_font.render(str(score), True, (255, 255, 255))
    screen.blit(message1, (250, 250))
    screen.blit(message2, (290, 300))
    screen.blit(message3, (240, 500))
