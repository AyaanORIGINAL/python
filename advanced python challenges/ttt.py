board = [' ' for _ in range(9)]

def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def check_winner(player):
    winconds =[
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for cond in winconds: 
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

def play_game():
    currentplayer = "X"
    for turn in range(1, 10):
        print_board()
        move = int(input(f"Player {currentplayer}, enter your move (1-9):")) - 1
        if board[move] == ' ':
            board[move] = currentplayer
        else:
            print("Spot is taken, Try again")
            continue
        if check_winner(currentplayer):
            print_board()
            print(f"Player {currentplayer} wins!")
            return
        currentplayer = "O" if currentplayer == "X" else "X"
    print_board()
    print("It's a tie!")
play_game()
