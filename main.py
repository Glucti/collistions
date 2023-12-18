import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800,800
screen = pygame.display.set_mode((screen_width, screen_height))

rect_1 = pygame.Rect((350, 350, 100, 100))
x_speed, y_speed = 5, 4

rect_2 = pygame.Rect((300, 600, 200, 100))
rect_2_speed = 2



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((30,30,30,30))
    pygame.draw.rect(screen, (255, 255, 255), rect_1)
    pygame.draw.rect(screen, (255, 0, 0), rect_2)

    pygame.display.flip()
    clock.tick(60)

