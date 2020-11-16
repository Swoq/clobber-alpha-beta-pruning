from copy import deepcopy
import pygame

from clobber.constants import BLACK, YELLOW


def minimax(position, depth, max_player, i_alfa, i_beta, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        alfa = i_alfa
        beta = i_beta
        best_move = None
        for move in get_all_moves(position, YELLOW, game):
            if alfa >= beta:
                print(f"Cut: A: {alfa} B: {beta}")
                break
            evaluation = minimax(move, depth - 1, False, alfa, beta, game)[0]
            alfa = max(alfa, evaluation)
            if alfa == evaluation:
                best_move = move

        return alfa, best_move
    else:
        alfa = i_alfa
        beta = i_beta
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            if alfa >= beta:
                print(f"Cut: A: {alfa} B: {beta}")
                break
            evaluation = minimax(move, depth - 1, True, alfa, beta, game)[0]
            beta = min(beta, evaluation)
            if beta == evaluation:
                best_move = move

        return beta, best_move


def simulate_move(piece, move, board):
    board.move(piece, move[0], move[1])

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move in valid_moves:
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board)
            moves.append(new_board)

    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves)
    pygame.display.update()
    pygame.time.delay(10)
