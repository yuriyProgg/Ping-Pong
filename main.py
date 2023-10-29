import time

import pygame


def nav_ball():
    global x, y, is_width, is_height, score

    if x > WIDTH:
        is_width = False
    elif x < 0:
        is_width = True
    if player.colliderect(circle):
        score += 1
        is_height = False
    elif y > HEIGHT:
        time.sleep(3)
        exit()
    elif y < 0:
        is_height = True

    if is_width:
        x += SPEED
    else:
        x -= SPEED

    if is_height:
        y += SPEED
    else:
        y -= SPEED


def best_score():
    global best
    with open('best.txt', 'r') as f:
        best = int(f.read())

    if score > best:
        with open('best.txt', 'w') as f:
            f.write(str(score))


WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
x, y = 0, 0
is_width = True
is_height = True
FPS = 60
SPEED = 5
score = 0
best = 0

pos_block = WIDTH / 2 - 50


pygame.init()
win = pygame.display.set_mode(SIZE)  # win: this window
pygame.display.set_caption("Ping-Pong")  # title game "Ping-Pong"
clock = pygame.time.Clock()

font_area = pygame.font.SysFont('Arial', 22, True)

while True:
    win.fill((41, 41, 41))
    circle = pygame.draw.circle(win, (220, 180, 90), (x, y), 10)
    player = pygame.draw.rect(win, (220, 41, 141), (pos_block, HEIGHT - 5, 100, 5))

    nav_ball()
    best_score()

    render_score = font_area.render(f"SCORE: {score}", True, (202, 51, 74))
    render_best = font_area.render(f"BEST: {best}", True, (41, 82, 144))

    win.blit(render_score, (5, 5))
    win.blit(render_best, (WIDTH // 4.5, 5))

    if pos_block > (WIDTH - 100):
        pos_block = WIDTH - 100
    if pos_block < 0:
        pos_block = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(FPS)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        pos_block -= SPEED
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        pos_block += SPEED
