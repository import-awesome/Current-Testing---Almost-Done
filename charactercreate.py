import pygame
import chartemplate
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 255, 0)
clock = pygame.time.Clock()

class Create(object):
	def __init__(self, s, win_x, win_y):
		self.screen = s
		self.winx = win_x
		self.winy = win_y

	def Display(self):
		display = True
		go = False
		party = []
		partysize = 0
		while display:
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					display = False
					go = True


			clock.tick(60)
			pygame.display.flip()

		if go == True:
			pygame.quit()
			return -1

		return 0



if __name__ == "__main__":
	screen = pygame.display.set_mode((500, 500))
	Create(screen, 500, 500).Display()