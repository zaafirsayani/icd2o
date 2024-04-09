import pygame
import sys
import random


pygame.init()

break_sound = pygame.mixer.Sound("break.wav")
music = pygame.mixer.Sound("breakoutsound.wav")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
LIGHTBLUE = (0,255,255)


PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
paddle = pygame.Rect((SCREEN_WIDTH - PADDLE_WIDTH) // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)


BALL_RADIUS = 10
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 6 * random.choice((1, -1))
ball_speed_y = 6


BRICK_WIDTH = 80
BRICK_HEIGHT = 30
brick_rows = 5
brick_columns = 10
bricks = []

for row in range(brick_rows):
    for col in range(brick_columns):
        brick = {}
        brick['rect'] = pygame.Rect(col * (BRICK_WIDTH + 2) + 1, row * (BRICK_HEIGHT + 2) + 1, BRICK_WIDTH, BRICK_HEIGHT)
        brick['colour'] = random.choice([BLUE, RED, GREEN, LIGHTBLUE])
        bricks.append(brick)


score = 0
font = pygame.font.Font(None, 36)

timer = 0
font = pygame.font.Font(None, 36)


running = True
music.play()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 10
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.right += 10

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    for brick in bricks[:]:
        if ball.colliderect(brick['rect']):
            if brick['colour'] == RED:
                ball_speed_x *= 0.8
                ball_speed_y *= 0.8
            if brick['colour'] == BLUE:
                score+=2
            if brick['colour'] == GREEN:
                score-=1
            if brick['colour'] == LIGHTBLUE:
                paddle.left -=2
                paddle.right -=2
            
            bricks.remove(brick)
            ball_speed_y *= -1
            score += 1
            break_sound.play()
            break_sound.set_volume(0.5)
        
            
    
    timer+=0.02
    if ball.bottom >= SCREEN_HEIGHT or not bricks:
        running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, brick['colour'], brick['rect'])

    
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    timer_text = font.render("Time: " + str(int(timer)), True, WHITE)
    screen.blit(timer_text, (610, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)


pygame.time.delay(2000)

pygame.quit()
sys.exit()
