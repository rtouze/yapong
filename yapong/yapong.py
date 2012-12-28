#!/usr/bin/env python
""" Pong clone game using Python """

import pygame
from pygame.locals import *
from pygame.time import Clock
from yapong import constants
import yapong.scenes as scenes

__all__ = ['main']

class GameConfiguration():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Yapong")

        screenRes = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(screenRes, 0, 32)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0 ,0))
        self.clock = Clock()

def main():
    """Main part of the app, with the different scenes and so on."""

    config = GameConfiguration()

    title_scene = scenes.TitleScene(config)
    play_scene = scenes.GamingScene(config)
    ending_scene = scenes.EndingScene(config)

    title_scene.play()

    while True:
        play_scene.play()
        ending_scene.set_winner(play_scene.the_winner_is)
        ending_scene.play()
        play_scene.reset()

if __name__ == '__main__':
    main()
