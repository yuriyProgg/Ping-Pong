import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 52)

while True:
    win.fill((41, 41, 41))
    p1 = font.render("Player 1", 1, (66, 135, 245))  # p1: this player 1
    p1_rect = p1.get_rect(topleft=(100, 200))
    p2 = font.render("Player 2", 1, (66, 135, 245))  # p2: this player 2
    p2_rect = p2.get_rect(topleft=(400, 200))

    win.blit(p1, p1_rect)
    win.blit(p2, p2_rect)

    mouse = pygame.mouse.get_pos()
    if p1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        from player_1 import *
    if p2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        from player_2 import *

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(10)
