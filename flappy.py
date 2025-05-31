import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 80

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 32)

# Game constants
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_SPEED = 3
PIPE_FREQUENCY = 1500  # milliseconds

class Bird:
    WIDTH = 40
    HEIGHT = 30

    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = int(self.y)

    def draw(self, surface):
        pygame.draw.ellipse(surface, RED, self.rect)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, SCREEN_HEIGHT - GROUND_HEIGHT - PIPE_GAP - 50)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT - (self.height + PIPE_GAP))

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, self.top_rect)
        pygame.draw.rect(surface, GREEN, self.bottom_rect)

    def off_screen(self):
        return self.x + PIPE_WIDTH < 0

    def collide(self, bird):
        return self.top_rect.colliderect(bird.rect) or self.bottom_rect.colliderect(bird.rect)

def draw_ground(surface):
    ground_rect = pygame.Rect(0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT)
    pygame.draw.rect(surface, (194, 178, 128), ground_rect)

def main():
    bird = Bird()
    pipes = []
    score = 0
    last_pipe_time = pygame.time.get_ticks()

    running = True
    game_over = False

    while running:
        clock.tick(60)
        screen.fill(SKY_BLUE)
        draw_ground(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.flap()
                if event.key == pygame.K_r and game_over:
                    # Restart game
                    bird = Bird()
                    pipes = []
                    score = 0
                    last_pipe_time = pygame.time.get_ticks()
                    game_over = False

        if not game_over:
            # Generate pipes
            current_time = pygame.time.get_ticks()
            if current_time - last_pipe_time > PIPE_FREQUENCY:
                pipes.append(Pipe(SCREEN_WIDTH))
                last_pipe_time = current_time

            # Update bird
            bird.update()

            # Update pipes
            for pipe in pipes:
                pipe.update()
                if pipe.collide(bird):
                    game_over = True

            # Remove off screen pipes
            pipes = [pipe for pipe in pipes if not pipe.off_screen()]

            # Check if bird hits ground or flies out of screen top
            if bird.y + bird.HEIGHT > SCREEN_HEIGHT - GROUND_HEIGHT or bird.y < 0:
                game_over = True

            # Update score
            for pipe in pipes:
                # Score only once when pipe passes the bird
                if pipe.x + PIPE_WIDTH < bird.x and not hasattr(pipe, "passed"):
                    pipe.passed = True
                    score += 1

        # Draw pipes
        for pipe in pipes:
            pipe.draw(screen)

        # Draw bird
        bird.draw(screen)

        # Draw score
        score_text = FONT.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = FONT.render("Game Over! Press R to Restart", True, BLACK)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_text, text_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

