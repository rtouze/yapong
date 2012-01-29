#!/usr/bin/env python
""" Debut de jeu pong en python """

import pygame
from pygame.locals import *

WHITE = (255, 255, 255)

def main():
    pygame.init()
    screenRes = (640, 480)
    screen = pygame.display.set_mode(screenRes, 0, 32)
    pygame.display.set_caption("Yapong")
    x_offset = 0
    x_current = 1

    #clock = pygame.time.Clock()

    ball_x = 640 / 2 - 5
    ball_y = 480 / 2 - 5
    bal_dir_x = 1
    bal_dir_y = 1

    while True:
        pygame.display.update()

        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_offset = -3
                if event.key == pygame.K_RIGHT:
                    x_offset = 3
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    x_offset = 0

        x_current += x_offset
        x_min = 2
        x_max = 638 - 70

        

        if x_current > x_max: x_current = x_max
        elif x_current < x_min: x_current = x_min

        ball_x, ball_y, bal_dir_x, bal_dir_y = get_ball_new_pos((ball_x, ball_y), x_current, (bal_dir_x, bal_dir_y))

        screen.fill((0, 0, 0))
        draw_rect_one(screen, x_current)
        draw_ball(screen, ball_x, ball_y)
        draw_wall(screen)

        #pygame.display.flip()
        #clock.tick(100)
                
def get_ball_new_pos(current_ball_pos, racket_pos, ball_dir):
    ball_x, ball_y = current_ball_pos
    bal_dir_x, bal_dir_y = ball_dir
    racket_x = racket_pos

    if ball_y > 468 - 10:
        bal_dir_y *= -1

    if ( ball_x > racket_x or ball_x < racket_x + 70 ) and ball_y < 12:
        bal_dir_y *= -1

    if ( ball_y < 0 ):
        ball_x = 640 / 2 - 5
        ball_y = 480 / 2 - 5
        bal_dir_x = 1
        bal_dir_y = 1

    if ball_x > 638 - 10 or ball_x < 2:
        bal_dir_x *= -1

    ball_y += 1 * bal_dir_y
    ball_x += 1 * bal_dir_x

    return (ball_x, ball_y, bal_dir_x, bal_dir_y)

def draw_rect_one(screen, x):
    pygame.draw.rect(screen, WHITE, [x, 2, 70, 10])

def draw_wall(screen):
    pygame.draw.rect(screen, WHITE, [0, 468, 640, 10])

def draw_ball(screen, x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 10, 10])


#    pygame. draw.rect(


if __name__ == '__main__':
    main()
