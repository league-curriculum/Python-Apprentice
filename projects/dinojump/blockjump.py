import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
PLAYER_SIZE = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 10
GRAVITY = 1
JUMP_STRENGTH = 15
BACKGROUND_SCROLL_SPEED = 5

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Endless Runner")

# Define player
player = pygame.Rect(100, SCREEN_HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_y_velocity = 0
is_jumping = False

# Define obstacles
obstacles = []
spawn_timer = 0

# Define background
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(WHITE)
background_rect = background.get_rect()

# Score
score = 0
font = pygame.font.SysFont(None, 48)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        player_y_velocity = -JUMP_STRENGTH
        is_jumping = True

    # Update player position
    player_y_velocity += GRAVITY
    player.y += player_y_velocity

    if player.y >= SCREEN_HEIGHT - PLAYER_SIZE:
        player.y = SCREEN_HEIGHT - PLAYER_SIZE
        player_y_velocity = 0
        is_jumping = False

    # Spawn obstacles
    spawn_timer += 1
    if spawn_timer >= 30:
        obstacle = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        obstacles.append(obstacle)
        spawn_timer = 0

    # Move obstacles
    for obstacle in obstacles:
        obstacle.x -= OBSTACLE_SPEED

    # Remove off-screen obstacles
    on_screen_obstacles = []
    for obstacle in obstacles:
        if obstacle.x + OBSTACLE_WIDTH > 0:
            on_screen_obstacles.append(obstacle)
    obstacles = on_screen_obstacles

 
    # Check for collisions
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            running = False

    # Scroll background
    background_rect.x -= BACKGROUND_SCROLL_SPEED
    if background_rect.x <= -SCREEN_WIDTH:
        background_rect.x = 0

    # Update score
    score += 1

    # Draw everything
    screen.blit(background, background_rect)
    screen.blit(background, (background_rect.x + SCREEN_WIDTH, background_rect.y))
    pygame.draw.rect(screen, BLACK, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
