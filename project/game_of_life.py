# 2D grid 30rows x 80 columns
# arguments: ticks,cells-on (formated like: row:col row:col etc)
#

# create initial grid:
r = 3; c = 8           #size of grid, will be 30x80
row1 = 1; col1 = 4    #cell indexes from user
row2 = 2; col2 = 5
grid = ['-'] * r        #create rows of dashes
for i in range(r):
    grid[i] = ['-'] * c  #loop through rows to create columns
    #print(i,row1)
    #---------this needs to be separate fcn to iterate through-----
    if i == row1-1:             #find cells that should be ON
       grid[i][col1-1] = 'X'    #change to X
    if i == row2-1:
        grid[i][col2-1] = 'X'
    #-----------------------------------------------------------
    print(''.join(grid[i][:]))       #print out grid
#return(grid)
#----new function to check neighbors-------
#find ON cells, convert to True
bool_grid = [False] * r
for i in range(r):
    bool_grid[i] = [False] * c

for i in range(r):
    for j in range(c):
       if grid[i][j] == 'X':
          bool_grid[i][j] = True
       #else:
           #bool_grid[i][j] = False
    row_count = sum(bool_grid[i][:])
    print(row_count)
print('\n',bool_grid)

#create indices to check neighbors using user inputed rows & columns
neighbor_coords = []
for i in range(8):
    neighbor_coords.append([0]*2)
print(neighbor_coords)

row = row1
col = col1
print(row,col)
neighbor_coords[0][0] = row - 2  #NW
neighbor_coords[0][1] = col - 2
neighbor_coords[1][0] = row - 2  #N
neighbor_coords[1][1] = col - 1
neighbor_coords[2][0] = row - 2  #NE
neighbor_coords[2][1] = col
neighbor_coords[3][0] = row - 1  #E
neighbor_coords[3][1] = col
neighbor_coords[4][0] = row      #SE
neighbor_coords[4][1] = col
neighbor_coords[5][0] = row      #S
neighbor_coords[5][1] = col - 1
neighbor_coords[6][0] = row - 2  #SW
neighbor_coords[6][1] = col
neighbor_coords[7][0] = row - 1  #W
neighbor_coords[7][1] = col - 2

print(neighbor_coords)
