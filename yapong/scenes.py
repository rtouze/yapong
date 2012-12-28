#!/usr/bin/env python
"""Module that contains the scenes played during the game"""

import pygame
import constants
from yapong.score import Score
from yapong.drawers import ScoreDrawer, TitleDrawer
from yapong.sprites import *
import os


def font_player(func):
    """
    Decorator to fill the screen, run passed function and class _run_loop
    method. To be used with FontScene subclasses.
    """

    def wrapped(arg):
        arg.config.background.fill((0, 0, 0))
        arg.config.screen.blit(arg.config.background, (0, 0))
        func(arg)
        arg._run_loop()
    return wrapped

class FontScene(object):
    """
    Abstract class for scenes with plain text, waiting for a key to be pressed
    to end.
    """

    def __init__(self, configuration):
        """Creates the different elements of the scene using the game
        configuration."""
        self.config = configuration
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.font_surface = self.font.render(
                "Write sth here ...",
                True,
                constants.WHITE
                )

    def play(self):
        pass

    def _run_loop(self):
        running = True
        pygame.display.flip()
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    running = False

            self.config.clock.tick(10)

class TitleScene(FontScene):
    """First scene of the game : the TITLE!"""

    def __init__(self, configuration):
        """Creates the different elements of the scene using the game
        configuration."""
        FontScene.__init__(self, configuration)

        self.font_surface = self.font.render(
                "Push a button to start...",
                True,
                constants.WHITE
                )

        self.title = TitleDrawer(self.config.screen)

    @font_player
    def play(self):
        """Plays the scene itself"""
        self.title.draw()
        self.config.screen.blit(self.font_surface, (210, 300))

class EndingScene(FontScene):
    def __init__(self, configuration):
        """Creates the different elements of the scene using the game
        configuration."""
        FontScene.__init__(self, configuration)
        self.winner_sentence = None
        self.font_surface = self.font.render(
                "Press a Key to play again.",
                True,
                constants.WHITE
                )
        sound_file = os.path.join('.', 'yapong', 'sounds', 'applause-light-02.wav')
        self.sound = pygame.mixer.Sound(sound_file)

    def set_winner(self, winner):
        self.winner_sentence = self.font.render(
                "%s wins." % str(winner),
                True,
                constants.WHITE
                )

    @font_player
    def play(self):
        rect = self.winner_sentence.get_rect()
        rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        self.config.screen.blit(self.winner_sentence, rect)
        rect = self.font_surface.get_rect()
        rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 30)
        self.config.screen.blit(self.font_surface, rect)
        self.sound.play()

class GamingScene(object):

    R1_DOWN = 1
    R1_UP = 2
    R2_DOWN = 3
    R2_UP = 4

    def __init__(self, configuration):
        self.config = configuration
        self.score = Score()
        self.score_drawer = ScoreDrawer(self.config.background)
        self.ball = Ball(*self._init_sounds())
        racket_x_position = 60
        self.racket1 = Racket(racket_x_position, constants.SCREEN_WIDTH/2 - 35)
        self.racket2 = Racket(
                constants.SCREEN_WIDTH - racket_x_position - 10,
                constants.SCREEN_WIDTH/2 - 35
                )
        self.net = Net()
        self.the_winner_is = ''

    def reset(self):
        """Use this method to reset the scene (sprite position, score,...)"""
        racket_x_position = 60
        self.racket1 = Racket(racket_x_position, constants.SCREEN_WIDTH/2 - 35)
        self.racket2 = Racket(
                constants.SCREEN_WIDTH - racket_x_position - 10,
                constants.SCREEN_WIDTH/2 - 35
                )
        self.score.reset()

    def play(self):
        y_offset_one = 0
        y_offset_two = 0

        accel_r1 = 0
        accel_r2 = 0

        previous_r1 = 0
        previous_r2 = 0

        end_game = False

        while not end_game:
            if previous_r1 == self.R1_DOWN and accel_r1 < 30:
                accel_r1 += 1
            if previous_r1 == self.R1_UP and accel_r1 > -30:
                accel_r1 -= 1
            if previous_r2 == self.R2_DOWN and accel_r2 < 30:
                accel_r2 += 1
            if previous_r2 == self.R2_UP and accel_r2 > -30:
                accel_r2 -= 1
            if previous_r1 == 0: accel_r1 = 0
            if previous_r2 == 0: accel_r2 = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        y_offset_one = -1
                        previous_r1 = self.R1_UP
                    if event.key == pygame.K_d:
                        y_offset_one = 1
                        previous_r1 = self.R1_DOWN
                    if event.key == pygame.K_UP:
                        y_offset_two = -1
                        previous_r2 = self.R2_UP
                    if event.key == pygame.K_DOWN:
                        y_offset_two = 1
                        previous_r2 = self.R2_DOWN

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_e, pygame.K_d]:
                        y_offset_one = 0
                        previous_r1 = 0
                    if event.key in [pygame.K_UP, pygame.K_DOWN]:
                        y_offset_two = 0
                        previous_r2 = 0

            # Update sprites
            self.racket1.update_position(y_offset_one, accel_r1)
            self.racket2.update_position(y_offset_two, accel_r2)
            self.ball.update_position(self.racket1, self.racket2)
            self.score.check_score(self.ball)

            # This fill call is shitty...
            self.config.background.fill((0, 0, 0))
            self.net.draw(self.config.background)
            self.score_drawer.draw(self.score)
            self.ball.draw(self.config.background)
            self.racket1.draw(self.config.background)
            self.racket2.draw(self.config.background)
            self.config.screen.blit(self.config.background, (0, 0))
            pygame.display.flip()

            self.config.clock.tick(constants.REFRESH_RATE)


            if self.score.winner != 0:
                end_game = True
                self.the_winner_is = 'Player %d' % self.score.winner


    def _init_sounds(self):
        """This functions initializes the sounds, stored in yapong/sounds, that
        will be played during the game."""
        sound_dir = os.path.join('.', 'yapong', 'sounds')
        beep_filename_1 = os.path.join(sound_dir, 'beep-7.wav')
        beep_filename_2 = os.path.join(sound_dir, 'beep-8.wav')
        sound_1 = sound_2 = None
        if os.path.isfile(beep_filename_1):
            sound_1 = pygame.mixer.Sound(beep_filename_1)
        else: print("ERROR : beep_filename_1 not found")
        if os.path.isfile(beep_filename_2):
            sound_2 = pygame.mixer.Sound(beep_filename_2)
        else: print("ERROR : beep_filename_2 not found")
        return sound_1, sound_2
