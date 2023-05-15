from TicTacToe import State

import sys
import random

class Player:
    def __init__(self):
        pass
    def move(self,state: State):
        """
        Make a random move.
        """

        mlist =  state.moves()
        return random.choice(mlist)
