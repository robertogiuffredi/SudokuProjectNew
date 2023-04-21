import pygame
from SudokuGenerator import *
pygame.init()
# define WIDTH, HEIGHT and create display screen with dimensions and 'sudoku' title
WIDTH, HEIGHT = 900, 600
original_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
# displayed variables for sudoku (background, cursor, etc...)
starting_cursor = pygame.image.load("assets/cursor.png")
game_board = pygame.image.load("assets/grid.png")
home_background = pygame.image.load("assets/background.jpg")
# values of colors
red = (255, 0, 0)
green = (65, 255, 17)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (75, 75, 75)
# default values (cell, screen, click, keypad keypad direction, etc...)
cell_size = 48
empty_cells = 0
clickable = False
cell_number = 0
enter = False
user_number = ""
screen = "home"
keypad = ""

# start at y = 34 x = 234
fps = 300
# Font class with size and default type of font
class Font():
    def __init__(self, size = 14):
        self.font = pygame.font.Font("assets/calibri.ttf", size)

    def get_font(self):
        return self.font

    def update_font_size(self, size):
        self.font = pygame.font.Font("assets/calibri.ttf", size)
# define text variables (with different font sizes)
smallest_text = Font(10)
small_text = Font(14)
med_text = Font(25)
large_text = Font(32)
largest_text = Font(40)
title_text = Font(50)

# Button class
class Button():
    def __init__(self, x, y, w, h, font = small_text, text = "", clickable = True, border = 2, color1 = red, color2 = green, color3 = blue, centered = True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
        self.text = text
        self.clickable = clickable
        self.border = border
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.centered = centered
# draw buttons in correct location on original_surface
    def draw_button(self):
        pygame.draw.rect(original_surface, self.color3, pygame.Rect(self.x, self.y, self.w, self.h))
        pygame.draw.rect(original_surface, self.color2, pygame.Rect(self.x + self.border, self.y + self.border, self.w - self.border*2, self.h - self.border*2))
        display_text(self.text, self.x + self.w/2, self.y + self.h/2, self.font, self.color1, None, self.centered)
# is the cursor over a specific position? ----> True or False
    def hovering(self, x, y):
        if x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h and self.clickable:
            return True
        return False
# setters and getters
    def get_centered(self):
        return self.centered

    def get_clickable(self):
        return self.clickable

    def set_text(self, text, centered = True):
        self.text = text
        self.centered = centered

    def get_text(self):
        return self.text
# more getters and setters (self-explanatory)
    def set_color1(self, color):
        self.color1 = color

    def get_color1(self):
        return self.color1

    def set_color3(self, color):
        self.color3 = color

    def get_color3(self):
        return self.color3
# starts default button and creates Button class instance
current_button = Button(0, 0, 0, 0)

# locations of buttons
easy_button = Button(WIDTH / 2 - 120, HEIGHT / 2 - 20, 240, 60, large_text, "Easy")
medium_button = Button(WIDTH / 2 - 120, HEIGHT / 2 + 60, 240, 60, large_text, "Medium")
hard_button = Button(WIDTH / 2 - 120, HEIGHT / 2 + 140, 240, 60, large_text, "Hard")
exit_button = Button(WIDTH / 2 - 180, HEIGHT / 2, 360, 90, largest_text, "Exit")
restart_button = Button(WIDTH / 2 - 180, HEIGHT / 2, 360, 90, largest_text, "Restart")
reset_game_button = Button(WIDTH / 2 - 360, HEIGHT / 2 + 210, 120, 40, med_text, "Reset", True, 2, red, green, blue)
restart_game_button = Button(WIDTH / 2 - 50, HEIGHT / 2 + 210, 120, 40, med_text, "Restart", True, 2, red, green, blue)
exit_game_button = Button(WIDTH / 2 + 260, HEIGHT / 2 + 210, 120, 40, med_text, "Exit", True, 2, red, green, blue)
### change

# text displayed and centered about (x, y)
def display_text(text, x, y, font = small_text, color = black, background = None, centered = True):
    if centered:
        text = font.get_font().render(text, True, color, background)
        textCenter = text.get_rect(center=(x, y))
        original_surface.blit(text, textCenter)
    else:
        text = small_text.get_font().render(text, True, color, background)
        textCenter = text.get_rect(center = (x-cell_size/2 + 8, y+cell_size/2 - 8))
        original_surface.blit(text, textCenter)
# blits the cursor on the surface at point (x, y)
def update_cursor(x,y, cursor = starting_cursor):
    original_surface.blit(cursor, (x, y))
# Board class
class Board:
    def __init__(self, empty_cells):
        self.board = generate_sudoku(9, empty_cells)

    def create_buttons(self):
        x = 234
        y = 34
        self.grid_list = []
        i = 0
        j = 0
        while i < 9:
            while j < 9:
                clickable = False
                if self.board[i][j] == 0:
                    self.board[i][j] = ""
                    clickable = True
                new_button = Button(x, y, cell_size, cell_size, med_text, str(self.board[i][j]), clickable, 1, black, white, black, True)
                self.grid_list.append(new_button)
                x += cell_size
                j += 1
            x = 234
            y += cell_size
            j = 0
            i += 1
# updates the buttons (location on surface screen)
    def update_buttons(self, current = -1):
        i = 0
        while i < 81:
            self.grid_list[i].draw_button()
            i += 1
        pygame.draw.rect(original_surface, black, pygame.Rect(377, 35, 4, 434))
        pygame.draw.rect(original_surface, black, pygame.Rect(521, 35, 4, 434))
        pygame.draw.rect(original_surface, black, pygame.Rect(234, 176, 434, 4))
        pygame.draw.rect(original_surface, black, pygame.Rect(234, 321, 434, 4))
        if current != -1:
            self.grid_list[current].draw_button()
    def clear_board(self):
        i = 0
        while i < 81:
            if self.grid_list[i].get_color1() != black:
                self.grid_list[i].set_text("")
                y = i % 9
                x = i // 9
                self.board[x][y] = ""
            i += 1

# getters and setters
    def get_grid_list_button(self, i):
        return self.grid_list[i]

    def set_grid_list_button(self, i, button):
        self.grid_list[i] = button

    def submit_button(self, i, value):
        y = i % 9
        x = i // 9
        self.board[x][y] = int(value)
        empty = False
        h = 0
        j = 0
        while h < 9:
            while j < 9:
                if self.board[h][j] == "":
                    empty = True
                j += 1
            h += 1
            j = 0
        if not empty:
            return self.check_if_valid()
        else:
            return "game"



    def check_if_valid(self):
        global screen
        i = 0
        j = 0
        while i < 9:
            while j < 9:
                current_val = self.board[i][j]
                if not (self.check_row(i, current_val) and self.check_col(j, current_val) and self.check_box(i, j, current_val)):
                    return "game_lose"
                j += 1
            i += 1
            j = 0
        return "game_original_surface"


    def check_row(self, row, value):
        i = 0
        runs = 0
        while i < 9:
            if self.board[row][i] == value:
                runs += 1
                if runs >= 2:
                    return False
            i+= 1
        return True

    def check_col(self, col, value):
        i = 0
        runs = 0
        while i < 9:
            if self.board[i][col] == value:
                runs += 1
                if runs >= 2:
                    return False
            i += 1
        return True

    def check_box(self, row, col, value):
        runs = 0
        if row // 3 == 0:
            row_start = 0

        if row // 3 == 1:
            row_start = 3

        if row // 3 == 2:
            row_start = 6

        if col // 3 == 0:
            col_start = 0

        if col // 3 == 1:
            col_start = 3

        if col // 3 == 2:
            col_start = 6

        i = row_start
        j = col_start
        while i < row_start + 3:
            while j < col_start + 3:
                if self.board[i][j] == value:
                    runs += 1
                if runs >= 2:
                    print("Check box")
                    return False
                j += 1
            j = col_start
            i += 1
        return True
# this is the screen drawer, will create screen and goes into main function logic
def draw_screen(screen):
    global empty_cells
    global board
    global num_input
    global clickable
    global current_button
    global cell_number
    global enter
    global user_number
    global keypad
    # unpacks tuple for coordinates on screen
    x, y = pygame.mouse.get_pos()
    # home screen logic
    if screen == "home":
        original_surface.fill(white)
        original_surface.blit(home_background, (0, -30))
        # draws easy, med, hard buttons and displays welcome text...
        easy_button.draw_button()
        medium_button.draw_button()
        hard_button.draw_button()
        display_text("Welcome to Sudoku", WIDTH/2, 80, title_text, red, green)
        display_text("Select Game Mode:", WIDTH/2, 180, large_text, red, green)
# logic for the corresponding number of empty cells (easy=30, med=40, etc...) and updates screen accordingly
        if easy_button.hovering(x + 5, y) or medium_button.hovering(x + 5, y) or hard_button.hovering(x + 5, y):
            if mouse_click:
                if easy_button.hovering(x + 5, y):
                    empty_cells = 30
                elif medium_button.hovering(x + 5, y):
                    empty_cells = 40
                else:
                    empty_cells = 50
                board = Board(empty_cells)
                board.create_buttons()
                screen = "game"
        else:
            update_cursor(x, y)
# game screen logic, display sudoku game board on screen, and buttons too
    if screen == "game":
        original_surface.fill(blue)
        original_surface.blit(game_board, (225, 25))
        reset_game_button.draw_button()
        restart_game_button.draw_button()
        exit_game_button.draw_button()
        board.update_buttons()
        # the following checks if mouse clicks buttons/cells and answers accordingly
        if restart_game_button.hovering(x, y):
            if mouse_click:
                screen = "home"
        elif reset_game_button.hovering(x, y):
            if mouse_click:
                board.clear_board() # clears the board to reset
                user_number = ""
        elif exit_game_button.hovering(x, y):
            if mouse_click:
                exit()
        else:
            if mouse_click:
                num_input = False
                enter = False
                current_button.set_color3(black)

                cell_number = ((x-234) // cell_size) + ((y - 34) // cell_size) * 9
                if cell_number < 81:
                    current_button = board.get_grid_list_button(cell_number)

# moving up/down/left/right in keypad ----> readjust current cell position
            if keypad != "":
                user_number = ""
                num_input = False
                if keypad == "up":
                    if cell_number >= 9:
                        current_button.set_color3(black)
                        cell_number -= 9
                        current_button = board.get_grid_list_button(cell_number)
                elif keypad == "down":
                    if cell_number < 72:
                        current_button.set_color3(black)
                        cell_number += 9
                        current_button = board.get_grid_list_button(cell_number)
                elif keypad == "left":
                    if cell_number % 9 != 0:
                        current_button.set_color3(black)
                        cell_number -= 1
                        current_button = board.get_grid_list_button(cell_number)
                elif keypad == "right":
                    if cell_number % 9 != 8:
                        current_button.set_color3(black)
                        cell_number += 1
                        current_button = board.get_grid_list_button(cell_number)
                keypad = ""
            clickable = current_button.get_clickable()

            if clickable:
                current_button.set_color3(red)
                board.update_buttons(cell_number)
                sketched_text = current_button.get_text()
                if num_input:
                    current_button.set_text(str(user_number), False)
                    current_button.set_color1(grey)
                    board.set_grid_list_button(cell_number, current_button)
                if enter:
                    num_input = False
                    user_number = ""
                    if sketched_text != "":
                        current_button.set_color1(blue)
                        current_button.set_text(sketched_text, True)
                        current_button.set_color3(blue)
                        board.set_grid_list_button(cell_number, current_button)
                        screen = board.submit_button(cell_number, sketched_text)
                    enter = False


    if screen == "game_lose":
        original_surface.fill(white)
        original_surface.blit(home_background, (0, -30))
        restart_button.draw_button()
        display_text("Game Over :(", WIDTH / 2, 120, title_text, black, white)

        if restart_button.hovering(x + 5, y):
            if mouse_click:
                screen = "home"
        else:
            update_cursor(x,y)
    if screen == "game_win":
        original_surface.fill(white)
        original_surface.blit(home_background, (0, -30))
        exit_button.draw_button()
        display_text("Game Won!!!", WIDTH / 2, 120, title_text, black, white)

        if exit_button.hovering(x + 5, y):
            if mouse_click:
                exit()
        else:
            update_cursor(x, y)

    pygame.display.update()
    return screen

# this is the main function, incorporates all previous classes/methods
def main():
    global screen
    global mouse_click
    global num_input
    global user_number
    global enter
    global keypad

    num_input = False
    mouse_click = False
    clock = pygame.time.Clock()
    boolean = True
    while boolean:
        clock.tick(fps)
        for occurrence in pygame.event.get():
            if occurrence.type == pygame.QUIT:
                boolean = False
            mouse_click = True if occurrence.type == pygame.MOUSEBUTTONDOWN else False
            if pygame.KEYDOWN == occurrence.type:
                num_input = True
                if occurrence.key == pygame.K_1 or occurrence.key == pygame.K_KP1:
                    user_number = 1
                elif occurrence.key == pygame.K_2 or occurrence.key == pygame.K_KP2:
                    user_number = 2
                elif occurrence.key == pygame.K_3 or occurrence.key == pygame.K_KP3:
                    user_number = 3
                elif occurrence.key == pygame.K_4 or occurrence.key == pygame.K_KP4:
                    user_number = 4
                elif occurrence.key == pygame.K_5 or occurrence.key == pygame.K_KP5:
                    user_number = 5
                elif occurrence.key == pygame.K_6 or occurrence.key == pygame.K_KP6:
                    user_number = 6
                elif occurrence.key == pygame.K_7 or occurrence.key == pygame.K_KP7:
                    user_number = 7
                elif occurrence.key == pygame.K_8 or occurrence.key == pygame.K_KP8:
                    user_number = 8
                elif occurrence.key == pygame.K_9 or occurrence.key == pygame.K_KP9:
                    user_number = 9
                elif occurrence.key == pygame.K_RETURN:
                    enter = True
                elif pygame.K_UP == occurrence.key:
                    keypad = "up"
                elif pygame.K_DOWN == occurrence.key:
                    keypad = "down"
                elif pygame.K_RIGHT == occurrence.key:
                    keypad = "right"
                elif pygame.K_LEFT == occurrence.key:
                    keypad = "left"
        screen = draw_screen(screen)
    exit()

if __name__ == "__main__":
    main()
