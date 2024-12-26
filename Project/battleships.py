import pygame

# game utility
def create_grid(rows, cols, cell_size, pos):
    """Creates a game grid with coordinates for each cell"""
    start_x = pos[0]
    start_y = pos[1]
    coordinate_grid = []
    for row in range(rows):
        row_x = []
        for col in range(cols):
            row_x.append((start_x, start_y))
            start_x += cell_size
        coordinate_grid.append(row_x)
        start_x = pos[0]
        start_y += cell_size
    return coordinate_grid

def update_game_logic(rows, cols):
    """Updates the game grid with logic, ie, spaces and X for ships"""
    game_logic = []
    for row in range(rows):
        row_x = []
        for col in range(cols):
            row_x.append(" ")
        game_logic.append(row_x)
    return game_logic

def show_grid(window, cell_size, player_grid, ai_grid):
    """Draws the player and computer grid on the screen"""
    game_grids = [player_grid, ai_grid]
    for grid in game_grids:
        for row in grid:
            for col in row:
                pygame.draw.rect(window,(255, 255, 255), (col[0], col[1], cell_size, + cell_size), 1)


def print_game_logic():
    """prints to the terminal the game logic"""
    print('Player Grid'.center(50, '#'))
    for _ in player_game_logic:
        print(_)
    print('AI grid'.center(50, '#'))
    for _ in AI_game_logic:
        print(_)

def update_screen(window):
    window.fill((0, 0, 0))
    show_grid(window, CELL_SIZE, player_game_grid, AI_game_grid)
    pygame.display.update()

# Game variables
SCREENWIDTH = 1260
SCREENHEIGHT = 960
ROWS = 10
COLS = 10
CELL_SIZE = 50

#loading game variables
player_game_grid = create_grid(ROWS, COLS, CELL_SIZE, (50, 50))
player_game_logic = update_game_logic(ROWS, COLS)

AI_game_grid = create_grid(ROWS, COLS, CELL_SIZE, (SCREENWIDTH - (ROWS * CELL_SIZE),50))
AI_game_logic = update_game_logic(ROWS, COLS)

print_game_logic()


SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("BATTLESHIPS")

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    update_screen(SCREEN)

pygame.quit()
