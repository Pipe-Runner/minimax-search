#! /usr/bin/env python3

import TicTacToe as ttt
from Template import Player as TPlayer
from MyPlayer import Player as MPlayer

g = ttt.Game()
g.play(TPlayer(), MPlayer())
