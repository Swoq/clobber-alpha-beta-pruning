import pygame

from clobber.board import Board
from clobber.constants import YELLOW, BLACK, RED, SQUARE_SIZE


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        if self.selected:
            pygame.draw.circle(self.win, (0, 255, 0), (self.selected.x, self.selected.y), 50, 5)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = YELLOW
        self.valid_moves = {}

    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        if self.selected and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
            print("Turn of Bot.")
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, RED, (col*SQUARE_SIZE + SQUARE_SIZE//2,
                                               row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = []
        if self.turn == BLACK:
            self.turn = YELLOW
        else:
            self.turn = BLACK

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def get_board(self):
        return self.board
