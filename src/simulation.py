import pygame
import time
from src.astar import astar

WIDTH = 600
ROWS = 20
CELL = WIDTH // ROWS

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)
GRAY = (200,200,200)

def draw(win, grid, path, start, goal, index):
    win.fill(WHITE)

    for i in range(ROWS):
        for j in range(ROWS):
            rect = pygame.Rect(j*CELL, i*CELL, CELL, CELL)

            if grid[i][j] == 1:
                pygame.draw.rect(win, BLACK, rect)
            elif (i,j) == start:
                pygame.draw.rect(win, BLUE, rect)
            elif (i,j) == goal:
                pygame.draw.rect(win, RED, rect)
            elif (i,j) in path[:index]:
                pygame.draw.rect(win, GREEN, rect)
            else:
                pygame.draw.rect(win, WHITE, rect)

            pygame.draw.rect(win, GRAY, rect, 1)

def run_simulation(grid):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Autonomous Navigation - Vision Based")

    start = (13,6)
    goal = (19,0)

    path = astar(grid, start, goal)

    if not path:
        print("No path found!")
        return

    running = True
    index = 0

    clock = pygame.time.Clock()

    while running:
        clock.tick(10)

        draw(win, grid, path, start, goal, index)

        if index < len(path):
            index += 1
            time.sleep(0.1)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()