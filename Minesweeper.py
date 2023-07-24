# Minesweeper game created by ChatGPT
# This script will:
# 1. Initialize a board of the size you specify and randomly populate it with mines.
# 2. Compute and fill in the numbers for the remaining cells based on the number of mines in the surrounding cells.
# 3. Begin the game loop, where the player can enter coordinates to "dig" at.
# 4. If the player hits a mine, the game ends with a game over message. If the player hits a number or an empty cell, it reveals it and the game continues.
#
# This is a very basic version of the game, it doesn't track the number of moves or check if the player has cleared all the non-mine spaces, but it provides a good starting point if you want to expand on it.


import random

def create_board(height, width, num_mines):
    # Initialize the board
    board = [['0' for _ in range(width)] for _ in range(height)]
    # Populate the board with mines
    mines = []
    while len(mines) < num_mines:
        x = random.randint(0, height - 1)
        y = random.randint(0, width - 1)
        if (x, y) not in mines:
            board[x][y] = '*'
            mines.append((x, y))
    # Compute the numbers
    for x, y in mines:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < height and 0 <= ny < width and board[nx][ny] != '*'):
                    board[nx][ny] = str(int(board[nx][ny]) + 1)
    return board

def print_board(board, height, width):
    x = 0
    y = 0
    xLegend = "  "
     
    # create the X axis legend
    while ( x < width ):
       xLegend = xLegend + str(x) + " "
       x = x + 1 
    
    print(xLegend)
    for row in board:
        print(str(y)+" " + ' '.join(row))
        y = y + 1
        
def play_game(height, width, num_mines):
    board = create_board(height, width, num_mines)
    print_board(board, height, width)
    while True:
        print("\nEnter your move (format: x y):")
        x, y = map(int, input().split())
        if board[x][y] == '*':
            print("\nBoom! You hit a mine!\n")
            break
        elif board[x][y] != '0':
            print("\nYou're safe! You revealed a number\n")
            board[x][y] = '.'
            print_board(board, height, width)
        else:
            print("\nYou're safe! You revealed an empty spot\n")
            board[x][y] = '.'
            print_board(board, height, width)
            
if __name__ == '__main__':
    play_game(10, 10, 10)