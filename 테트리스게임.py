import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (0, 0, 255),    # Blue
    (0, 255, 0),    # Green
    (128, 0, 128),  # Purple
    (255, 0, 0)     # Red
]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Initialize grid
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


class Tetrimino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def can_move(self, dx, dy, grid):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.x + x + dx
                    new_y = self.y + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or (new_y >= 0 and grid[new_y][new_x] != BLACK):
                        return False
        return True

    def lock_to_grid(self, grid):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid[self.y + y][self.x + x] = self.color


def clear_lines(grid):
    global score
    new_grid = [row for row in grid if any(cell == BLACK for cell in row)]
    lines_cleared = GRID_HEIGHT - len(new_grid)
    score += lines_cleared
    new_grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(lines_cleared)] + new_grid
    return new_grid


# Game loop
def main():
    global grid, score
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    running = True
    current_tetrimino = Tetrimino()
    fall_time = 0
    score = 0

    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick(30)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_tetrimino.can_move(-1, 0, grid):
                    current_tetrimino.x -= 1
                if event.key == pygame.K_RIGHT and current_tetrimino.can_move(1, 0, grid):
                    current_tetrimino.x += 1
                if event.key == pygame.K_DOWN and current_tetrimino.can_move(0, 1, grid):
                    current_tetrimino.y += 1
                if event.key == pygame.K_UP:
                    current_tetrimino.rotate()
                    if not current_tetrimino.can_move(0, 0, grid):
                        current_tetrimino.rotate()
                        current_tetrimino.rotate()
                        current_tetrimino.rotate()
                if event.key == pygame.K_SPACE:  # Speed up drop
                    while current_tetrimino.can_move(0, 1, grid):
                        current_tetrimino.y += 1
                    current_tetrimino.lock_to_grid(grid)
                    grid = clear_lines(grid)
                    current_tetrimino = Tetrimino()
                    if not current_tetrimino.can_move(0, 0, grid):
                        running = False  # Game over

        # Move tetrimino down
        if fall_time > 500:
            if current_tetrimino.can_move(0, 1, grid):
                current_tetrimino.y += 1
            else:
                current_tetrimino.lock_to_grid(grid)
                grid = clear_lines(grid)
                current_tetrimino = Tetrimino()
                if not current_tetrimino.can_move(0, 0, grid):
                    running = False  # Game over
            fall_time = 0

        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        # Draw current tetrimino
        for y, row in enumerate(current_tetrimino.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, current_tetrimino.color, ((current_tetrimino.x + x) * BLOCK_SIZE, (current_tetrimino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, GRAY, ((current_tetrimino.x + x) * BLOCK_SIZE, (current_tetrimino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()