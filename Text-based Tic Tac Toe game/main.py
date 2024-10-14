# Text-based Tic Tac Toe game for two players.

def display_board(board):
    # Display the current state of the board
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def player_input(player, board):
    # Get valid move from player
    while True:
        try:
            pos = int(input(f"Player {player}, choose your move (1-9): ")) - 1
            if pos not in range(9):
                print("Invalid position. Choose 1-9.")
            elif board[pos] != ' ':
                print("Position already taken.")
            else:
                board[pos] = player
                break
        except ValueError:
            print("Please enter a number.")

def check_win(board, player):
    # Check all win conditions
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    # Check if the board is full
    return all(space != ' ' for space in board)

def switch_player(current):
    # Switch between players
    return 'O' if current == 'X' else 'X'

def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    while True:
        display_board(board)
        player_input(current_player, board)
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        current_player = switch_player(current_player)

if __name__ == "__main__":
    main()
