from src.vision import get_obstacle_grid
from src.simulation import run_simulation

if __name__ == "__main__":
    grid = get_obstacle_grid()
    run_simulation(grid)