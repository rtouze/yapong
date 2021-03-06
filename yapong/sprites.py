#!/usr/bin/env python
""" This module cares about pong sprites (ball, rackets)"""

import config
import constants
import pygame
import random

class Ball(object):
    """Defines ball object's behaviour."""
    def __init__(self, sound_1=None, sound_2=None):
        self.color = constants.WHITE
        self.dimension = {'width': 10, 'height': 10}
        self.direction = {'x': 1, 'y': 1}
        self.position = {'x': 0, 'y': 0}
        speed = config.BALL_SPEED
        self.speeds = {'x': speed, 'y': speed}
        self.sound_1 = sound_1
        self.sound_2 = sound_2

    def update_position(self, racket_1, racket_2):
        """Define next position of the ball, depending on rackets
        information"""
        if self._hit_racket_1(racket_1):
            if self.sound_1: self.sound_1.play()
            self.direction['x'] *= -1
            self.speeds['y'] = racket_1.acceleration

        if self._hit_racket_2(racket_2):
            if self.sound_2: self.sound_2.play()
            self.direction['x'] *= -1
            self.speeds['y'] = racket_2.acceleration

        if self._hit_top() or self._hit_bottom():
            self.direction['y'] *= -1

        self.position['x'] += self.speeds['x'] * self.direction['x']
        self.position['y'] += self.speeds['y'] * self.direction['y']

    def _hit_racket_1(self, racket):
        """Tests if the ball hits racket 1"""
        hit_x_position_base = racket.position['x'] + racket.dimension['width']
        return self._hit_a_racket(racket, hit_x_position_base) \
                and self.direction['x'] == -1

    def _hit_racket_2(self, racket):
        """Tests if the ball hits racket 2"""
        hit_x_position_base = racket.position['x'] - self.dimension['width']
        return self._hit_a_racket(racket, hit_x_position_base) \
                and self.direction['x'] == 1

    def _hit_a_racket(self, racket, hit_x_position_base):
        """Tests if the ball hits a racket object. This methods should be used
        by _hit_racket_1 and _hit_racket_2 only."""
        hit_x_position_low = hit_x_position_base - self.speeds['x']/2 
        hit_x_position_high = hit_x_position_base + self.speeds['x']/2 
        return self._hit_height(racket) \
                and self.position['x'] >= hit_x_position_low \
                and self.position['x'] <= hit_x_position_high \

    def _hit_top(self):
        top = constants.SCREEN_MARGIN 
        return self.position['y'] < top and self.direction['y'] == -1

    def _hit_bottom(self):
        bottom = constants.SCREEN_HEIGHT
        bottom -= constants.SCREEN_MARGIN
        bottom -= self.dimension['height']
        return self.position['y'] > bottom and self.direction['y'] == 1

    def _hit_height(self, racket):
        """Tests if the ball is high enough to hit a racket"""
        return self.position['y'] > racket.position['y'] - self.dimension['height'] \
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
        """Resets ball position on screen when one of the player win the
        point. Ball direction is chosen randomly, which is soooo much exciting!"""
        self.position['x'] = constants.SCREEN_WIDTH / 2
        self.position['x'] -= self.dimension['width'] / 2
        self.position['y'] = constants.SCREEN_HEIGHT / 2
        self.position['y'] -= self.dimension['height'] / 2
        self.direction['x'] = random.choice((-1, 1))
        self.direction['y'] = random.choice((-1, 1))
        self.speeds['x'] = config.BALL_SPEED
        self.speeds['y'] = config.BALL_SPEED

class Racket(object):
    """Definition for racket object. That's the rectangle that have to hit the
    ugly square that we call the BALL"""
    def __init__(self, initial_x, initial_y):
        self.color = constants.WHITE
        self.dimension = {'width': 10, 'height': config.RACKET_HEIGHT}
        self.position = {'x': initial_x, 'y': initial_y}
        self.acceleration = 1

    def update_position(self, y_offset, acceleration=30):
        min_y = constants.SCREEN_MARGIN
        max_y = constants.SCREEN_HEIGHT
        max_y -= constants.SCREEN_MARGIN 
        max_y -= self.dimension['height']

        self.acceleration = (abs(acceleration)/10 + 1)

        if self.position['y'] + y_offset < min_y:
            self.position['y'] = min_y
        elif self.position['y'] + y_offset > max_y:
            self.position['y'] = max_y
        else:
            self.position['y'] += y_offset * self.acceleration

    def draw(self, screen):
        info = [
                self.position['x'],
                self.position['y'],
                self.dimension['width'],
                self.dimension['height']
                ]
        pygame.draw.rect(screen, self.color, info)

class Net(object):
    """Line that split the screen. It's animation is insane, believe me"""
    def __init__(self):
        self.segment_length = 20
        self.color = constants.WHITE
        self.width = 5

    def draw(self, screen):
        x = constants.SCREEN_WIDTH/2 - self.width/2
        y = 0
        info = []

        while y < constants.SCREEN_HEIGHT:
            info = [x, y, self.width, self.segment_length]
            pygame.draw.rect(screen, self.color, info)
            y += self.segment_length*2

