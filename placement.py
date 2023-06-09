
import random
from board import Board, Cell
from position import Orientation, Position
from ship import Ship


def place_ship_on_position(
    ship: Ship,
    board: Board,
    pos: Position,
    orientation: Orientation
) -> None:
    if orientation == Orientation.HORIZONTAL:
        positions = [Position(pos.x, pos.y + i) for i in range(ship.size)]
    else:
        positions = [Position(pos.x + i, pos.y) for i in range(ship.size)]
    for pos in positions:
        board.set_value(pos, ship.type.value)
        ship.coords.append(pos)


def can_place_ship_on_position(
    ship: Ship,
    board: Board,
    pos: Position,
    orientation: Orientation
) -> bool:
    can_fit_vertically = pos.x + ship.size < board.size
    can_fit_horizontally = pos.y + ship.size < board.size
    if orientation == Orientation.VERTICAL and can_fit_vertically:
        positions = [Position(pos.x + i, pos.y) for i in range(ship.size)]
    elif orientation == Orientation.HORIZONTAL and can_fit_horizontally:
        positions = [Position(pos.x, pos.y + i) for i in range(ship.size)]
    else:
        return False
    has_no_obstacles = all(board.get_value(pos) == Cell.EMPTY for pos in positions)
    return has_no_obstacles


def place_ship_randomly(ship: Ship, board: Board) -> None:
    while True:
        pos = Position(
            x=random.randint(0, board.size - 1),
            y=random.randint(0, board.size - 1)
        )
        orientation = random.choice(list(Orientation))
        if can_place_ship_on_position(ship, board, pos, orientation):
            place_ship_on_position(ship, board, pos, orientation)
            break
