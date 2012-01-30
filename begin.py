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
    x_offset_one = 0
    x_offset_two = 0
    x_current_one = 1
    x_current_two = 1

    ball_x = 640 / 2 - 5
    ball_y = 480 / 2 - 5
    bal_dir_x = 1
    bal_dir_y = 1

    score_one = 0
    score_two = 0

    draw_score(score_one, score_two)

    while True:
        pygame.display.update()

        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_offset_one = -3
                if event.key == pygame.K_RIGHT:
                    x_offset_one = 3
                if event.key == pygame.K_e:
                    x_offset_two = -3
                if event.key == pygame.K_r:
                    x_offset_two = 3

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    x_offset_one = 0
                if event.key in [pygame.K_e, pygame.K_r]:
                    x_offset_two = 0

        x_current_one += x_offset_one
        x_current_two += x_offset_two
        x_current_one = validate_pos(x_current_one)
        x_current_two = validate_pos(x_current_two)

        ball_x, ball_y, bal_dir_x, bal_dir_y = get_ball_new_pos(
                (ball_x, ball_y),
                (x_current_one, x_current_two),
                (bal_dir_x, bal_dir_y)
                )

        if  ball_y < 0 or ball_y > 478:
            if ball_y < 0: score_two += 1
            if ball_y > 478: score_one += 1
            draw_score(score_one, score_two)
            ball_x = 640 / 2 - 5
            ball_y = 480 / 2 - 5
            bal_dir_x = 1
            bal_dir_y = 1

        screen.fill((0, 0, 0))
        draw_racket_one(screen, x_current_one)
        draw_racket_two(screen, x_current_two)
        draw_ball(screen, ball_x, ball_y)

def draw_score(score_one, score_two):
    print("Score : %d - %d" % (score_one, score_two))

def validate_pos(x_current):
    x_min = 2
    x_max = 638 - 70
    x_valid = x_current
    if x_current > x_max: x_valid = x_max
    elif x_current < x_min: x_valid = x_min
    return x_valid
                
def get_ball_new_pos(current_ball_pos, rackets_pos, ball_dir):
    ball_x, ball_y = current_ball_pos
    bal_dir_x, bal_dir_y = ball_dir
    racket_one_x, racket_two_x = rackets_pos

    if ( ball_x > racket_one_x and ball_x < racket_one_x + 70 ) and ball_y == 12:
        bal_dir_y *= -1

    if ( ball_x > racket_two_x and ball_x < racket_two_x + 70 ) and ball_y == 468 - 10:
        bal_dir_y *= -1


    if ball_x > 638 - 10 or ball_x < 2:
        bal_dir_x *= -1

    ball_y += 1 * bal_dir_y
    ball_x += 1 * bal_dir_x

    return (ball_x, ball_y, bal_dir_x, bal_dir_y)

def draw_racket_one(screen, x):
    pygame.draw.rect(screen, WHITE, [x, 2, 70, 10])

def draw_racket_two(screen, x):
    pygame.draw.rect(screen, WHITE, [x, 468, 70, 10])

def draw_ball(screen, x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 10, 10])

if __name__ == '__main__':
    main()
