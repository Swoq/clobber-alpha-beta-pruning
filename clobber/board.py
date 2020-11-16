import pygame

from clobber.constants import GREY, ROWS, WHITE, SQUARE_SIZE, COLS, YELLOW, BLACK
from clobber.piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.create_board()

    def draw_squares(self, win):
        win.fill(GREY)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE,
                                              SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    self.board[row].append(Piece(row, col, YELLOW))
                else:
                    self.board[row].append(Piece(row, col, BLACK))

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = 0, self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        moves = []

        # left
        if piece.col != 0:
            watch_p = self.board[piece.row][piece.col - 1]
            if watch_p != 0 and watch_p.color != piece.color:
                moves.append((watch_p.row, watch_p.col))

        # top
        if piece.row != 0:
            watch_p = self.board[piece.row - 1][piece.col]
            if watch_p != 0 and watch_p.color != piece.color:
                moves.append((watch_p.row, watch_p.col))

        # right
        if piece.col != len(self.board[piece.row]) - 1:
            watch_p = self.board[piece.row][piece.col + 1]
            if watch_p != 0 and watch_p.color != piece.color:
                moves.append((watch_p.row, watch_p.col))

        # down
        if piece.row != len(self.board) - 1:
            watch_p = self.board[piece.row + 1][piece.col]
            if watch_p != 0 and watch_p.color != piece.color:
                moves.append((watch_p.row, watch_p.col))

        return moves

    def evaluate(self):
        amount_of_yellow = 0
        amount_of_black = 0

        for row in self.board:
            for piece in row:
                if piece == 0:
                    continue
                if piece.color == YELLOW:
                    if not self.is_dead(piece):
                        amount_of_yellow += 1
                else:
                    if not self.is_dead(piece):
                        amount_of_black += 1

        return amount_of_yellow - amount_of_black

    def is_dead(self, piece):
        # left
        if piece.col != 0:
            watch_p = self.board[piece.row][piece.col - 1]
            if watch_p != 0:
                return False

        # top
        if piece.row != 0:
            watch_p = self.board[piece.row - 1][piece.col]
            if watch_p != 0:
                return False

        # right
        if piece.col != len(self.board[piece.row]) - 1:
            watch_p = self.board[piece.row][piece.col + 1]
            if watch_p != 0:
                return False

        # down
        if piece.row != len(self.board) - 1:
            watch_p = self.board[piece.row + 1][piece.col]
            if watch_p != 0:
                return False

        return True

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def winner(self):
        for row in self.board:
            for piece in row:
                if piece != 0:
                    if len(self.get_valid_moves(piece)) != 0:
                        return None

        return BLACK
