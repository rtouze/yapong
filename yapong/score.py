#!/usr/bin/env python
"""Scoring module"""

import constants

class Score(object):
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.winner = 0 

    def check_score(self, ball):
        if ball.position['x'] < 0:
            if self.player2 < 9: self.player2 += 1
            self._update_score(ball)
            if self.player2 == 9: self.winner = 2
        if ball.position['x'] > constants.SCREEN_WIDTH:
            if self.player1 < 9: self.player1 += 1
            self._update_score(ball)
            if self.player1 == 9: self.winner = 1

    def _update_score(self, ball):
        ball.reset_position()

    def reset(self):
        self.__init__()
