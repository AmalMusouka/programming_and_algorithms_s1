import pygame, math


class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size


    def create_grid(self, pos):
        """Creates a game grid with coordinates for each cell"""
        start_x = pos[0]
        start_y = pos[1]
        coordinate_grid = []
        for row in range(self.rows):
            row_x = []
            for col in range(self.cols):
                row_x.append((start_x, start_y))
                start_x += self.cell_size
            coordinate_grid.append(row_x)
            start_x = pos[0]
            start_y += self.cell_size
        return coordinate_grid

    def update_game_logic(self):
        """Updates the game grid with logic, ie, spaces and X for ships"""
        game_logic = []
        for row in range(self.rows):
            row_x = []
            for col in range(self.cols):
                row_x.append(" ")
            game_logic.append(row_x)
        return game_logic

    def show_grid(self, window, player_grid, AI_grid):
        """Draws the player and computer grid on the screen"""
        grids = [player_grid, AI_grid]
        for grid in grids:
            for row in grid:
                for col in row:
                    pygame.draw.rect(window,(255, 255, 255), (col[0], col[1], self.cell_size, + self.cell_size), 1)

    def print_game_logic(self):
        """prints to the terminal the game logic"""
        print('Player Grid'.center(50, '#'))
        for _ in player_game_logic:
            print(_)
        print('AI grid'.center(50, '#'))
        for _ in AI_game_logic:
            print(_)

    def update_screen(self, window, player_grid, AI_grid):
        window.fill((100, 0, 0))
        self.show_grid(window, player_grid, AI_grid)
        pygame.display.update()

    def get_input(self, pos, player_grid, ai_grid):
        """gets the mouse click and connects it to the coordinate grid"""
        x_click = math.floor(pos[0] / 50) - 1
        y_click = math.floor(pos[0] / 50) - 1
        return x_click, y_click
        # if 0 <= x_click <= 9 and 0 <= y_click <= 9:
        #    return player_grid[x_click][y_click]
        # if 14 <= x_click <= 23 and 14 <= y_click <= 23:
        #     return ai_grid[x_click - 14][y_click - 14]

    def change_state(self, window, coordinates):
        """change the state of the tile from unknown to ship or vice versa"""
        if coordinates[0] <= 10:
            if player_game_logic[coordinates[0]][coordinates[1]] == '#':
                print("Already shot")
            else:
                player_game_logic[coordinates[0]][coordinates[1]] = '#'


# Game variables
SCREENWIDTH = 1260
SCREENHEIGHT = 960
ROWS = 10
COLS = 10
CELL_SIZE = 50



grid = Grid(ROWS, COLS, CELL_SIZE)
#loading game variables
player_game_grid = grid.create_grid((50, 50))
player_game_logic = grid.update_game_logic()

AI_game_grid = grid.create_grid((SCREENWIDTH - 50 - (ROWS * CELL_SIZE),50))
AI_game_logic = grid.update_game_logic()

grid.print_game_logic()


SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("BATTLESHIPS")




run = True

# main game loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            grid.change_state(SCREEN, grid.get_input(pos, player_game_grid, AI_game_grid))
            grid.print_game_logic()


    grid.update_screen(SCREEN, player_game_grid, AI_game_grid)


pygame.quit()
