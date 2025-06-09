import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Basket settings
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 7

# Ball settings
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop flag
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 frames per second
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move the ball down
    ball_y += ball_speed

    # Check if ball caught by basket
    if (basket_y < ball_y + ball_radius < basket_y + basket_height) and (basket_x < ball_x < basket_x + basket_width):
        score += 1
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = 0

    # If ball hits the bottom, reset ball and lose a point
    if ball_y > HEIGHT:
        score -= 1
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = 0

    # Draw basket
    pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height))

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()

 