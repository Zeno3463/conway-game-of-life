import pygame
from pygame import display, draw, time
import numpy
pygame.init()


WIDTH = 500
HEIGHT = 500
SCREEN = display.set_mode([WIDTH, HEIGHT])
GREY = (50, 50, 50)
BLOCK_SIZE = 10
running = True
grid = numpy.zeros((WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE))

grid[10, 10] = 1
grid[10, 11] = 1
grid[10, 12] = 1
grid[9, 12] = 1
grid[8, 11] = 1

def draw_grid():
	for x in range(0, WIDTH, BLOCK_SIZE):
		for y in range(0, HEIGHT, BLOCK_SIZE):
			rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
			# if this position has a cell, fill the block with grey
			width = 0 if grid[y // BLOCK_SIZE, x // BLOCK_SIZE] == 1 else 1
			draw.rect(SCREEN, GREY, rect, width)

def click(pos):
	y, x = pos
	grid[x // BLOCK_SIZE, y // BLOCK_SIZE] = 1

def next_gen():
	time.wait(500)
	new_grid = grid
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			live_neighbors_count = 0
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

			if (live_neighbors_count < 2 or live_neighbors_count > 3) and grid[x, y]:
				new_grid[x, y] = 0
			elif not grid[x, y] and live_neighbors_count == 3:
				new_grid[x, y] = 1
	return new_grid

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			click(pygame.mouse.get_pos())
	SCREEN.fill((0, 0, 0))
	draw_grid()
	display.update()
	grid = next_gen()

pygame.quit()