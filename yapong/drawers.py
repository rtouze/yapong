#!/usr/bin/env python
"""Module for sprites drawers"""

import pygame
import constants

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

