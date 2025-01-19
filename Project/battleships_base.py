import random


# size of grid is 10x10
# number of ships possible to place is 6, each ship takes one spot, ships may be adjacent to form a larger ship.


class Ship:
    def __init__(self, x, y, length, orientation=None, sunk=False):
        self.x = x
        self.y = y
        self.length = length
        self.positions = [(x, y)]
        if self.length > 1:
            if orientation == 'h':
                for i in range(1, length):
                    self.positions.append((x, y + i))
            else:
                for j in range(1, length):
                    self.positions.append((x + j, y))
        self.hit_pos = []
        self.hit_count = len(self.hit_pos)
        self.sunk = sunk
        self.orientation = orientation
        self.value = '⏺'
        self.values = {}

        for pos in self.positions:
            self.values[pos] = self.value

        if self.hit_pos is not []:
            for i in range(self.hit_count):
                if self.hit_pos[i] in self.values:
                    self.values[self.hit_pos[i]] = 'A'

        if len(self.hit_pos) == self.length:
            self.sunk = True



class Grid:
    def __init__(self, count, size = 10):
        self.ships = []
        self.slot_count = count
        self.grid_hit = []
        self.size = size
        self.matrix = [['.' for _ in range(size)] for _ in range(size)]
        self.hidden_grid = self.matrix

    def remove_ship(self, ship):
        self.ships.remove(ship)

    def add_to_grid(self, ship):
        for pos in ship.positions:
            x, y = pos
            self.matrix[x][y] = ship

    def add_ship(self, ship):
        x = ship[0]
        y = ship[1]
        length = ship[2]
        orientation = ship[3]
        new_ship = Ship(x, y, length, orientation)
        self.ships.append(new_ship)
        self.add_to_grid(new_ship)


def get_x(grid_slot):
    return ord(list(grid_slot)[0].lower()) - ord('a')

def get_y(grid_slot):
    return int(list(grid_slot)[1])

def check_valid_grid_slot(grid_slot):
    input_grid = list(grid_slot)
    if len(input_grid) != 2:
        return False

    var = str(input_grid[0]).lower()
    num = str(input_grid[1])

    if var.isalpha() and num.isdigit():
        if ord("a") <= ord(var) <= ord("j") and 0 <= int(num) <= 9:
            return True
        else:
            return False
    else:
        return False

def check_if_empty(x, y, length, grid, orientation=None):
    if orientation == 'h':
        for i in range(length):
            if grid.matrix[x][y + i] != '.':
                return False
            else:
                continue
    elif orientation == 'v':
        for i in range(length):
            if grid.matrix[x + i][y] != '.':
                return False
            else:
                continue
    else:
        if grid.matrix[x][y] != '.':
            return False

    return True

def check_if_in_bounds(x, y, length, orientation=None):
    if orientation== 'h':
        if(y + length - 1) >= 10:
            return False
    elif orientation == 'v':
        if(x + length - 1) >= 10:
            return False
    else:
        if (x > 9 or x < 0) or (x > 9 or x < 0):
            return False
    return True

def check_if_hit(x, y, grid):
    if isinstance(grid.matrix[x][y], Ship):
        if (x, y) in grid.matrix[x][y].hit_pos:
            return True
        else:
            return False

    if grid.matrix[x][y] == '.':
        return False
    return True

def get_coordinates(length):
    if length == 3:
        print(f"Choose the coordinates and orientation of your only 3-grid box long ship(A0 - J9)")
    else:
        print(f"Choose the coordinates and orientation of your {length}-grid box long ship(A0 - J9)")
    correct_grid_slot = False
    while not correct_grid_slot:
        grid_slot = input("Starting Coordinates:")

        if len(grid_slot) != 2:
            print("Invalid grid slot, grid slot should be between A0 - J9")
        else:
            if check_valid_grid_slot(grid_slot):
                return grid_slot
            else:
                print("Invalid grid slot, grid slot should be between A0 - J9")

def get_orientation():
    correct_input = False
    while not correct_input:
        print("Orientation - 'H' for horizontal and 'V' for vertical.")
        orientation = input().strip().lower()

        if orientation != 'h' and orientation != 'v':
            print("Invalid input, please type either 'H' or 'V'.")
        elif orientation.lower() == 'h' or orientation.lower() == 'v':
            return orientation

def get_ship(length, grid):
    grid_slot = get_coordinates(length)
    x = get_x(grid_slot)
    y = get_y(grid_slot)
    if check_valid_grid_slot(grid_slot):
        if length > 1:
            orientation = get_orientation()
        else:
            orientation = None

        if not check_if_in_bounds(x, y, length, orientation):
            print("Ship is out of bounds, choose another grid slot")
            return get_ship(length, grid)

        if check_if_empty(x, y, length, grid, orientation) is True:
            ship = (x, y, length, orientation)
        else:
            print("The position is already filled, choose another")
            return get_ship(length, grid)

        grid.add_ship(ship)

def set_player_grid(grid):
    get_ship(4, grid)
    for _ in range(2):
        get_ship(3, grid)
    # for _ in range(3):
    #     get_ship(2, grid)

def generate_ai_coordinates():
    return random.randint(0, 9), random.randint(0, 9)

def generate_ai_orientation():
    return random.choice(['h', 'v'])

def get_ai_ship(grid, length):
    x, y = generate_ai_coordinates()
    if length != 1:
        ai_orientation = generate_ai_orientation()
        create_ships_for_ai(x, y, length, grid,  ai_orientation)
    else:
        create_ships_for_ai(x, y, length, grid)

def create_ships_for_ai( x, y, length, grid, orientation=None):
    if check_if_in_bounds(x, y, length, orientation) is False or check_if_empty(x, y, length, grid, orientation) is False:
        get_ai_ship(grid, length)
    else:
        if length == 1:
            ship = (x, y, length, None)
        else:
            ship = (x, y, length, orientation)
        grid.add_ship(ship)

def set_ai_grid(grid):
    get_ai_ship(grid, 4)
    for _ in range(2):
        get_ai_ship(grid, 3)
    for _ in range(3):
        get_ai_ship(grid, 2)

def display_live_grids(player_grid, ai_grid):
    # to display the grid while hiding the ships
    space = ' '
    print(space * 7, "YOUR GRID", space * 31 , "AI GRID")
    for i in range(10):
        first = True
        for j in range(10):
            if isinstance(player_grid.matrix[i][j], Ship):
                if (i, j) in player_grid.matrix[i][j].values:
                    print(player_grid.matrix[i][j].values[(i,j)], " ", sep=" ", end="")
            else:
                print(player_grid.matrix[i][j], " ", sep=" ", end="")

        for j in range(10):
            if first:
                if ai_grid.matrix[i][j] == 'X' or ai_grid.matrix[i][j] == '.':
                    print(space * 10, ai_grid.matrix[i][j], " ", sep=" ", end="")

                else:
                    if ai_grid.matrix[i][j].hit_pos != 0 and (i,j) in ai_grid.grid_hit:
                        print(space * 10, ai_grid.matrix[i][j].value, " ", sep=" ", end="")
                    else:
                        print(space * 10, ".", " ", sep=" ", end="")
                first = False
            else:
                if ai_grid.matrix[i][j] == 'X' or ai_grid.matrix[i][j] == '.':
                    print( ai_grid.matrix[i][j], " ", sep=" ", end="")
                else:
                    if len(ai_grid.matrix[i][j].hit_pos) != 0 and (i,j) in ai_grid.grid_hit:
                        print(ai_grid.matrix[i][j].value, " ", sep=" ", end="")
                    else:
                        print(".", " ", sep=" ", end="")

        print()
    print(f"Ships hit by you = {len(ai_grid.grid_hit)}",  space * 18, f"Ships hit by ai = {len(player_grid.grid_hit)}")

def players_move(player_grid, ai_grid):
    strike = input("Choose where to fire your missile(A0 - J9):")
    while True:
        if check_valid_grid_slot(strike):
            break
        else:
            print("Invalid grid slot, try again")
            strike = input("Choose where to fire your missile(A0 - J9):")

    x, y = get_x(strike), get_y(strike)

    if ai_grid.matrix[x][y] == ".":
        ai_grid.matrix[x][y] = "X"
        print("You missed!")
        ai_grid.grid_hit.append((x,y))
    elif check_if_hit(x, y, ai_grid):
        print("You already shot here, choose another grid slot.")
        return players_move(player_grid, ai_grid)
    else:
        ai_grid.matrix[x][y].hit_count += 1
        ai_grid.matrix[x][y].hit_pos.append((x,y))
        if ai_grid.matrix[x][y].hit_count == ai_grid.matrix[x][y].length:
            print("YOU SUNK A SHIP!!")
            ai_grid.matrix[x][y].sunk = True
        else:
            print("YOU HIT A SHIP!")
        ai_grid.grid_hit.append((x,y))
        ai_grid.slot_count -= 1

def ai_check(x, y, player_grid):
    if player_grid.matrix[x][y] == ".":
        player_grid.matrix[x][y] = "X"
        return False, x, y
    else:
        if (x,y) in player_grid.matrix[x][y].values:
            player_grid.matrix[x][y].values[(x,y)] = 'A'
        return True, x, y

def get_ai_strike_coordinates(ai_shots):
    while True:
        x, y = generate_ai_coordinates()
        if (x, y) not in ai_shots:
            return x, y

def ai_move(player_grid, ai_shots: list, ai_last_ship_hit: dict):
    orientation = None
    hit_multi_grid_ship = False
    x, y = get_ai_strike_coordinates(ai_shots)

    if ai_last_ship_hit:
        prev_x, prev_y = ai_last_ship_hit[0]
        print(player_grid)
        # check if the coordinates have already been struck or the previous strike zone sunk a ship
        if isinstance(player_grid.matrix[prev_x][prev_y], Ship):
            if player_grid.matrix[prev_x][prev_y].sunk is False:
                x, y = prev_x, prev_y
                hit_multi_grid_ship = True
            else:
                ai_last_ship_hit = {}

        if player_grid.matrix[x][y].value == '⏺' and hit_multi_grid_ship:
            if check_if_in_bounds(x, y + 1, 1) and not check_if_hit(x, y + 1, player_grid):
                y = y + 1
                orientation = 'v'
            elif check_if_in_bounds(x, y - 1, 1) and not check_if_hit(x, y - 1, player_grid):
                y = y - 1
                orientation = 'v'
            elif check_if_in_bounds(x + 1, y, 1) and not check_if_hit(x + 1, y, player_grid):
                x = x + 1
                orientation = 'h'
            else:
                x = x - 1
                orientation = 'h'

            move_hit = ai_check(x, y, player_grid)

    else:
        move_hit = False, x, y

    if move_hit[0]:
        ai_last_ship_hit[(move_hit[1], move_hit[2])] = orientation
        print(f"AI hit a ship at {(chr(move_hit[1] + ord('a'))).upper()}{move_hit[2]}")
        player_grid.grid_hit.append((x, y))
    else:
        ai_shots.append((move_hit[1], move_hit[2]))

    print(move_hit)


def start_game(slots = 13):
    # game with 8 ships, includes one 3 block long ship, three 2 block long ships and four 1 block long ships = 3 + 6 + 4 = 13 grid_slots
    player_grid = Grid(slots)
    set_player_grid(player_grid)
    ai_grid = Grid(slots)
    set_ai_grid(ai_grid)
    turn = 0
    ai_shots = []
    ai_shots_hit = []
    display_live_grids(player_grid, ai_grid)
    while ai_grid.slot_count != 0:
        players_move(player_grid, ai_grid)
        turn += 1
        ai_move(player_grid, ai_shots, ai_shots_hit)
        display_live_grids(player_grid, ai_grid)

    print("Game Over")


start_game()
