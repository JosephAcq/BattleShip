class Board:
    def __init__(self, size=5):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def display(self, reveal=False):
        print("\n  " + " ".join([chr(i + 65) for i in range(self.size)]))  # A B C D E...
        for index, row in enumerate(self.grid):
            row_display = []
            for cell in row:
                if cell == 0:
                    row_display.append(".")
                elif cell == 1:
                    row_display.append("B" if reveal else ".")
                elif cell == 2:
                    row_display.append("X")  # Hit
                elif cell == 3:
                    row_display.append("O")  # Miss
            print(f"{index + 1} {' '.join(row_display)}")

    def place_ship(self, row, col, length=3, direction="H"):
        for i in range(length):
            r = row + i if direction == "V" else row
            c = col + i if direction == "H" else col
            if r >= self.size or c >= self.size:
                raise ValueError("Ship out of bounds.")
            if self.grid[r][c] != 0:
                raise ValueError("Ship overlaps with another.")
            self.grid[r][c] = 1

    def receive_attack(self, row, col):
        if self.grid[row][col] == 1:
            self.grid[row][col] = 2  # Hit
            return "hit"
        elif self.grid[row][col] == 0:
            self.grid[row][col] = 3  # Miss
            return "miss"
        else:
            return "already tried"
