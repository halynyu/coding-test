
"""
AAAA로 replace 가능한 곳을 먼저 채워넣고, BB로 replace 가능한 곳을 변경한다.
"""

import sys
board = input()

board = board.replace("XXXX", "AAAA")
board= board.replace("XX", "BB")

if "X" in board:
    print(-1)

else:
    print(board)