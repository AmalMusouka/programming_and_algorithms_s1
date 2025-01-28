import random

class Ship:
    """The main Ship class that stores the (x, y) co-ordinates, length, position and orientation of the Ship as well as all its (x, y) coordinates that aren't the current co-ordinates.
    Also stores whether the ship is afloat or has sunk, and where all it has been shot."""
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
    """The main grid class used to store all the ships that are placed in it, the number of slots it takes, size, and all the co-ordinates that have been hit by a missile while the game is playing.
    Also converts the co-ordinates into an actual grid which is visible to the user."""
    def __init__(self, count, size = 10):
        self.ships = []
        self.slot_count = count
        self.grid_hit = []
        self.size = size
        self.matrix = [['.' for _ in range(size)] for _ in range(size)]

    def remove_ship(self, ship):
        """Removes a ship from the class."""
        self.ships.remove(ship)

    def add_to_grid(self, ship):
        """Adds all the ships to the matrix grid."""
        for pos in ship.positions:
            x, y = pos
            self.matrix[x][y] = ship

    def add_ship(self, ship):
        """Adds a ship to the class."""
        x = ship[0]
        y = ship[1]
        length = ship[2]
        orientation = ship[3]
        new_ship = Ship(x, y, length, orientation)
        self.ships.append(new_ship)
        self.add_to_grid(new_ship)


def get_x(grid_slot):
    """Returns the x co-ordinate in integer form from user input which is a letter."""
    return ord(list(grid_slot)[0].lower()) - ord('a')

def get_y(grid_slot):
    """Returns the y co-ordinate in integer form from user input which is a digit."""
    return int(list(grid_slot)[1])

def check_valid_grid_slot(grid_slot):
    """To check if the x and y co-ordinates that the user inputs is valid. That is, the x-coordinate is a character between and including A-J and y-coordinate is a number between and including 0-9."""
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
    """To check if the (x, y) co-ordinates does not contain a ship."""
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
    """To check if the x and y co-ordinates of the ship are within the bounds of the matrix grid which is 10 x 10."""
    if orientation== 'h':
        if(y + length - 1) >= 10:
            return False
    elif orientation == 'v':
        if(x + length - 1) >= 10:
            return False
    else:
        if (x > 9 or x < 0) or (y > 9 or y < 0):
            return False
    return True

def check_if_ship(x, y, grid):
    """Checks if the chosen (x, y) co-ordinates already has a ship."""
    if isinstance(grid.matrix[x][y], Ship):
        return True
    return False

def check_if_hit(x, y, grid):
    """Checks if the chosen (x, y) co-ordinates has already been hit by a missile."""
    if isinstance(grid.matrix[x][y], Ship):
        if (x, y) in grid.matrix[x][y].hit_pos:
            return True

    if grid.matrix[x][y] == 'X':
        return True
    return False

def get_coordinates(length):
    """Takes the user input to get the (x, y) coordinates."""
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
    """Takes the user input to get the orientation of the ship."""
    correct_input = False
    while not correct_input:
        print("Orientation - 'H' for horizontal and 'V' for vertical.")
        orientation = input().strip().lower()

        if orientation != 'h' and orientation != 'v':
            print("Invalid input, please type either 'H' or 'V'.")
        elif orientation.lower() == 'h' or orientation.lower() == 'v':
            return orientation

def get_ship(length, grid):
    """Used to create a ship from the user inputs if it is valid and in bounds."""
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
    """Displays the player grid and takes in user input while constantly updating the grid as the ships are formed at their respective coordinates."""
    display_player_grid(grid)
    get_ship(4, grid)
    for _ in range(2):
        display_player_grid(grid)
        get_ship(3, grid)
    for _ in range(4):
        display_player_grid(grid)
        get_ship(2, grid)

def generate_ai_coordinates():
    """Used to generate (x, y) coordinates of the ship for the AI."""
    return random.randint(0, 9), random.randint(0, 9)

def generate_ai_orientation():
    """Used to generate the orientation of the ship for the AI."""
    return random.choice(['h', 'v'])

def create_ships_for_ai( x, y, length, grid, orientation=None):
    """Creates the ships for the AI's grid."""
    if check_if_in_bounds(x, y, length, orientation) is False or check_if_empty(x, y, length, grid, orientation) is False:
        get_ai_ship(grid, length)
    else:
        if length == 1:
            ship = (x, y, length, None)
        else:
            ship = (x, y, length, orientation)
        grid.add_ship(ship)

def get_ai_ship(grid, length):
    """Takes the (x, y) coordinates and uses it to call the function that creates the ship, with the orientation or without depending on the length of the ship."""
    x, y = generate_ai_coordinates()
    if length != 1:
        ai_orientation = generate_ai_orientation()
        create_ships_for_ai(x, y, length, grid,  ai_orientation)
    else:
        create_ships_for_ai(x, y, length, grid)

def set_ai_grid(grid):
    """Creates the grid for the AI."""
    get_ai_ship(grid, 4)
    for _ in range(2):
        get_ai_ship(grid, 3)
    for _ in range(4):
        get_ai_ship(grid, 2)

def display_player_grid(player_grid):
    """Displays the players grid with numbering and lettering and spacing between the ships and/or empty spaces."""
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    number = '0  1  2  3  4  5  6  7  8  9'
    space = ' '
    print(space * 10, "YOUR GRID")
    print(space, number)
    for i in range(10):
        print(letters[i], end=' ')
        for j in range(10):
            if isinstance(player_grid.matrix[i][j], Ship):
                if (i, j) in player_grid.matrix[i][j].values:
                    print(player_grid.matrix[i][j].values[(i, j)], " ", sep=" ", end="")
            else:
                print(player_grid.matrix[i][j], " ", sep=" ", end="")

        print(letters[i], end=' ')
        print()
    print(space, number)

def display_live_grids(player_grid, ai_grid):
    """Displays both the players grid and the AI's grid with numbering and lettering as well as spacing between the ships and/or empty spaces and is constantly updated after each round. Also shows how many ship slots have been hit by the user and the AI.
    Key point: The AI grid is shown without the ships, which are only displayed after they have been hit and the empty slots are shown as misses if hit."""
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    number = '0  1  2  3  4  5  6  7  8  9'
    space = ' '
    print(space * 10, "YOUR GRID", space * 36 , "AI GRID")
    print(space, number, space * 15, number)
    for i in range(10):
        print(letters[i], end=' ')
        first = True
        for j in range(10):
            if isinstance(player_grid.matrix[i][j], Ship):
                if (i, j) in player_grid.matrix[i][j].values:
                    print(player_grid.matrix[i][j].values[(i,j)], " ", sep=" ", end="")
            else:
                print(player_grid.matrix[i][j], " ", sep=" ", end="")

        for j in range(10):
            if first:
                print(letters[i], end=' ')
                if ai_grid.matrix[i][j] == 'X' or ai_grid.matrix[i][j] == '.':
                    print(space * 10, letters[i], ai_grid.matrix[i][j], " ", sep=" ", end="")

                else:
                    if ai_grid.matrix[i][j].hit_pos != 0 and check_if_hit(i, j, ai_grid):
                        print(space * 10, letters[i], ai_grid.matrix[i][j].value, " ", sep=" ", end="")
                    else:
                        print(space * 10, letters[i], ".", " ", sep=" ", end="")
                first = False
            else:
                if ai_grid.matrix[i][j] == 'X' or ai_grid.matrix[i][j] == '.':
                    print(ai_grid.matrix[i][j], " ", sep=" ", end="")
                else:
                    if len(ai_grid.matrix[i][j].hit_pos) != 0 and check_if_hit(i, j, ai_grid):
                        print(ai_grid.matrix[i][j].value, " ", sep=" ", end="")
                    else:
                        print(".", " ", sep=" ", end="")
        print(letters[i], end='')

        print()
    print(space, number, space * 15, number)
    print(f"Ship slots hit by you = {len(ai_grid.grid_hit)}",  space * 20, f"Ship slots hit by ai = {len(player_grid.grid_hit)}")

def players_move(player_grid, ai_grid):
    """Takes the user input for firing the missile. If the slot is invalid or the slot is out of bounds, it tries again until a valid input is provided.
    Also gives feedback on whether the player hit a ship, sank a ship or missed."""
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
        print("YOU MISSED!")
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
        ai_grid.slot_count -= 1
        ai_grid.grid_hit.append((x, y))

def ai_check(x, y, player_grid):
    """Used to check if the (x, y) coordinates of the AI's missile struck a ship or missed."""
    if player_grid.matrix[x][y] == ".":
        player_grid.matrix[x][y] = "X"
        return False, x, y
    else:
        if (x,y) in player_grid.matrix[x][y].values:
            player_grid.matrix[x][y].values[(x,y)] = 'A'
            res = True

            for value in player_grid.matrix[x][y].values:
                if player_grid.matrix[x][y].values[value] != 'A':
                    res = False
                    break

            if res:
                for value_x, value_y in player_grid.matrix[x][y].values:
                    player_grid.matrix[value_x][value_y].sunk = True

        return True, x, y

def get_ai_strike_coordinates(ai_shots):
    """Used to get the (x, y) coordinates for the AI's strike."""
    while True:
        x, y = generate_ai_coordinates()
        if (x, y) not in ai_shots:
            return x, y

def ai_move(player_grid, ai_shots: list, ai_last_ship_hit: list):
    """Used to dictate the next move of the AI. Takes in a list of all the co-ordinates shot by the AI and the last ship that it hit if there exists one.
    The AI checks the neighbouring positions if a ship was hit before and if it didn't sink. If the AI hit a ship, it proceeds to give feedback that the AI indeed did so."""
    orientation = None
    hit_multi_grid_ship = False
    x, y = get_ai_strike_coordinates(ai_shots)
    direction = None

    if ai_last_ship_hit:
        prev_x, prev_y = ai_last_ship_hit[0], ai_last_ship_hit[1]
        orientation = ai_last_ship_hit[2]
        # check if the coordinates have already been struck or the previous strike zone sunk a ship
        if isinstance(player_grid.matrix[prev_x][prev_y], Ship):
            if player_grid.matrix[prev_x][prev_y].sunk is False:
                x, y = prev_x, prev_y
                hit_multi_grid_ship = True
            else:
                ai_last_ship_hit.clear()

        if hit_multi_grid_ship and player_grid.matrix[x][y].value == '⏺':

            for i in range(1,4):
                if check_if_in_bounds(x, y + i, 1) and orientation != 'v' and direction not in ['L', 'U', 'D']:
                    if not check_if_hit(x, y + i, player_grid):
                        y = y + i
                        orientation = 'h'
                        direction = 'R'
                        break
                    else:
                        if check_if_ship(x, y + i, player_grid):
                            orientation = 'h'
                            direction = 'R'
                        else:
                            direction = None
                            break

            if direction == 'L' or direction is None:
                for i in range(1, 4):
                    if check_if_in_bounds(x, y - i, 1) and orientation != 'v' and direction not in ['R', 'U', 'D']:
                        if not check_if_hit(x, y - i, player_grid):
                            y = y - i
                            orientation = 'h'
                            direction = 'L'
                            break
                        else:
                            if check_if_ship(x, y - i, player_grid):
                                orientation = 'h'
                                direction = 'L'
                            else:
                                direction = None
                                break

            if direction is None:
                for i in range(1, 4):
                    if check_if_in_bounds(x - i, y, 1) and orientation != 'h' and direction not in ['L', 'R', 'D']:
                        if not check_if_hit(x - i, y, player_grid):
                            x = x - i
                            orientation = 'v'
                            direction = 'U'
                            break
                        else:
                            if check_if_ship(x - i, y, player_grid):
                                orientation = 'v'
                                direction = 'U'
                            else:
                                direction = 'D'
                                break

            if direction == 'D' or direction is None:
                for i in range(1, 4):
                    if check_if_in_bounds(x + i, y, 1) and orientation != 'h' and direction not in ['L', 'R', 'U']:
                        if not check_if_hit(x + i, y, player_grid):
                            x = x + i
                            orientation = 'v'
                            break
                        else:
                            if check_if_ship(x + i, y, player_grid):
                                orientation = 'v'
        else:
            x, y = get_ai_strike_coordinates(ai_shots)
    move_hit = ai_check(x, y, player_grid)

    if move_hit[0]:
        if isinstance(player_grid.matrix[x][y], Ship):
            if not player_grid.matrix[x][y].sunk:
                ai_last_ship_hit.extend([move_hit[1], move_hit[2], orientation])
        print(f"AI HIT A SHIP AT {(chr(move_hit[1] + ord('a'))).upper()}{move_hit[2]}")
        player_grid.matrix[x][y].hit_pos.append((x, y))
        player_grid.grid_hit.append((x, y))

    ai_shots.append((move_hit[1], move_hit[2]))


def start_game(slots = 18):
    """The function that starts the game. Displays the grids, takes the user input for both ships and for firing missiles, as well as for the AI. After the game ends, when either the AI or the User gets all the ships, the game ends and provides the results."""
    # game with 8 ships, includes one 4 block long ship, two 3 block long ships and four 2 block long ships = 4 + 6 + 8 = 18 grid_slots
    player_grid = Grid(slots)
    set_player_grid(player_grid)
    ai_grid = Grid(slots)
    set_ai_grid(ai_grid)
    turn = 0
    ai_shots = []
    ai_last_ship_hit = []
    display_live_grids(player_grid, ai_grid)
    while ai_grid.slot_count != 0:
        players_move(player_grid, ai_grid)
        turn += 1
        ai_move(player_grid, ai_shots, ai_last_ship_hit)
        display_live_grids(player_grid, ai_grid)
        if len(player_grid.grid_hit) == 18:
            print("GAME OVER! AI WINS!!")
            break
        elif len(ai_grid.grid_hit) == 18:
            print("GAME OVER! YOU WIN!!.")
            break

start_game()
