from Board import Board
from Player import Player
from TicTacToe import TicTacToe


def start_game():
    game = TicTacToe()
    board = Board()
    player_1 = Player()
    player_2 = Player()

    board.clear_board()

    player_1.name = input(f"Player 1 name: ").capitalize()
    player_2.name = input(f"Player 2 name: ").capitalize()

    player_1.symbol = 'X'
    player_2.symbol = 'O'

    while game.in_progress:
        board.draw_board()

        for player in [player_1, player_2]:
            move = int(input(f"{player.name} move: [1-9]"))

            if move not in board.board:
                board.add_element(move, player.symbol)

            if board.check_win(player.symbol):
                game.in_progress = False
                board.draw_board()
                print(f"{player.name} won!")

            if board.no_more_space():
                game.in_progress = False
                board.draw_board()
                print('DRAW')

            if not game.in_progress:
                start = input("Play again? [y/n]")
                if start == 'y':
                    start_game()
                else:
                    exit()


start_game()
