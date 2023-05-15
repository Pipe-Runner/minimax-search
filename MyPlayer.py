from TicTacToe import State

import sys
import random

"""
even depth is our turn so we decide based on max
odd depth is their turn so we decide based on min
"""
WIN_SCORE = 10
LOSE_SCORE = -10
DRAW_SCORE = 0


def score_fn(base, number_of_moves_left) -> int:
    return (number_of_moves_left + 1) * base


memory = {}


def pick_best(state: State, depth=0):
    if state.key() in memory:
        _, best_move, best_score = memory[state.key()]
        return best_move, best_score

    is_my_move = depth % 2 == 0

    # get a list of moves to generate children
    move_list = state.moves()
    stateK_move_score_list = []

    score_fn = max if is_my_move else min

    for move in move_list:
        # make a copy of the state and make the move
        new_state = state.moveCopy(move)
        number_of_moves_left = new_state.key().count(".")

        # if the move wins the game
        if new_state.isWin() is not None:
            stateK_move_score_list.append(
                (
                    new_state.key(),
                    move,
                    score_fn(
                        WIN_SCORE if is_my_move else LOSE_SCORE,
                        number_of_moves_left,
                    ),
                )
            )
        # if the move is a draw
        elif number_of_moves_left == 0:
            stateK_move_score_list.append(
                (
                    new_state.key(),
                    move,
                    score_fn(
                        DRAW_SCORE,
                        number_of_moves_left,
                    ),
                )
            )
        # if the move is neither a win or a draw
        else:
            _, score = pick_best(new_state, depth + 1)
            stateK_move_score_list.append(
                (
                    new_state.key(),
                    move,
                    score,
                )
            )
    
    best_move_and_score = score_fn(stateK_move_score_list, key=lambda x: x[2])

    # store the best move and score in memory
    memory[state.key()] = best_move_and_score
    # print(best_move_and_score)

    return best_move_and_score[1], best_move_and_score[2]


class Player:
    def __init__(self):
        pass

    def move(self, state: State):
        """
        Make a random move.
        """
        move, _ = pick_best(state)
        return move
