#!/usr/bin/env python
"""Scoring module"""

import constants

class Score(object):
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.updated = False

    def check_score(self, ball):
        if ball.position['x'] < 0:
            if self.player2 < 9: self.player2 += 1
            self._update_score(ball)
        if ball.position['x'] > constants.SCREEN_WIDTH:
            if self.player1 < 9: self.player1 += 1
            self._update_score(ball)

    def _update_score(self, ball):
        self.updated = True
        ball.reset_position()
