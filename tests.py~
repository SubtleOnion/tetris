import pygame
from tetris import *
import unittest


class TetrisTest(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 600))
        self.board = Board(self.screen)

    def test_grid(self):
        self.board.grid[0][0] = 1

if __name__ == '__main__':
    unittest.main()
