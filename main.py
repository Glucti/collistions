import pygame
import sys


def rect_bounce():
    global x_speed, y_speed, rect_2_speed
    rect_1.x += x_speed
    rect_1.y += y_speed
    # collision with wall

    if rect_1.right >= screen_width or rect_1.left <= 0:
        x_speed *= -1
    if rect_1.top <= 0 or rect_1.bottom >= screen_height:
        y_speed *= -1

    # move rect_2
    rect_2.y += rect_2_speed
    if rect_2.top <= 0 or rect_2.bottom >= screen_height:
        rect_2_speed *= -1
    if rect_2.right >= screen_width or rect_2.left <= 0:
        rect_2_speed *= -1

    # rect collision
    collision_tolerance = 8
    if rect_1.colliderect(rect_2):
        if abs(rect_2.top - rect_1.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(rect_2.bottom - rect_1.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(rect_2.left - rect_1.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1
        if abs(rect_2.right - rect_1.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1

    pygame.draw.rect(screen, (255, 255, 255), rect_1)
    pygame.draw.rect(screen, (255, 0, 0), rect_2)


pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
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
    screen.fill((30, 30, 30, 30))
    rect_bounce()
    pygame.display.flip()
    clock.tick(60)
