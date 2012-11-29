#!/usr/bin/env python
""" Pong clone game using Python """

import pygame
from pygame.locals import *
from pygame.time import Clock
from yapong import constants
from yapong.sprites import *
from yapong.score import Score
from yapong.drawers import ScoreDrawer, TitleDrawer
import os

__author__ = 'romain.touze@gmail.com'

R1_DOWN = 1
R1_UP = 2
R2_DOWN = 3
R2_UP = 4

def main():
    """Main part of the app, with the different scenes and so on."""

    pygame.init()

    screenRes = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenRes, 0, 32)
    pygame.display.set_caption("Yapong")
    background = pygame.Surface(screen.get_size())
    clock = Clock()

    scene_nb = 0 # first scene by default
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    font_surface = font.render("Push a button to start...", True, constants.WHITE)

    title = TitleDrawer(background)
    title.draw()
    screen.blit(background, (0, 0))

    pygame.display.flip()

    countdown = 0
    title_not_shown = True

    # Scene 1
    while scene_nb == 0:
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and not title_not_shown: scene_nb += 1

        if countdown > 20 and title_not_shown:
            background.blit(font_surface, (210,300))
            screen.blit(background, (0, 0))
            pygame.display.flip()
            title_not_shown = False

        countdown += 1
        clock.tick(10)

    # Scene 2
    y_offset_one = 0
    y_offset_two = 0

    score = Score()
    score_drawer = ScoreDrawer(background)

    ball = Ball(*init_sounds())
    racket_x_position = 60
    racket1 = Racket(racket_x_position, constants.SCREEN_WIDTH/2 - 35)
    racket2 = Racket(
            constants.SCREEN_WIDTH - racket_x_position - 10,
            constants.SCREEN_WIDTH/2 - 35
            )

    net = Net()

    accel_r1 = 0
    accel_r2 = 0

    previous_r1 = 0
    previous_r2 = 0

    background.fill((0, 0, 0))
    net.draw(background)
    pygame.display.flip()

    while scene_nb == 1:

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

        if event.type == pygame.QUIT:
            exit()

        for event in pygame.event.get():
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

        # Update sprites
        racket1.update_position(y_offset_one, accel_r1)
        racket2.update_position(y_offset_two, accel_r2)
        ball.update_position(racket1, racket2)
        score.check_score(ball)

        background.fill((0, 0, 0))
        net.draw(background)
        score_drawer.draw(score)
        ball.draw(background)
        racket1.draw(background)
        racket2.draw(background)
        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock.tick(constants.REFRESH_RATE)

def init_sounds():
    """This functions initializes the sounds, stored in yapong/sounds, that
    will be played during the game."""
    sound_dir = os.path.join('.', 'yapong', 'sounds')
    beep_filename_1 = os.path.join(sound_dir, 'beep-7.wav')
    beep_filename_2 = os.path.join(sound_dir, 'beep-7.wav')
    sound_1 = sound_2 = None
    if os.path.isfile(beep_filename_1):
        sound_1 = pygame.mixer.Sound(beep_filename_1)
    if os.path.isfile(beep_filename_2):
        sound_2 = pygame.mixer.Sound(beep_filename_2)
    return sound_1, sound_2


if __name__ == '__main__':
    main()
