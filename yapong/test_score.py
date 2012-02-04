#!/usr/bin/env python
"""Test module fore score.py """
import unittest

from score import Score
from sprites import Ball
import constants

class TestScore(unittest.TestCase):
    def setUp(self):
        self.score = Score()

    def test_initial_score(self):
        self.assertEqual(0, self.score.player1)
        self.assertEqual(0, self.score.player2)

    def test_inc_play2(self):
        ball = Ball()
        ball.position['x'] = -1
        self.score.check_score(ball)
        self.assertEqual(0, self.score.player1)
        self.assertEqual(1, self.score.player2)
        self.checkFinalPosition(ball)

    def checkFinalPosition(self, ball):
        final_position = constants.SCREEN_WIDTH / 2 - ball.dimension['width'] / 2
        self.assertEqual(final_position, ball.position['x'])

    def test_inc_play1(self):
        ball = Ball()
        ball.position['x'] = constants.SCREEN_WIDTH + 1
        self.score.check_score(ball)
        self.assertEqual(1, self.score.player1)
        self.assertEqual(0, self.score.player2)
        self.checkFinalPosition(ball)

if __name__ == '__main__':
    unittest.main()
