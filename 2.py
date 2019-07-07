"""
This program takes a Tic-Tac-Toe game pattern (9 chars of [xo.]), and checks if there is a winner.
"""

import re


def is_winner(game_pattern):
    return (re.search(r'^(.{3})*(x{3}|o{3})', game_pattern) or
            re.search(r'^.{0,2}([xo])..\1..\1.?', game_pattern) or
            re.search(r'([xo])...\1...\1|..([xo]).\2.\2..', game_pattern))


if is_winner(input("Please enter the game pattern")):
    print("Yay! There is a winner!")
else:
    print("Oops, no winner this time :(")
