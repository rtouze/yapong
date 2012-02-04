#!/usr/bin/env python
""" This module cares about pong sprites (ball, rackets)"""

import constants
import pygame

class Ball(object):
    def __init__(self):
        self.color = constants.WHITE
        self.dimension = {'width': 10, 'height': 10}
        self.direction = {'x': 1, 'y': 1}
        self.position = {'x': 0, 'y': 0}

    def set_position(self, racket_1, racket_2):
        """Define next position of the ball, depending on rackets
        information"""
        if self._hit_racket_1(racket_1) or self._hit_racket_2(racket_2):
            self.direction['x'] *= -1

        if self._hit_top() or self._hit_bottom():
            self.direction['y'] *= -1

        self.position['x'] += 1 * self.direction['x']
        self.position['y'] += 1 * self.direction['y']

    def _hit_racket_1(self, racket):
        """Tests if the ball hits racket 1"""
        return self._is_hit_height(racket) \
                and self.position['x'] == racket.position['x'] + \
                racket.dimension['width'] \
                and self.direction['x'] == -1

    def _hit_racket_2(self, racket):
        """Tests if the ball hits racket 2"""
        return self._is_hit_height(racket) \
                and self.position['x'] == racket.position['x'] \
                and self.direction['x'] == 1

    def _hit_top(self):
        top = constants.SCREEN_MARGIN 
        return self.position['y'] < top and self.direction['y'] == -1

    def _hit_bottom(self):
        bottom = constants.SCREEN_HEIGHT - constants.SCREEN_MARGIN
        return self.position['y'] > bottom and self.direction['y'] == 1

    def _is_hit_height(self, racket):
        """Tests if the ball is high enough to hit a racket"""
        return self.position['y'] > racket.position['y'] \
                and self.position['y'] < racket.position['y'] + \
                racket.dimension['height']

    def draw(self, screen):
        ball_info = [
                self.position['x'],
                self.position['y'],
                self.dimension['width'],
                self.dimension['height']
                ]
        pygame.draw.rect(screen, self.color, ball_info)

    def reset_position(self):
        pass

class Racket(object):
    def __init__(self, initial_x, initial_y):
        self.color = constants.WHITE
        self.dimension = {'width': 10, 'height': 70}
        self.position = {'x': initial_x, 'y': initial_y}

    def draw(self, screen):
        info = [
                self.position['x'],
                self.position['y'],
                self.dimension['x'],
                self.dimension['y']
                ]
        pygame.draw.rect(screen, self.color, info)

