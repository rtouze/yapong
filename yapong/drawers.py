#!/usr/bin/env python
"""Module for sprites drawers"""

import pygame
import constants

BIG = 1

class ScoreDrawer(object):
    score_table = [
            (0, 1, 3, 4, 5, 6),
            (3, 6),
            (0, 2, 3, 4, 5),
            (0, 2, 3, 5, 6),
            (1, 2, 3, 6),
            (0, 1, 2, 5, 6),
            (0, 1, 2, 4, 5, 6),
            (0, 3, 6),
            (0, 1, 2, 3, 4, 5, 6),
            (0, 1, 2, 3, 6)
            ]

    def __init__(self, screen):
        self.drawers_score_one = [
            SegmentZeroDrawer(screen, 140, 10),
            SegmentOneDrawer(screen, 140, 10),
            SegmentTwoDrawer(screen, 140, 10),
            SegmentThreeDrawer(screen, 140, 10),
            SegmentFourDrawer(screen, 140, 10),
            SegmentFiveDrawer(screen, 140, 10),
            SegmentSixDrawer(screen, 140, 10)
            ]

        self.drawers_score_two = [
            SegmentZeroDrawer(screen, 460, 10),
            SegmentOneDrawer(screen, 460, 10),
            SegmentTwoDrawer(screen, 460, 10),
            SegmentThreeDrawer(screen, 460, 10),
            SegmentFourDrawer(screen, 460, 10),
            SegmentFiveDrawer(screen, 460, 10),
            SegmentSixDrawer(screen, 460, 10)
            ]

    def draw(self, score):
        if score.player1 < 10:
            for segment in self.score_table[score.player1]:
                self.drawers_score_one[segment].draw()
        if score.player2 < 10:
            for segment in self.score_table[score.player2]:
                self.drawers_score_two[segment].draw()

class TitleDrawer(object):
    def __init__(self, screen):
        self.screen = screen
        #start_x, start_y = 10, 10
        start_x, start_y = 180, 300 - 100

        self.letters = [
            LetterY(self.screen, start_x, start_y),
            LetterA(self.screen, start_x + 50, start_y),
            LetterP(self.screen, start_x + 50*2, start_y),
            LetterO(self.screen, start_x + 50*3, start_y),
            LetterN(self.screen, start_x + 50*4, start_y),
            LetterG(self.screen, start_x + 50*5, start_y)
            ]
        
    def draw(self):
        for letter in self.letters: letter.draw()
    

class Letter(object):
    def __init__(self, screen, x_origin, y_origin, scale=BIG):
        self.long_side = 30
        self.short_side = 4
        self.x_origin = x_origin
        self.y_origin = y_origin
        self._set_coord_list()
        self.screen = screen
        self.color = constants.WHITE

    def draw(self):
        for rect in self.coord_list:
            pygame.draw.rect(self.screen, self.color, rect)

class LetterY(Letter):
    def _set_coord_list(self):
        self.coord_list = [
                [self.x_origin, self.y_origin, self.short_side, self.long_side],
                [self.x_origin,
                    self.y_origin + self.long_side - self.short_side,
                    self.long_side,
                    self.short_side],
                [self.x_origin + self.long_side - self.short_side,
                    self.y_origin,
                    self.short_side,
                    self.long_side],
                [self.x_origin + self.long_side/2 - self.short_side/2,
                    self.y_origin + self.long_side,
                    self.short_side,
                    self.long_side]
                ]

class LetterA(Letter):
    def _set_coord_list(self):
        self.coord_list = [
                [self.x_origin, self.y_origin, self.long_side, self.short_side],
                [self.x_origin, self.y_origin, self.short_side, self.long_side],
                [self.x_origin + self.long_side - self.short_side,
                    self.y_origin,
                    self.short_side,
                    self.long_side],
                [self.x_origin,
                    self.y_origin + self.long_side - self.short_side,
                    self.long_side,
                    self.short_side],
                [self.x_origin,
                    self.y_origin + self.long_side,
                    self.short_side,
                    self.long_side],
                [self.x_origin + self.long_side - self.short_side,
                    self.y_origin + self.long_side,
                    self.short_side,
                    self.long_side]
                ]

class LetterP(Letter):
    def _set_coord_list(self):
        self.coord_list = [
                [self.x_origin,
                    self.y_origin,
                    self.long_side,
                    self.short_side],
                [self.x_origin,
                    self.y_origin,
                    self.short_side,
                    self.long_side],
                [self.x_origin + self.long_side - self.short_side,
                    self.y_origin,
                    self.short_side,
                    self.long_side],
                [self.x_origin,
                    self.y_origin + self.long_side - self.short_side,
                    self.long_side,
                    self.short_side],
                [self.x_origin,
                    self.y_origin + self.long_side,
                    self.short_side,
                    self.long_side]
                ]

class LetterO(Letter):
    def _set_coord_list(self):
        self.coord_list = [
                [self.x_origin,
                    self.y_origin,
                    self.long_side,
                    self.short_side],
                [self.x_origin,
                    self.y_origin,
                    self.short_side,
                    2*self.long_side],
                [self.x_origin + self.long_side - self.short_side,
                    self.y_origin,
                    self.short_side,
                    2*self.long_side],
                [self.x_origin,
                    self.y_origin + 2*self.long_side - self.short_side,
                    self.long_side,
                    self.short_side]
                ]

class LetterN(Letter):
    def _set_coord_list(self):
        self.coord_list = [
                [self.x_origin,
                    self.y_origin,
                    self.short_side,
                    2*self.long_side],
                [self.x_origin,
                    self.y_origin,
                    self.long_side/2,
                    self.short_side],
                [self.x_origin + self.long_side/2 - self.short_side,
                    self.y_origin,
                    self.short_side,
                    self.long_side],
                [self.x_origin + self.long_side/2 - self.short_side,
                    self.y_origin + self.long_side,
                    self.short_side,
                    self.long_side],
                [self.x_origin + self.long_side/2,
                    self.y_origin + 2*self.long_side - self.short_side,
                    self.long_side/2,
                    self.short_side],
                [self.x_origin + self.long_side - self.short_side,
                    self.y_origin,
                    self.short_side,
                    2*self.long_side]
                ]

class LetterG(Letter):
    def _set_coord_list(self):
        self.coord_list = [
                [self.x_origin,
                    self.y_origin,
                    self.long_side,
                    self.short_side],
                [self.x_origin,
                    self.y_origin,
                    self.short_side,
                    2*self.long_side],
                [self.x_origin,
                    self.y_origin + 2*self.long_side - self.short_side,
                    self.long_side,
                    self.short_side],
                [self.x_origin + self.long_side - self.short_side,
                    self.y_origin + self.long_side - self.short_side,
                    self.short_side,
                    self.long_side],
                [self.x_origin + self.long_side/2,
                    self.y_origin + self.long_side - self.short_side,
                    self.long_side/2,
                    self.short_side]
                ]







class SegmentDrawer(object):
    """Base class to draw segments of the score. Bellow is segment organization.
                0
              -----
             1| 2 |3
              |---|
             4| 5 |6
              -----"""
    def __init__(self, screen, x_origin, y_origin):
        self.screen = screen
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.color = constants.WHITE
        self.long_side = 30
        self.short_side = 5
        self.info = []

    def draw(self):
        self.set_info()
        pygame.draw.rect(self.screen, self.color, self.info)

    def get_info(self):
        return []

class SegmentZeroDrawer(SegmentDrawer):
    def set_info(self):
        self.info = [
                self.x_origin,
                self.y_origin,
                self.long_side + self.short_side,
                self.short_side
                ]

class SegmentOneDrawer(SegmentDrawer):
    def set_info(self):
        self.info = [
                self.x_origin,
                self.y_origin,
                self.short_side,
                self.long_side 
                ]

class SegmentTwoDrawer(SegmentDrawer):
    def set_info(self):
        self.info = [
                self.x_origin,
                self.y_origin + self.long_side - self.short_side,
                self.long_side + self.short_side,
                self.short_side
                ]

class SegmentThreeDrawer(SegmentDrawer):
    def set_info(self):
        self.info = [
                self.x_origin + self.long_side,
                self.y_origin,
                self.short_side,
                self.long_side 
                ]

class SegmentFourDrawer(SegmentDrawer):
    def set_info(self):
        self.info = [
                self.x_origin,
                self.y_origin + self.long_side,
                self.short_side,
                self.long_side + self.short_side
                ]

class SegmentFiveDrawer(SegmentDrawer):
    def set_info(self):
        self.info = [
                self.x_origin,
                self.y_origin + 2 * self.long_side,
                self.long_side + self.short_side,
                self.short_side
                ]
    
class SegmentSixDrawer(SegmentDrawer):
    def set_info(self):
        self.info = [
                self.x_origin + self.long_side,
                self.y_origin + self.long_side,
                self.short_side,
                self.long_side + self.short_side
                ]

