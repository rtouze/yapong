#!/usr/bin/env python
""" Debut de jeu pong en python """

import pygame
from pygame.locals import *
from pygame.time import Clock
#import yapong.ball
from yapong import constants
from yapong.sprites import *
from yapong.score import Score
from yapong.drawers import ScoreDrawer
import time

WHITE = constants.WHITE

def main():
    pygame.init()
    screenRes = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenRes, 0, 32)
    pygame.display.set_caption("Yapong")

    y_offset_one = 0
    y_offset_two = 0

    score = Score()
    score_drawer = ScoreDrawer(screen)

    ball = Ball()
    racket_x_position = 60
    racket1 = Racket(racket_x_position, constants.SCREEN_WIDTH/2 - 35)
    racket2 = Racket(
            constants.SCREEN_WIDTH - racket_x_position - 10,
            constants.SCREEN_WIDTH/2 - 35
            )

    net = Net()
    clock=Clock()

    while True:
        pygame.display.update()

        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    y_offset_one = -3
                if event.key == pygame.K_d:
                    y_offset_one = 3
                if event.key == pygame.K_UP:
                    y_offset_two = -3
                if event.key == pygame.K_DOWN:
                    y_offset_two = 3

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_e, pygame.K_d]:
                    y_offset_one = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    y_offset_two = 0

        racket1.update_position(y_offset_one)
        racket2.update_position(y_offset_two)
        ball.update_position(racket1, racket2)
        score.check_score(ball)

        screen.fill((0, 0, 0))
        score_drawer.draw(score)
        net.draw(screen)
        ball.draw(screen)
        racket1.draw(screen)
        racket2.draw(screen)
        #time.sleep(0.002)
        clock.tick(80)

if __name__ == '__main__':
    main()
