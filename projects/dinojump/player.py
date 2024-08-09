import pygame

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
GRAVITY = 1
JUMP_STRENGTH = 15

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumper")

# Define player
player = pygame.Rect(100, SCREEN_HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_y_velocity = 0
is_jumping = False

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

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
