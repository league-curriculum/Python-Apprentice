import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 60

# Bird properties
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
bird_velocity = 0
gravity = 0.25      # slower fall
jump_strength = -8  # gentler jump

# Pipe properties
pipe_width = 70
pipe_gap = 200      # bigger gap
pipe_velocity = 4

# Pipes: list of dictionaries with x position and height of the top pipe
pipes = []
pipe_spawn_time = 0  # Timer to spawn pipes

score = 0
font = pygame.font.SysFont(None, 40)

def draw_bird(y):
    pygame.draw.circle(screen, BLUE, (bird_x, int(y)), bird_radius)

def draw_pipe(x, height):
    # Top pipe
    pygame.draw.rect(screen, GREEN, (x, 0, pipe_width, height))
    # Bottom pipe
    bottom_pipe_y = height + pipe_gap
    bottom_pipe_height = HEIGHT - bottom_pipe_y
    pygame.draw.rect(screen, GREEN, (x, bottom_pipe_y, pipe_width, bottom_pipe_height))

def check_collision(bird_y, pipes):
    # Check if bird hits ground or ceiling
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        return True
    # Check collision with pipes
    for pipe in pipes:
        pipe_x = pipe['x']
        pipe_height = pipe['height']
        if bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width:
            if bird_y - bird_radius < pipe_height or bird_y + bird_radius > pipe_height + pipe_gap:
                return True
    return False

def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def game_over_screen(score):
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLACK)
    score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    global bird_y, bird_velocity, pipes, pipe_spawn_time, score
    
    running = True
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump_strength

        # Bird physics
        bird_velocity += gravity
        bird_y += bird_velocity

        # Pipe spawning
        pipe_spawn_time += 1
        if pipe_spawn_time > 90:  # Every 1.5 seconds (at 60 FPS)
            pipe_height = random.randint(50, HEIGHT - pipe_gap - 50)
            pipes.append({'x': WIDTH, 'height': pipe_height})
            pipe_spawn_time = 0

        # Move pipes and remove off-screen ones
        for pipe in pipes:
            pipe['x'] -= pipe_velocity
        pipes = [pipe for pipe in pipes if pipe['x'] + pipe_width > 0]

        # Check score (when bird passes pipe)
        for pipe in pipes:
            if pipe['x'] + pipe_width < bird_x and not pipe.get('passed', False):
                score += 1
                pipe['passed'] = True

        # Draw everything
        draw_bird(bird_y)
        for pipe in pipes:
            draw_pipe(pipe['x'], pipe['height'])
        display_score(score)

        # Check collisions
        if check_collision(bird_y, pipes):
            game_over_screen(score)
            # Reset game state
            bird_y = HEIGHT // 2
            bird_velocity = 0
            pipes = []
            pipe_spawn_time = 0
            score = 0

        pygame.display.flip()

if __name__ == "__main__":
    main()
