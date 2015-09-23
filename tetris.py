import pygame
import random


class Tetromino(object):

    # create peice shapes
    oPeice = [[[1, 1],
               [1, 1]]
               ]

    zPeice = [[[1, 1, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],

              [[0, 1, 0, 0],
               [1, 1, 0, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 0]
               ]
              ]

    lPeice = [[[1, 1, 1, 1],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],
            
               [[1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0]]
               ]

    tPeice = [[[1, 1, 1, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],

               [[1, 0, 0, 0],
                [1, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 0]],

               [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]],

               [[0, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
              ]

    sPeice = [[[0, 1, 1, 0],
               [1, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],

               [[1, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]
               ]

    peices = [oPeice, zPeice, lPeice, tPeice, sPeice]

    def __init__(self):

        self.shape = random.choice(self.peices)
        self._x = 0
        self._y = 0

    def rotate(self):
        """rotates a peice"""
        pass

    @property
    def topLeft(self):
        return (self._x, self._y)

    @topLeft.setter
    def topLeft(self, value):
        self._x = value[0]
        self._y = value[1]


class Board():

    def __init__(self, screen):
        self.colors = {1: pygame.Color(255, 0, 0, 0),
                       2: pygame.Color(0, 255, 0, 0),
                       3: pygame.Color(0, 0, 255, 0),
                       4: pygame.Color(0, 255, 255, 0),
                       5: pygame.Color(255, 255, 0, 0),
                       0: pygame.Color(0, 0, 0, 0)
                       }
        self.screen = screen
        self.color = pygame.Color(255, 0, 0)
        self.tileSize = 50
        self.width = 10
        self.height = 18
        self.grid = [[0 for i in range(self.height)]
                     for i in range(self.width)]

    @property
    def grid(self):
        return self.grid[:]

    # Is this a better implementation than a setter function?
    @grid.setter
    def grid(self, x, y, val):
        self.grid[x][y] = val

    def update(self):
        """Board update meathod"""
        if not activePeice:
            self.addPeice()
        self.draw()

    def draw(self):
        """Board draw meathod"""
        self.drawBoard()

    def drawBoard(self):
        """Draw the game board and peices"""
        for x, col in enumerate(self.grid):
            for y, row in enumerate(col):
                # draw tile
                self.paintTile(x, y)
    
    def paintTile(self, x, y):
        """Paints board tile (x, y)"""
        left = x * self.tileSize
        top = y * self.tileSize
        color = self.colors[self.grid[x][y]]
        pygame.draw.rect(self.screen, color,
                         (left, top, self.tileSize, self.tileSize))

    def addPeice(self):
        """Adds a tetromino to the board"""
        self.peice = Tetromino()
        self.peice.topLeft = (5, 0)

    def drawPeice(self):
        """Draws the current active peice"""
        for x, col in enumerate(self.peice.shape):
            for y, row in enumerate(col):
                pass

    def rotate(self):
        """Rotates the active game peice"""
        pass

    def checkLines(self):
        """Checks for compleated lines"""
        for line in self.grid:
            if 0 not in line:
                pass

    def clearRow(self):
        """Clears a row"""
        pass


class Tetris():

    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((500, 900))
        self.board = Board(self.screen)

    def update(self):
        while True:
            self.board.update()
            pygame.display.update()
            pygame.time.delay(30)

if __name__ == '__main__':
    t = Tetris()
    t.update()
