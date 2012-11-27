#!/usr/bin/env python
""" Debut de jeu pong en python """

import pygame
from pygame.locals import *
from pygame.time import Clock
from yapong import constants
from yapong.sprites import *
from yapong.score import Score
from yapong.drawers import ScoreDrawer, TitleDrawer
import time

WHITE = constants.WHITE
R1_DOWN = 1
R1_UP = 2
R2_DOWN = 3
R2_UP = 4

def main():

    pygame.init()

    # sound file
    # TODO test that file exists!
    beep_filename_1 = './yapong/sounds/beep-7.wav'
    beep_filename_2 = './yapong/sounds/beep-8.wav'
    sound_1 = pygame.mixer.Sound(beep_filename_1)
    sound_2 = pygame.mixer.Sound(beep_filename_2)

    screenRes = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenRes, 0, 32)
    pygame.display.set_caption("Yapong")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    y_offset_one = 0
    y_offset_two = 0

    score = Score()
    score_drawer = ScoreDrawer(screen)

    ball = Ball(sound_1, sound_2)
    racket_x_position = 60
    racket1 = Racket(racket_x_position, constants.SCREEN_WIDTH/2 - 35)
    racket2 = Racket(
            constants.SCREEN_WIDTH - racket_x_position - 10,
            constants.SCREEN_WIDTH/2 - 35
            )

    net = Net()
    clock=Clock()

    accel_r1 = 0
    accel_r2 = 0

    previous_r1 = 0
    previous_r2 = 0

    scene_nb = 0 # first scene by default

    #temp
    title = TitleDrawer(screen)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        pygame.display.update()

        if previous_r1 == R1_DOWN and accel_r1 < 30:
            accel_r1 += 1
        if previous_r1 == R1_UP and accel_r1 > -30:
            accel_r1 -= 1
        if previous_r2 == R2_DOWN and accel_r2 < 30:
            accel_r2 += 1
        if previous_r2 == R2_UP and accel_r2 > -30:
            accel_r2 -= 1

        if previous_r1 == 0: accel_r1 = 0
        if previous_r2 == 0: accel_r2 = 0


        #Event loop
        for event in pygame.event.get():
            if scene_nb == 1:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        y_offset_one = -1
                        previous_r1 = R1_UP
                    if event.key == pygame.K_d:
                        y_offset_one = 1
                        previous_r1 = R1_DOWN
                    if event.key == pygame.K_UP:
                        y_offset_two = -1
                        previous_r2 = R2_UP
                    if event.key == pygame.K_DOWN:
                        y_offset_two = 1
                        previous_r2 = R2_DOWN

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_e, pygame.K_d]:
                        y_offset_one = 0
                        previous_r1 = 0
                    if event.key in [pygame.K_UP, pygame.K_DOWN]:
                        y_offset_two = 0
                        previous_r2 = 0
            elif scene_nb == 0:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN: scene_nb += 1


        if scene_nb == 1:
            racket1.update_position(y_offset_one, accel_r1)
            racket2.update_position(y_offset_two, accel_r2)
            ball.update_position(racket1, racket2)
            score.check_score(ball)

        # TODO use blit to improve perf (http://www.pygame.org/docs/tut/tom/games2.html)
        # TODO score are blitted only on refresh
        screen.fill((0, 0, 0))
        if scene_nb == 1:

            score_drawer.draw(score)
            net.draw(screen)
            ball.draw(screen)
            racket1.draw(screen)
            racket2.draw(screen)
        elif scene_nb == 0: title.draw()

        clock.tick(80)

if __name__ == '__main__':
    main()
