board = [["-" for row in range(8)] for column in range(8)]
board[0][0], board[0][7], board[7][0], board[7][7] = "R", "R", "R", "R"
board[0][1], board[0][6], board[7][1], board[7][6] = "N", "N", "N", "N"
board[0][2], board[0][5], board[7][2], board[7][5] = "B", "B", "B", "B"
board[0][3], board[7][3] = "K", "K"
board[0][4], board[7][4] = "Q", "Q"
for p in range(len(board)):
    board[1][p], board[6][p] = "P", "P"
for i in range(len(board)):
    print(board[i])

input("Press enter to exit")