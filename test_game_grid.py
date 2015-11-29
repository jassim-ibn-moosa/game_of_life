import game_grid

grid =  game_grid.get_grid()

def test_is_alive_true():
    alive = game_grid.is_alive(0,1,grid)
    assert alive == True  
def test_is_alive_false():
    alive = game_grid.is_alive(0,0,grid)
    assert alive == False

def test_live_neighbour_count():
    live_neighbours_count = game_grid.live_neighbour_count(0,0,grid)
    assert live_neighbours_count == 2
    live_neighbours_count = game_grid.live_neighbour_count(0,1,grid)
    assert live_neighbours_count == 1
    live_neighbours_count = game_grid.live_neighbour_count(0,2,grid)
    assert live_neighbours_count == 2
    live_neighbours_count = game_grid.live_neighbour_count(1,0,grid)
    assert live_neighbours_count == 3
    live_neighbours_count = game_grid.live_neighbour_count(1,1,grid)
    assert live_neighbours_count == 2
    live_neighbours_count = game_grid.live_neighbour_count(1,2,grid)
    assert live_neighbours_count == 3
    live_neighbours_count = game_grid.live_neighbour_count(2,0,grid)
    assert live_neighbours_count == 2
    live_neighbours_count = game_grid.live_neighbour_count(2,1,grid)
    assert live_neighbours_count == 1
    live_neighbours_count = game_grid.live_neighbour_count(2,2,grid)
    assert live_neighbours_count == 2

def test_new_grid():
	new_grid = game_grid.play_game(grid,grid)
	new_grid = [[0,1,0],
		    [0,1,0],
		    [0,1,0]]
    
