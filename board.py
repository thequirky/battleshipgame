from enum import Enum

from position import Position

SPACE = " "
GAP = 2 * SPACE


class Cell(Enum):
    HIT = "X"
    MISS = "O"
    EMPTY = "-"


class Board:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.grid = self.reset()

    def reset(self) -> list[Cell]:
        return [[Cell.EMPTY for _ in range(self.size)] for _ in range(self.size)]

    def get_value(self, pos: Position) -> Cell:
        return self.grid[pos.x][pos.y]

    def set_value(self, pos: Position, value: Cell) -> None:
        self.grid[pos.x][pos.y] = value

    def is_empty(self, guess: Position) -> bool:
        return self.get_value(guess) == Cell.EMPTY

    def __str__(self) -> str:
        separator = 2*SPACE if self.size > 10 else SPACE
        brd_str = SPACE + separator + separator.join(str(idx) for idx in range(self.size))
        for x in range(self.size):
            row = str(x) + separator
            for y in range(self.size):
                pos = Position(x, y)
                cell_value = self.get_value(pos)
                if cell_value == Cell.EMPTY or cell_value in [Cell.HIT, Cell.MISS]:
                    row += cell_value.value + separator
                else:
                    row += Cell.EMPTY.value + separator
            brd_str += "\n" + row
        return brd_str

    def _show_board(self) -> None:
        for row in self.grid:
            row_items = [
                cell[0].upper() if isinstance(cell, str) else cell.name[0] for cell in row
            ]
            print(" ".join(row_items))
        print('\n')


if __name__ == "__main__":
    brd = Board(size=10)
    pos = Position(x=3, y=3)
    brd.set_value(pos=pos, value=Cell.HIT)
    print(brd)
