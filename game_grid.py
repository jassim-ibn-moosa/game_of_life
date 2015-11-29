
def get_grid():
    grid = [[0,1,0],
            [0,1,0],
            [0,1,0]]
    return grid

def is_alive(x,y,grid):
    if grid[x][y] == 1:
        return True
    else:
        return False

def live_neighbour_count(x,y,grid):
    neighbour_count = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue
            elif dx+x < 0 or y+dy < 0:
                continue
            else:
                try:
                    if is_alive(x+dx, y+dy, grid):
                        neighbour_count += 1
                except IndexError:
                    continue
    return neighbour_count

def play_game(grid, new_grid):
    neighbour_count = 0
    for x in range(3):
        for y in range(3):
            neighbour_count = live_neighbour_count(x,y,grid)
            if is_alive(x,y,grid) and neighbour_count < 2:
                new_grid[x][y] = 0#kill_cell(x,y,new_grid)
            elif is_alive(x,y,grid) and neighbour_count <= 3 :
                new_grid[x][y] = 1#stay_alive(x,y,new_grid)
            elif is_alive(x,y,grid) and (neighbour_count >3) :
                new_grid[x][y] = 0#kill_cell(x,y,new_grid)
            elif not is_alive(x,y,grid) and (neighbour_count == 3):
                new_grid[x][y] = 1
    return new_grid

def main():
    grid = get_grid()
    x = 'n'
    new_grid = get_grid()
    print grid
    print play_game(grid, new_grid)

if __name__ == "__main__":
    main()
    
