# from random import randrange

# def display_board(board):
#     # The function accepts one parameter containing the board's current status
#     # and prints it out to the console.
#     print("+-------+-------+-------+")
#     for i in range(3):
#         print(f"""
#         |       |       |       |
#         |   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |
#         |       |       |       |
#         +-------+-------+-------+""")


# def enter_move(board):
#     index_to_position = {1: board[0][0], 2: board[0][1], 3: board[0][2],
#                          4: board[1][0], 5: board[1][1], 6: board[1][2],
#                          7: board[1][0], 8: board[2][1], 9: board[2][2],}
#     try:
#         user_move_not_done = True
#         while user_move_not_done:
            
#             user_choice = int(input("Enter your move: "))
            
#             if str(index_to_position[user_choice]) == "X" or str(index_to_position[user_choice]) == "O": print("This position is already taken!")
#             elif str(index_to_position[user_choice]) != "X":
#                 for row in board:
#                     for column in row:
#                         if user_choice == column:
#                             board[board.index(row)][row.index(column)] = "O"
#                             user_move_not_done = False
    
#     except ValueError:
#         print("Use integer value to make your next move.")
#         enter_move(playing_board)

#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.

#     list_of_free_fields = []

#     for row in board:
#         for column in row:
#             if column not in ["X", "O"]:
#                 list_of_free_fields.append((board.index(row), row.index(column)))
    
#     return list_of_free_fields



# def victory_for(board):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2]: return board[i][0]
#         elif board[0][i] == board[1][i] == board[2][i]: return board[0][i]
#         elif board[0][0] == board[1][1] == board[2][2]: return board[0][0]
#         elif board[0][2] == board[1][1] == board[1][0]: return board[1][0]
#         else: return False


# def draw_move(board):
#     # The function draws the computer's move and updates the board.

#     index_to_position = {1: board[0][0], 2: board[0][1], 3: board[0][2],
#                          4: board[1][0], 5: board[1][1], 6: board[1][2],
#                          7: board[2][0], 8: board[2][1], 9: board[2][2],}
    
#     move_not_done = True
#     while move_not_done:
#         choice = randrange(10)
#         if str(index_to_position[choice]) == "X" or str(index_to_position[choice]) == "O": print("This position is already taken!")
#         else:
#             for row in board:
#                 for column in row:
#                     if choice == column:
#                         board[board.index(row)][row.index(column)] = "X"
#                         move_not_done = False
#     display_board(playing_board)
    

#     return

# playing_board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
# display_board(playing_board)


# while make_list_of_free_fields(playing_board):
#     enter_move(playing_board)
#     draw_move(playing_board)
    
#     if victory_for(playing_board):
#         print(victory_for(playing_board), "wins the game!")
#         break




"""" 2ND VERSION """

from random import randrange


def display_board(board):
    for row in board: print(*row)


def enter_move(board):
    while True:
        try:
            player_move = int(input("Your move: "))
            if 1 <= player_move <= 9 and isinstance(board[(player_move-1)//3][(player_move-1)%3], int):
                board[(player_move-1)//3][(player_move-1)%3] = "O"
                break
            else:
                print("This position has been already taken!")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")


def make_list_of_free_fields(board): 
    return [(row, col) for row in range(3) for col in range(3) if isinstance(board[row][col], int)]


def victory_for(board):
        for i in range(3):
            if board[i][0] is board[i][1] is board[i][2]: return board[i][0]
            if board[0][i] is board[1][i] is board[2][i]: return board[0][i]
        if board[0][0] is board[1][1] is board[2][2]: return board[0][0]
        if board[2][0] is board[1][1] is board[0][2]: return board[2][0]
        return False


def draw_move(board):
    row, col = make_list_of_free_fields(board)[randrange(len(make_list_of_free_fields(board)))]
    board[row][col] = "X"
    
current_board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

while True:
    display_board(current_board)
    if not make_list_of_free_fields(current_board):
        print("Draw!")
        break
    enter_move(current_board)
    if victory_for(current_board):
        display_board(current_board)
        print(f"{victory_for(current_board)} wins the game!")
        break
    draw_move(current_board)
    if victory_for(current_board):
        display_board(current_board)
        print(f"{victory_for(current_board)} wins the game!")
        break