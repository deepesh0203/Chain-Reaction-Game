# alpha-beta pruning function returns best move
import copy
import random


def alpha_beta(b, depth=2, diff=None):
    alpha = -300
    beta = 300
    moves = b.valid_move()

    if diff == "easy":
        depth = 2
    if diff == "med":
        depth = 2
    if diff == "hard":
        depth = 3

    random.shuffle(moves)
    player = b.player

    b_score = -300
    best_move = moves[0]

    for pos in moves:
        board = copy.deepcopy(b)
        board.move(pos)
        b_score = max(b_score, min_value(board, depth - 1, alpha, beta, player))

        if alpha < b_score:
            alpha = b_score
            best_move = pos

        if alpha >= beta:
            break

    return best_move


def max_value(b, depth, alpha, beta, player):
    moves = b.valid_move()

    if len(moves) == 0:
        return b.cal_heuristics(player)
    if depth == 0:
        return b.cal_heuristics(player)

    b_score = -300

    for pos in moves:
        board = copy.deepcopy(b)
        board.move(pos)
        b_score = max(b_score, min_value(board, depth - 1, alpha, beta, player))

        alpha = max(alpha, b_score)

        if alpha >= beta:
            break

    return b_score


def min_value(b, depth, alpha, beta, player):
    moves = b.valid_move()

    if len(moves) == 0:
        return b.cal_heuristics(player)
    if depth == 0:
        return b.cal_heuristics(player)

    b_score = 300

    for pos in moves:
        board = copy.deepcopy(b)
        board.move(pos)
        b_score = min(b_score, max_value(board, depth - 1, alpha, beta, player))

        beta = min(beta, b_score)

        if alpha >= beta:
            break

    return b_score
