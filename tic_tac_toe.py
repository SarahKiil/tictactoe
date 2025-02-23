import math
import random

BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"

def print_board(board):
    for i in range(3):
        row = []
        for j in range(3):
            cell = board[i * 3 + j]
            if cell == "X":
                row.append(f"{BLUE}X{RESET}")
            elif cell == "O":
                row.append(f"{RED}O{RESET}")
            else:
                row.append(str(cell))
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")

def check_winner(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] in ["X", "O"]:
            return board[a]
    return None

def available_moves(board):
    return [i for i in range(9) if isinstance(board[i], int)]

def minimax(board, depth, is_maximizing, ai_player, human_player, alpha=-math.inf, beta=math.inf):
    winner = check_winner(board)
    if winner == ai_player:
        return 10 - depth
    elif winner == human_player:
        return depth - 10
    elif not available_moves(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = ai_player
            score = minimax(board, depth + 1, False, ai_player, human_player, alpha, beta)
            board[move] = move + 1  # reset move
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # beta cut-off
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = human_player
            score = minimax(board, depth + 1, True, ai_player, human_player, alpha, beta)
            board[move] = move + 1  # reset move
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break  # alpha cut-off
        return best_score

def ai_move(board, ai_player, human_player):
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move] = ai_player
        score = minimax(board, 0, False, ai_player, human_player, -math.inf, math.inf)
        board[move] = move + 1  # reset move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [i + 1 for i in range(9)]
    player_symbol = ""
    while player_symbol not in ["X", "O"]:
        player_symbol = input("Choose your symbol (X or O): ").upper()
    ai_symbol = "O" if player_symbol == "X" else "X"

    if player_symbol == "X":
        print(f"You are {BLUE}X{RESET} and AI is {RED}O{RESET}")
    else:
        print(f"You are {RED}O{RESET} and AI is {BLUE}X{RESET}")

    # Tilfældig start: enten player eller ai starter
    turn = random.choice(["player", "ai"])
    print(f"{turn.capitalize()} will start the game!")

    winner = None
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner or not available_moves(board):
            break

        if turn == "player":
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move not in available_moves(board):
                    print("Invalid move. Please try again.")
                    continue
                board[move] = player_symbol
                turn = "ai"
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        else:
            print("AI is making a move...")
            move = ai_move(board, ai_symbol, player_symbol)
            board[move] = ai_symbol
            turn = "player"

    print_board(board)
    if winner:
        if winner == player_symbol:
            print("Congratulations, you win!")
        else:
            print("AI wins. Better luck next time!")
    else:
        print("It's a tie!")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()