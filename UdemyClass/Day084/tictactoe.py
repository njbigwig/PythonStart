tictactoe_board = {
    "1-1":" ",
    "1-2":" ",
    "1-3":" ",
    "2-1":" ",
    "2-2":" ",
    "2-3":" ",
    "3-1":" ",
    "3-2":" ",
    "3-3":" "
}

def win_check():
    if tictactoe_board["1-1"] == tictactoe_board["1-2"] == tictactoe_board["1-3"]:
        return(tictactoe_board["1-1"])
    elif tictactoe_board["2-1"] == tictactoe_board["2-2"] == tictactoe_board["2-3"]:
        return(tictactoe_board["2-1"])
    elif tictactoe_board["3-1"] == tictactoe_board["3-2"] == tictactoe_board["3-3"]:
        return(tictactoe_board["3-1"])
    elif tictactoe_board["1-1"] == tictactoe_board["2-1"] == tictactoe_board["3-1"]:
        return(tictactoe_board["1-1"])
    elif tictactoe_board["1-2"] == tictactoe_board["2-2"] == tictactoe_board["3-2"]:
        return(tictactoe_board["1-2"])
    elif tictactoe_board["1-3"] == tictactoe_board["2-3"] == tictactoe_board["3-3"]:
        return(tictactoe_board["1-3"])
    elif tictactoe_board["1-1"] == tictactoe_board["2-2"] == tictactoe_board["3-3"]:
        return(tictactoe_board["1-1"])
    elif tictactoe_board["3-1"] == tictactoe_board["2-2"] == tictactoe_board["1-3"]:
        return(tictactoe_board["3-1"])
    else:
        return(" ")
    

def print_board():
    print("\n")
    
    for row in range(1,4):
        row_str =""
        for column in range(1,4):
            #print(f"{row}-{column}")
            key = f"{row}-{column}"
            row_str += " " + tictactoe_board[key] + " "
            if column < 3:
                row_str += '|'
        print(row_str)
        if row < 3: 
            print("-----------")
            
    print("\n")
    
def player_move(playerno):
        
    valid_move = False
    
    if playerno == 1:
        player_symbol = 'O'
    else:
        player_symbol = 'X'
    
    while valid_move == False:
        pr = 0
        while pr == 0:
            pr = int(input(f"Player {playerno} ({player_symbol}) - what row?: "))
            if pr < 1 or pr > 3:
                pr = 0
          
        pc = 0
        while pc == 0:
            pc = int(input(f"Player {playerno} ({player_symbol}) - what col?: "))
            if pc < 1 or pc > 3:
                pc = 0
        
        move_key = f"{pr}-{pc}"
        
        if tictactoe_board[move_key] == ' ':
            tictactoe_board[move_key] = player_symbol
            valid_move = True  
        else:
            print("Space already selected, choose again...")  
            
    print_board() 
    
    return win_check() 


game_over = False

while game_over == False:    
    
    player = 1
    while player < 3 and game_over == False: 
        game_check = player_move(player)  
    
        if game_check != " ":
            print(f"Player {game_check} WON!")
            game_over = True
        else:
            player += 1
       
    
 
    
