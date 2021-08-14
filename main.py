import pygame
from pygame import display, draw
import numpy
pygame.init()

WIDTH = 500
HEIGHT = 500
SCREEN = display.set_mode([WIDTH, HEIGHT])
GREY = (50, 50, 50)
BLOCK_SIZE = 100
running = True

grid = numpy.zeros((WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE))
grid[0, 1] = 1
print(grid)

def draw_grid():
	for x in range(0, WIDTH, BLOCK_SIZE):
		for y in range(0, HEIGHT, BLOCK_SIZE):
			rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
			width = 0 if grid[y // BLOCK_SIZE, x // BLOCK_SIZE] == 1 else 1
			draw.rect(SCREEN, GREY, rect, width)

def click(pos):
	print(pos)

def next_gen():
	pass

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			click(pygame.mouse.get_pos())

	SCREEN.fill((0, 0, 0))
	draw_grid()
	display.update()

pygame.quit()