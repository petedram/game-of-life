
from random import randint

'''
Cell class with:
- status of alive or dead
- method to set alive
- method to set dead
- method to check status
- method to print

'''

class Cell:
    def __init__(self):
        self._status = 'dead'
    
    def set_dead(self):
        self._status = 'dead'

    def set_alive(self):
        self._status = 'alive'

    def check_alive(self):
        if self._status == 'alive':
            return True
        else:
            return False

    def print_cell(self):
        if self.check_alive():
            return '1'
        else:
            return '0'


'''
grid class with:

- ability set the rows and columns
- store the generation_count
- a method to draw out the grid
- a method to check the neighbours of each cell
- a method to update the board based on status of each cell in the next generation

'''

class Grid:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self.generation_count = 0
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]
        
        #build grid
        self._build_grid()

    def increment_generation(self):
        self.generation_count +=1

    def draw_grid(self):
        print('printing grid')
        for row in self._grid:
            for column in row:
                #change this to add to array
                some_array.append(column.print_cell(),end='')
                # print(column.print_cell(),end='')
            # print () #new line
    
    def _build_grid(self):
        #random
        for row in self._grid:
            for column in row:
                rand = randint(0,2)
                if rand == 1:
                    column.set_alive()

    def check_neighbour(self, check_row, check_column):

        neighbour_list = []
        for row in range(-1, 2): #the min and max
            for column in range(-1, 2):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                valid_neighbour = True

                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_neighbour = False

                if (neighbour_row) < 0 or (neighbour_row) >= self._rows:
                    valid_neighbour = False

                if (neighbour_column) < 0 or (neighbour_column) >= self._columns:
                    valid_neighbour = False

                #if we get to here and still true then append it
                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])

        return neighbour_list 

    def update_board(self):
        self.increment_generation()
        print (f'updating board for generation: {self.generation_count}')
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                
                check_neighbour = self.check_neighbour(row , column)

                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    if neighbour_cell.check_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.check_alive()

                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()


generation_count = 0
rows = 25
columns = 25

grid = Grid(rows,columns)

grid.draw_grid()

user_action = ''
while user_action != 'q':
    user_action = input('enter to add generation or q to quit:')

    if user_action == '':
        grid.update_board()
        grid.draw_grid()








