class Board:
    def __init__(self):
        self.board = []
        self.win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

    def clear_board(self):
        self.board = ['', '', '', '', '', '', '', '', '']

    def add_element(self, position, mark):
        self.board[position-1] = mark

    def draw_board(self):
        i = 1
        for cell in self.board:
            if cell == '':
                print("|   ", end="")
            else:
                print(f"| {cell} ", end="")
            if i % 3 == 0:
                print("|")
                if i < 9:
                    print("-------------")
            i += 1
        print("\n\n")

    def no_more_space(self):
        space = 0
        for cell in self.board:
            if cell == '':
                space += 1

        if space:
            return False
        return True

    def check_win(self, symbol):
        appearance = []
        for i in range(len(self.board)):
            if self.board[i] == symbol:
                appearance.append(i)

        if len(appearance) >= 3:
            for combination in self.win_combinations:
                if set(combination).issubset(set(appearance)):
                    return True
