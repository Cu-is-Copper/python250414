import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 패들 설정
paddle_width = 100
paddle_height = 20
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 40
paddle_speed = 8

# 공 설정
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 5
ball_dy = -5

# 블록 설정
block_width = 80
block_height = 30
block_rows = 5
block_cols = 10
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        block_x = col * (block_width + 5) + 5
        block_y = row * (block_height + 5) + 5
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# 게임 루프
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed
    
    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy
    
    # 벽 충돌
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1
    
    # 패들 충돌
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.collidepoint(ball_x, ball_y):
        ball_dy *= -1
    
    # 블록 충돌
    for block in blocks[:]:
        if block.collidepoint(ball_x, ball_y):
            blocks.remove(block)
            ball_dy *= -1
            break
    
    # 게임 오버 체크
    if ball_y >= HEIGHT:
        game_over = True
    
    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
    
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)
    
    pygame.display.flip()
    clock.tick(60)

# 게임 오버 메시지
font = pygame.font.Font(None, 74)
text = font.render('게임 오버!', True, WHITE)
text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
screen.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(2000)
pygame.quit()
