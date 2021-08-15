import pygame
from pygame import display, draw, time
import numpy
pygame.init()


WIDTH = 500
HEIGHT = 500
SCREEN = display.set_mode([WIDTH, HEIGHT])
GREY = (50, 50, 50)
WHITE = (100, 100, 100)
BLACK = (0, 0, 0)
BLOCK_SIZE = 10
running = True
start_simulation = False
grid = numpy.zeros((WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE))


def draw_grid():
	for x in range(0, WIDTH, BLOCK_SIZE):
		for y in range(0, HEIGHT, BLOCK_SIZE):
			rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
			# if this position has a cell, fill the block with grey
			width = 0 if grid[y // BLOCK_SIZE, x // BLOCK_SIZE] == 1 else 1
			draw.rect(SCREEN, GREY, rect, width)

def click(pos):
	y, x = pos
	# invert the state of the block the user clicked
	grid[x // BLOCK_SIZE, y // BLOCK_SIZE] = 1 if not grid[x // BLOCK_SIZE, y // BLOCK_SIZE] else 0

def next_gen():
	# delay for 0.5 second
	time.wait(100)
	new_grid = numpy.zeros_like(grid)

	# iterate through all blocks in the grid
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			live_neighbors_count = 0
			# iterate through all the the block's neighbors. If the neighbor is live, increment the live_neighbors count.
			try: 
				if grid[x-1, y-1]: live_neighbors_count += 1
			except: pass
			try: 
				if grid[x, y-1]: live_neighbors_count += 1
			except: pass
			try: 
				if grid[x+1, y-1]: live_neighbors_count += 1
			except: pass
			try: 
				if grid[x-1, y]: live_neighbors_count += 1
			except: pass
			try: 
				if grid[x+1, y]: live_neighbors_count += 1
			except: pass
			try: 
				if grid[x-1, y+1]: live_neighbors_count += 1
			except: pass
			try: 
				if grid[x, y+1]: live_neighbors_count += 1
			except: pass
			try: 
				if grid[x+1, y+1]: live_neighbors_count += 1
			except: pass

			# any live cell with two or three neighbors survive
			# any dead cell with three live neighbors becomes a live cell
			# other live cells die in the next generation
			# other dead cells stay dead
			if grid[x, y] and (live_neighbors_count == 2 or live_neighbors_count == 3):
				new_grid[x, y] = 1
			elif live_neighbors_count == 3:
				new_grid[x, y] = 1

	return new_grid


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			click(pygame.mouse.get_pos())
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			start_simulation = not start_simulation

	SCREEN.fill(WHITE)
	draw_grid()
	display.update()
	if start_simulation: grid = next_gen()

pygame.quit()