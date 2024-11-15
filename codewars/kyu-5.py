# TIC-TAC-TOE-SOLVER (5 KYU)

# 1.
# def is_solved(board):
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
#             if board[i][i] != 0: return board[i][i]
#     if board[0][0] == board[1][1] == board[2][2] or board[2][0] is board[1][1] is board[0][2]:
#         if board[1][1] != 0: return board[1][1]
    
#     for i in range(3):
#         if board[i][0] == 0 or board[i][1] == 0 or board[i][2] == 0: return -1 
#     return 0

# 2.
# def is_solved(board):
#     UNFINISHED = -1
#     DRAW = 0

#     array = [row[i] for i in range(3) for row in board]

#     combinations = [(i, i + 1, i + 2) for i in range(0, 7, 3)] + \
#                    [(i, i + 3, i + 6) for i in range(3)] + \
#                    [(0, 4, 8), (2, 4, 6)]

#     for e in combinations:
#         if array[e[0]] is array[e[1]] is array[e[2]] is not DRAW: return array[e[0]]

#     return UNFINISHED if 0 in array else DRAW