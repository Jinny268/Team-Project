print('메소드(9팀) - 팀 프로젝트')
from pygame import *

WINDOW_WIDTH = 600  # window 가로
WINDOW_HEIGHT = 600  # window 세로

init()  # pygame 초기화
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # 디스플레이 설정

# display.set_icon(icon) # 아이콘 설정
display.set_caption("method(9)")  # 타이틀 설정

run = True
while run:  # 실행부
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
