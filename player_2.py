import pygame
import time

WIDTH = 800
HEIGHT = 600
FPS = 60
SPEED = 5

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong (Player 2)")
clock = pygame.time.Clock()

is_width = True
is_height = True
is_player = True

font = pygame.font.SysFont('Arial', 50, True)

x, y = 0, 0  # coordinates ball
xf, yf = 0, HEIGHT // 2 - 50  # coordinates first player
xs, ys = WIDTH - 5, HEIGHT // 2 - 50  # coordinates second player

score_f = 0  # score first player
score_s = 0  # score second player


def nav_ball():
    global x, y, score_f, score_s, is_height, is_width
    if y > HEIGHT:
        is_height = True
    elif y < 0:
        is_height = False

    if first_player.colliderect(ball):
        is_width = True
    elif x < 0:
        score_s += 1
        x, y = WIDTH, 0
        is_width, is_height = False, True
        time.sleep(1)
        return

    if second_player.colliderect(ball):
        is_width = False
    elif x > WIDTH:
        score_f += 1
        x, y = 0, 0
        is_width, is_height = True, True
        time.sleep(1)
        return

    if is_height:
        y -= SPEED
    else:
        y += SPEED

    if is_width:
        x += SPEED
    else:
        x -= SPEED


while True:
    win.fill((41, 41, 41))

    pygame.draw.line(win, (220, 220, 220), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    first_player = pygame.draw.rect(win, (122, 41, 222), (xf, yf, 5, 100))
    second_player = pygame.draw.rect(win, (241, 130, 51), (xs, ys, 5, 100))

    ball = pygame.draw.circle(win, (14, 151, 90), (x, y), 7)

    render_first = font.render(str(score_f), 1, (61, 61, 61))  # render score first player
    render_second = font.render(str(score_s), 1, (61, 61, 61))  # render score second player

    win.blit(render_first, (WIDTH // 2 - 100, 10))
    win.blit(render_second, (WIDTH // 2 + 70, 10))

    nav_ball()

    if yf < 0:
        yf = 0
    if yf > (HEIGHT - 100):
        yf = HEIGHT - 100

    if ys < 0:
        ys = 0
    if ys > (HEIGHT - 100):
        ys = HEIGHT - 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(FPS)

    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        yf += SPEED
    if key[pygame.K_a]:
        yf -= SPEED
    if key[pygame.K_RIGHT]:
        ys += SPEED
    if key[pygame.K_LEFT]:
        ys -= SPEED
