# import pygame
# import sys
# import random




# pygame.init()


# # setting screen size

# SCREEN_WIDTH =600
# SCREEN_HEIGHT =600
# screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


# pygame.display.set_caption("flappy bird")










# # clock
# Clock = pygame.time.Clock()
# running = True



# # bird setting
# bird_x = 100
# bird_y = 300
# bird_radius = 20
# bird_velocity = 0
# gravity = 0.5
# flap_strength = -10







# # pipe setup
# pipe_width = 60
# pipe_gap = 150
# pipe_velocity = 5     




# # first pipe open position

# pipe_x =SCREEN_WIDTH
# pipe_height= random.randint(100,400)



# running = True 
# game_over = False







# # game restart on R key
# def reset_game():
#     global bird_y,bird_velocity,pipe_x,pipe_height,score,scored,game_over
#     bird_y = 300
#     bird_velocity = 0
#     pipe_x = SCREEN_WIDTH
#     pipe_height =random.randint(100,400)
#     score = 0
#     scored = False
#     game_over = False




# # game loop
# while running:
#     Clock.tick(60)

        
#     #applying the gravity
#     if not game_over:
#         bird_velocity += gravity
#         bird_y += bird_velocity

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         # game over
#         if not game_over and event.type == pygame.KEYDOWN:
#             if event.key ==pygame.K_SPACE:
#                 bird_velocity =flap_strength

#         else:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:
#                     reset_game()





#         # key press space bar
#         if event.type== pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 bird_velocity =flap_strength


#         # stop bird from going off screen
#         if bird_y > SCREEN_HEIGHT - bird_radius:
#             bird_y = SCREEN_HEIGHT - bird_radius
#             bird_velocity = 0

#         if bird_y < bird_radius:
#             bird_y = bird_radius
#             bird_velocity = 0







#         # pipe
#         pipe_x -= pipe_velocity
#         if pipe_x +pipe_width <0 :
#             pipe_x =SCREEN_WIDTH
#             pipe_height =random.randint(100,400)




#         # Collision detection
#         bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius*2, bird_radius*2)
#         top_pipe_rect = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
#         bottom_pipe_rect = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT)

#         if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
#             game_over = True

#         if bird_y >= SCREEN_HEIGHT - bird_radius or bird_y <= bird_radius:
#             game_over = True    


#     screen.fill((135,206,235))
#     pygame.draw.circle(screen,(255,255,0),(bird_x ,int (bird_y)),bird_radius)#bird

#     # Pipe design
#     pygame.draw.rect(screen,(0,255,0),(pipe_x , 0 , pipe_width, pipe_height))#top pipe
#     pygame.draw.rect(screen,(0,255,0),(pipe_x , pipe_height + pipe_gap, pipe_width,SCREEN_HEIGHT)) #bottom pipe


#     if game_over:
#         font =pygame.font,SysFont(None,48)
#         text =font.render("Game Over !",True,(255,0,0))
#         screen.blit(text,(SCREEN_WIDTH//2-100,SCREEN_HEIGHT //2-24))
#         restart_text = font.render("Press R to Restart", True, (0, 0, 0))
#         screen.blit(restart_text, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 + 60))

#     pygame.display.update()


# pygame.quit()
# sys.exit()            


import pygame
import sys
import random

# Initialize
pygame.init()




# setting screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("flappy bird")

# clock
Clock = pygame.time.Clock()
running = True

# bird setting
bird_x = 100
bird_y = 300
bird_radius = 20
bird_velocity = 0
gravity = 0.5
flap_strength = -10

# pipe setup
pipe_width = 60
pipe_gap = 150
pipe_velocity = 5

# first pipe open position
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(100, 400)

running = True
game_over = False
score = 0
scored = False

# font setup
font = pygame.font.SysFont(None, 48)

# game restart on R key
def reset_game():
    global bird_y, bird_velocity, pipe_x, pipe_height, score, scored, game_over
    bird_y = 300
    bird_velocity = 0
    pipe_x = SCREEN_WIDTH
    pipe_height = random.randint(100, 400)
    score = 0
    scored = False
    game_over = False

# game loop
while running:
    Clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = flap_strength

        elif game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    # applying the gravity
    if not game_over:
        bird_velocity += gravity
        bird_y += bird_velocity

    # stop bird from going off screen
    if bird_y > SCREEN_HEIGHT - bird_radius:
        bird_y = SCREEN_HEIGHT - bird_radius
        bird_velocity = 0

    if bird_y < bird_radius:
        bird_y = bird_radius
        bird_velocity = 0

    # pipe movement
    if not game_over:
        pipe_x -= pipe_velocity

        if pipe_x + pipe_width < 0:
            pipe_x = SCREEN_WIDTH
            pipe_height = random.randint(100, 400)
            scored = False

        # scoring
        if pipe_x + pipe_width < bird_x and not scored:
            score += 1
            scored = True

    # Collision detection
    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)
    top_pipe_rect = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
    bottom_pipe_rect = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - (pipe_height + pipe_gap))

    if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
        game_over = True

    if bird_y >= SCREEN_HEIGHT - bird_radius or bird_y <= bird_radius:
        game_over = True

    # drawing
    screen.fill((135, 206, 235))
    pygame.draw.circle(screen, (255, 255, 0), (bird_x, int(bird_y)), bird_radius)  # bird

    # Pipe design
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 0, pipe_width, pipe_height))  # top pipe
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - (pipe_height + pipe_gap)))  # bottom pipe

    # score display
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Game over screen
    if game_over:
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 24))
        restart_text = font.render("Press R to Restart", True, (0, 0, 0))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 30))

    pygame.display.update()

pygame.quit()
sys.exit()
