import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = int(row_length)
        self.removed_cells = int(removed_cells)
        self.board = [[0 for i in range(row_length)] for j in range(row_length)]
        self.box_length = math.sqrt(row_length)

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        for row in self.board:
            print(row)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        #Create list of every occurrence of num in row. If the length of the list is greater than zero, then
        #num is not valid in row.
        row = int(row)
        occurrences = [x for x in self.board[row] if x == num]
        if len(occurrences) > 0:
            return False
        else:
            return True
    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        #Create list of every element in specified column, then create list of every occurrence of num in column list.
        #If the length of the list is greater than zero, then num is not valid in col.
        col = int(col)
        column = [x[col] for x in self.board]
        occurrences = [x for x in column if x == num]
        if len(occurrences) > 0:
            return False
        else:
            return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        #Create list of every element in specified box, and then another list of every occurence of num in box list.
        #If the length of the list of occurences is greater than zero, then num is not valid in box
        boxlist = []
        row_start = int(row_start)
        col_start = int(col_start)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                boxlist.append(self.board[i][j])
        occurrences = [x for x in boxlist if x == num]
        if len(occurrences) > 0:
            return False
        else:
            return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num):
            if self.valid_in_col(col, num):
                if self.valid_in_box((row // self.box_length) * 3, (col // self.box_length) * 3, num):
                    return True
        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        #chars is a list of integers 1-9.
        chars = [i for i in range(1, 10)]
        #Iterate thru every element in specified box. Pick a random element from chars list and assign its value to
        #the box element currently being iterated. Then remove that selected random element from chars list to assure
        #no numbers are repeated in the specified box.
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                num = random.choice(chars)
                chars.remove(num)
                self.board[i][j] = num
        pass

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(3):
            self.fill_box(3 * i, 3 * i)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 0)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        #Pick two random numbers (x and y) between 0 and row_length. If board[x][y] isn't zero, then make it zero.
        #If it's already zero, leave it alone and pick a new set of two numbers
        #Repeat this process for however many cells they wanted removed from the solution
        for i in range(self.removed_cells):
            while True:
                x, y = random.randint(0, self.row_length), random.randint(0, self.row_length)
                if self.board[x][y] == 0:
                    continue
                else:
                    break
            self.board[x][y] = 0

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board