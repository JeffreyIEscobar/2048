import random

class Numbers2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = random.choice([2, 4])

    def move(self, direction):
        if direction == "left":
            self.move_left()
        elif direction == "right":
            self.move_right()
        elif direction == "up":
            self.move_up()
        elif direction == "down":
            self.move_down()

    def move_left(self):
        for row in self.board:
            # Merge tiles and shift to the left
            self.merge_and_shift(row)

    def move_right(self):
        for row in self.board:
            # Reverse, merge, and shift to the right
            row.reverse()
            self.merge_and_shift(row)
            row.reverse()

    def move_up(self):
        # Transpose the board, move left, and transpose back
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        # Transpose the board, move right, and transpose back
        self.transpose()
        self.move_right()
        self.transpose()

    def merge_and_shift(self, row):
        # Merge tiles and shift to the left within a row
        for i in range(3):
            for j in range(3, 0, -1):
                if row[j] == row[j - 1] and row[j] != 0:
                    row[j] *= 2
                    self.score += row[j]
                    row[j - 1] = 0
                elif row[j] == 0 and row[j - 1] != 0:
                    row[j] = row[j - 1]
                    row[j - 1] = 0

    def transpose(self):
        self.board = [list(row) for row in zip(*self.board)]

    def is_game_over(self):
        # Check if there are no more valid moves (horizontally or vertically)
        for i in range(4):
            for j in range(4):
                if (
                    (j < 3 and self.board[i][j] == self.board[i][j + 1]) or
                    (i < 3 and self.board[i][j] == self.board[i + 1][j])
                ):
                    return False
        return True

    def display_board(self):
        print("\nScore:", self.score)
        for row in self.board:
            print(" ".join(map(str, row)))

    def run(self):
        while True:
            self.display_board()
            move = input("Enter a move (left, right, up, down, or q to quit): ").lower()
            if move == 'q':
                break
            if move in ['left', 'right', 'up', 'down']:
                self.move(move)
                self.add_tile()
                if self.is_game_over():
                    print("Game over!")
                    break

if __name__ == "__main__":
    game = Numbers2048()
    game.run()
