"""Python script that creates Conway's Game of Life grid

.. module:: game_of_life
    :synopsis: for AFS505_u1, see conwaylife.com

.. moduleauthor:: Lana Cohen

"""
import sys
script, ticks, *args = sys.argv

def initialize(grid,bool_grid,*args):
    """Takes initial coordinates (args) and creates list of ON cells and
    modifies grid and bool_grid.
    :param grid: grid of dashes and Xs to be printed out
    :type grid: string array
    :param bool_grid: copy of grid where -- are False (off) and XX are True (on)
    :type bool_grid: boolean array
    :param args: initial coordinate pairs (row:column)
    :type args: list of integers between 1-30 & 1-80

    :return: grid and bool_grid changed from original based on *args
    :rtype: arrays sized r rows by c columns
    """
    cells_on = []
    for i in range(len(args)):
        coords = args[i].split(':')  # format coordinates into list of strings
        cells_on.append(coords)
    for i in range(len(cells_on)):
        cells_on[i][0] = int(cells_on[i][0])  #must convert strings to integers
        cells_on[i][1] = int(cells_on[i][1])
        cells_on[i][0] = cells_on[i][0] - 1    #convert to python coords
        cells_on[i][1] = cells_on[i][1] - 1
    #print("Cells on = ",cells_on)

    #change ON cells to Xs, and TRUE in bool_grid
    for i in range(len(cells_on)):
        grid[cells_on[i][0]][cells_on[i][1]] = 'X'   #change values to 'X'
        bool_grid[cells_on[i][0]][cells_on[i][1]] = True #change values to True

    return(grid,bool_grid)

def print_grid(r,grid):
    """Prints out grid
    :param r: # of rows to iterate through
    :type r: integer
    :param grid: grid of --s and XXs
    :type grid: string array
    """
    for i in range(r):
        print(''.join(grid[i][:]))
    print('\n')

def neighbor_calc(grid,bool_grid,r,c):
    """Creates n_sum array which gives neighbor sum for each cell, then changes
    cells in bool_grid based on the rules.
    Then changes grid based on bool_grid and prints grid out to screen.
    :param grid: grid of --s and XXs
    :type grid: string array
    :param bool_grid: boolean array
    :param r & c: # of rows and columns (integers)

    :return: bool_grid and grid
    :rtype: arrays
    """
    n_sum = [0] * r      #create/reinitialize r-by-c array of neighbor sums
    for i in range(r):
        n_sum[i] = [0] * c

    for i in range(1,r-1):   #*********excludes edges***********
        for j in range(1,c-1):
           n_sum[i][j] = sum([bool_grid[i+1][j],bool_grid[i-1][j],bool_grid[i][j-1],bool_grid[i][j+1],bool_grid[i+1][j+1],bool_grid[i+1][j-1],bool_grid[i-1][j+1],bool_grid[i-1][j-1]])

    # change bool_grid based on rules
    for i in range(r):
        for j in range(c):
            if bool_grid[i][j] == 1 and n_sum[i][j] < 2:
                bool_grid[i][j] = False
            elif bool_grid[i][j] == 1 and (n_sum[i][j] == 2 or n_sum[i][j] == 3):
                bool_grid[i][j] = True
            elif bool_grid[i][j] == 1 and n_sum[i][j] > 3:
                bool_grid[i][j] = False
            elif bool_grid[i][j] == 0 and n_sum[i][j] == 3:
                bool_grid[i][j] = True
            else:
                bool_grid[i][j] = False
    # change grid symbols based on bool_grid
    for i in range(r):
        for j in range(c):
            if bool_grid[i][j] == True:
                grid[i][j] = 'X'
            elif bool_grid[i][j] == False:
                grid[i][j] = '-'
    print_grid(r,grid)

    return(bool_grid,grid)

def main(ticks,*args):
    """Creates initial grids, then does initial modification based on
    coordinates given on command line. Prints first grid, then ticks
    through time-steps (given on command line) changing cells based
    on the rules given.
    """
    r = 30; c = 80           #size of grid
    #create grid of --s
    grid = ['-'] * r
    for i in range(r):
        grid[i] = ['-'] * c
    #create same grid with booleans (used to count neighbor sums)
    bool_grid = [False] * r
    for i in range(r):
        bool_grid[i] = [False] * c

    initialize(grid,bool_grid,*args)
    print_grid(r,grid)

    t = 1
    ticks = int(ticks)
    while t <= ticks:
        print("ticks =", t)
        neighbor_calc(grid,bool_grid,r,c)
        t += 1

main(ticks, *args)
