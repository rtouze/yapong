#!/usr/bin/env python
""" Debut de jeu pong en python """

import pygame
from pygame.locals import *
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
    racket1 = Racket(constants.SCREEN_MARGIN, constants.SCREEN_WIDTH/2 - 35)
    racket2 = Racket(
            constants.SCREEN_WIDTH - constants.SCREEN_MARGIN - 10,
            constants.SCREEN_WIDTH/2 - 35
            )

    while True:
        pygame.display.update()

        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    y_offset_one = -3
                if event.key == pygame.K_q:
                    y_offset_one = 3
                if event.key == pygame.K_UP:
                    y_offset_two = -3
                if event.key == pygame.K_DOWN:
                    y_offset_two = 3

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_q]:
                    y_offset_one = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    y_offset_two = 0

        racket1.set_position(y_offset_one)
        racket2.set_position(y_offset_two)
        ball.set_position(racket1, racket2)
        score.check_score(ball)

        screen.fill((0, 0, 0))
        score_drawer.draw(score)
        ball.draw(screen)
        racket1.draw(screen)
        racket2.draw(screen)
        time.sleep(0.002)

# TODO : gerer le score autrement, c'est nul la
def draw_score(score):
    if score.updated:
        print("Score : %d - %d" % (score.player1, score.player2))
    score.updated = False

if __name__ == '__main__':
    main()