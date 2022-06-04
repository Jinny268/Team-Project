import pygame

# 글자 크기 설정
Big_font = None
Small_font = None
Mini_font = None
WIDTH, HEIGHT = 0, 0
cnt = 0


def init(width, height):
    global WIDTH, HEIGHT, cnt, Big_font, Small_font, Mini_font, message1, message2, message3
    # 문구와 색상 설정
    WIDTH, HEIGHT = width, height
    cnt = 0
    # 글자 크기 설정
    Big_font = pygame.font.SysFont(None, 80, None, None)
    Small_font = pygame.font.SysFont(None, 40, None, None)
    Mini_font = pygame.font.SysFont(None, 20, None, None)
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


def endScreen(screen, score):
    global WIDTH, HEIGHT
    screen.fill((255, 255, 255))
    game_over_image1 = Big_font.render('Game Over', True, (255, 0, 0))
    game_over_image2 = Small_font.render('Score: {}'.format(score), True, (255, 245, 0))
    game_over_image3 = Small_font.render("Press the space bar to main screen..", True, (0, 191, 255))
    screen.blit(game_over_image1,
                ((WIDTH - game_over_image1.get_width()) // 2, (HEIGHT - game_over_image1.get_height()) // 2))
    screen.blit(game_over_image2,
                ((WIDTH - game_over_image2.get_width()) // 2, ((HEIGHT - game_over_image2.get_height()) // 2) + 40))
    screen.blit(game_over_image3,
                (45, 520))
