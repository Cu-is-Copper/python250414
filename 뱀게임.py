import pygame
import time
import random

# pygame 초기화
pygame.init()

# 색상 정의
흰색 = (255, 255, 255)
검정색 = (0, 0, 0)
빨강색 = (213, 50, 80)
초록색 = (0, 255, 0)
파랑색 = (50, 153, 213)

# 화면 크기 설정
화면_가로 = 800
화면_세로 = 600

# 뱀 크기와 속도 설정
뱀_블록 = 10
뱀_속도 = 15

# pygame 화면 생성
화면 = pygame.display.set_mode((화면_가로, 화면_세로))
pygame.display.set_caption('뱀 게임')

# 폰트 설정
글꼴 = pygame.font.SysFont("bahnschrift", 25)

# 점수 표시 함수
def 점수_표시(score):
    값 = 글꼴.render("점수: " + str(score), True, 파랑색)
    화면.blit(값, [10, 10])

# 게임 루프 함수
def 게임_루프():
    # 게임 종료 및 재시작 플래그
    게임_종료 = False
    게임_끝 = False

    # 뱀 초기 위치
    x = 화면_가로 / 2
    y = 화면_세로 / 2

    # 뱀 이동 방향
    x_변화 = 0
    y_변화 = 0

    # 뱀 몸통 리스트
    뱀_몸통 = []
    뱀_길이 = 1

    # 먹이 위치
    먹이_x = round(random.randrange(0, 화면_가로 - 뱀_블록) / 10.0) * 10.0
    먹이_y = round(random.randrange(0, 화면_세로 - 뱀_블록) / 10.0) * 10.0

    # 게임 루프
    while not 게임_종료:

        # 게임 종료 화면 처리
        while 게임_끝:
            화면.fill(검정색)
            메시지 = 글꼴.render("게임 오버! 다시 시작하려면 C를 누르세요. 종료하려면 Q를 누르세요.", True, 빨강색)
            화면.blit(메시지, [화면_가로 / 6, 화면_세로 / 3])
            점수_표시(뱀_길이 - 1)
            pygame.display.update()

            for 이벤트 in pygame.event.get():
                if 이벤트.type == pygame.KEYDOWN:
                    if 이벤트.key == pygame.K_q:
                        게임_종료 = True
                        게임_끝 = False
                    if 이벤트.key == pygame.K_c:
                        게임_루프()

        # 키 입력 처리
        for 이벤트 in pygame.event.get():
            if 이벤트.type == pygame.QUIT:
                게임_종료 = True
            if 이벤트.type == pygame.KEYDOWN:
                if 이벤트.key == pygame.K_LEFT:
                    x_변화 = -뱀_블록
                    y_변화 = 0
                elif 이벤트.key == pygame.K_RIGHT:
                    x_변화 = 뱀_블록
                    y_변화 = 0
                elif 이벤트.key == pygame.K_UP:
                    x_변화 = 0
                    y_변화 = -뱀_블록
                elif 이벤트.key == pygame.K_DOWN:
                    x_변화 = 0
                    y_변화 = 뱀_블록

        # 화면 경계 충돌 처리
        if x >= 화면_가로 or x < 0 or y >= 화면_세로 or y < 0:
            게임_끝 = True

        # 뱀 이동
        x += x_변화
        y += y_변화
        화면.fill(검정색)
        pygame.draw.rect(화면, 초록색, [먹이_x, 먹이_y, 뱀_블록, 뱀_블록])

        # 뱀 머리 추가
        뱀_머리 = []
        뱀_머리.append(x)
        뱀_머리.append(y)
        뱀_몸통.append(뱀_머리)

        # 뱀 길이 유지
        if len(뱀_몸통) > 뱀_길이:
            del 뱀_몸통[0]

        # 뱀이 자기 몸통에 부딪혔는지 확인
        for 블록 in 뱀_몸통[:-1]:
            if 블록 == 뱀_머리:
                게임_끝 = True

        # 뱀 그리기
        for 블록 in 뱀_몸통:
            pygame.draw.rect(화면, 파랑색, [블록[0], 블록[1], 뱀_블록, 뱀_블록])

        # 점수 표시
        점수_표시(뱀_길이 - 1)

        # 화면 업데이트
        pygame.display.update()

        # 먹이를 먹었는지 확인
        if x == 먹이_x and y == 먹이_y:
            먹이_x = round(random.randrange(0, 화면_가로 - 뱀_블록) / 10.0) * 10.0
            먹이_y = round(random.randrange(0, 화면_세로 - 뱀_블록) / 10.0) * 10.0
            뱀_길이 += 1

        # 게임 속도 조절
        time.sleep(0.1)

    # pygame 종료
    pygame.quit()
    quit()

# 게임 실행
게임_루프()