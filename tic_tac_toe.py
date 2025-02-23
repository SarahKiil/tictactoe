import math
import random
import time

BLUE = "\033[34m"
RED = "\033[31m"
BLACK = "\033[30m"
PINK = "\033[95m"
RESET = "\033[0m"

# Globale statistikvariabler
wins = 0
losses = 0
draws = 0

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

                row.append(f"{BLACK}{cell}{RESET}")

        print(f"{PINK} | {RESET}".join(row))
        if i < 2:
            print(f"{PINK}--+---+--{RESET}")

def check_winner(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rækker
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # kolonner
        (0, 4, 8), (2, 4, 6)              # diagonaler
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
            board[move] = move + 1  # nulstil træk
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
            board[move] = move + 1  # nulstil træk
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
        board[move] = move + 1  # nulstil træk
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def replay_game(moves):
    # Genskab brættet og afspil hvert træk med en lille pause
    board = [i + 1 for i in range(9)]
    print("\nReplaying game:")
    for move_entry in moves:
        player, move, board_state = move_entry
        board[move] = board_state[move]  # opdater brættet med trækets symbol
        print_board(board)
        time.sleep(1)  # Pause 1 sekund mellem træk
        print("\n")
    print("Replay finished.\n")

def play_game():
    global wins, losses, draws

    board = [i + 1 for i in range(9)]
    moves = []  # Liste til at gemme spillets bevægelser
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

                moves.append(("Player", move, board.copy()))
                turn = "ai"
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        else:
            print("AI is making a move...")
            move = ai_move(board, ai_symbol, player_symbol)
            board[move] = ai_symbol
            moves.append(("AI", move, board.copy()))
            turn = "player"

    print_board(board)
    if winner:
        if winner == player_symbol:
            print("Congratulations, you win!")
            wins += 1
        else:
            print("AI wins. Better luck next time!")
            losses += 1
    else:
        print("It's a tie!")
        draws += 1

    # Udskriv statistik
    print("\n--- Statistics ---")
    print(f"Wins: {wins} | Losses: {losses} | Draws: {draws}")
    print("------------------\n")


    replay = input("Do you want to see a replay of the game? (y/n): ").lower()
    if replay == 'y':
        replay_game(moves)

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()