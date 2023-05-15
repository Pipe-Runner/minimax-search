#! /usr/bin/env python3

import TicTacToe as ttt
from Player import Player 
from MyPlayer import Player as MPlayer

g = ttt.Game()
g.play(Player(),MPlayer())
