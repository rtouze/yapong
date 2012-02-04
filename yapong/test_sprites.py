#!/usr/bin/env python

"""Test module for module 'sprites'."""

import unittest
import constants
from sprites import Racket
from sprites import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.racket = Racket(constants.SCREEN_MARGIN, 10)
        self.racket.dimension['height'] = 70
        self.racket2 = Racket(constants.SCREEN_WIDTH - constants.SCREEN_MARGIN - 10, 10)
        self.racket2.dimension['height'] = 70

        self.ball = Ball()
        self.ball.direction['y'] = 1
        self.ball.direction['x'] = 1

    def test_colision_w_racket_1(self):
        x_pos = self.racket.position['x'] + self.racket.dimension['width']
        self.ball.position['x'] = x_pos
        self.ball.position['y'] = 30 
        self.ball.direction['x'] = -1
        self.ball.set_position(self.racket, self.racket2)
        self.assertEqual(1, self.ball.direction['x'])
        self.assertEqual(x_pos + 1, self.ball.position['x'])

    def test_colision_w_racket_2(self):
        x_pos = self.racket2.position['x'] - self.ball.dimension['width']
        self.ball.position['x'] = x_pos
        self.ball.position['y'] = 30 
        self.ball.set_position(self.racket, self.racket2)
        self.assertEqual(-1, self.ball.direction['x'])
        self.assertEqual(x_pos - 1, self.ball.position['x'])

    def test_colision_on_top(self):
        y_pos = constants.SCREEN_MARGIN - 1
        self.ball.position['y'] = y_pos
        self.ball.direction['y'] = -1
        self.ball.set_position(self.racket, self.racket2)
        self.assertEqual(1, self.ball.direction['y'])
        self.assertEqual(y_pos + 1, self.ball.position['y'])

    def test_colision_on_bottom(self):
        y_pos = constants.SCREEN_HEIGHT
        y_pos -= constants.SCREEN_MARGIN
        y_pos -= self.ball.dimension['height']
        y_pos += 1
        self.ball.position['y'] = y_pos
        self.ball.direction['y'] = 1
        self.ball.set_position(self.racket, self.racket2)
        self.assertEqual(-1, self.ball.direction['y'])
        self.assertEqual(y_pos - 1, self.ball.position['y'])

    def test_reset_position(self):
        self.ball.position['x'] = 42
        self.ball.position['y'] = 69
        self.ball.direction['x'] = -1
        self.ball.reset_position()
        self.assertEqual(constants.SCREEN_WIDTH / 2 - 5, self.ball.position['x'])
        self.assertEqual(constants.SCREEN_HEIGHT / 2 - 5, self.ball.position['y'])
        self.assertEqual(1, self.ball.direction['x'])
        self.assertEqual(1, self.ball.direction['y'])

class RackerTest(unittest.TestCase):
    def setUp(self):
        self.racket = Racket(constants.SCREEN_MARGIN, constants.SCREEN_MARGIN)
        
    def test_set_position(self):
        """Tests the position update in the regular way"""
        self.racket.set_position(3)
        self.assertEqual(constants.SCREEN_MARGIN + 3, self.racket.position['y'])

    def test_limit_top(self):
        """Test that the racket cannot go beyond top limit"""
        self.racket.set_position(-3)
        self.assertEqual(constants.SCREEN_MARGIN, self.racket.position['y'])

    def test_limit_bottom(self):
        """Test that the racket cannot go beyond top limit"""
        position = constants.SCREEN_HEIGHT
        position -= constants.SCREEN_MARGIN
        position -= self.racket.dimension['height']
        self.racket.set_position(position + 1)
        self.assertEqual(position, self.racket.position['y'])

if __name__ == '__main__':
    unittest.main()
