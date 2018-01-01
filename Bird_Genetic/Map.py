import sys, pygame, random, os



class Map:

	def __init__(self,generation):
		# super the pygame libary
		pygame.init()
		# set up the generation display text
		wordfont = pygame.font.SysFont("sans",35)
		self.generation = wordfont.render("Gen: "+str(generation), True, (255, 255, 255))
		# where the window will open
		os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
		# ccaption for the window
		caption = "A Pygame that runs a genetic algorithm of flappy bird"
		# set up for the background image

		self.bg = pygame.image.load("resources/background/background.gif")
		self.bgRect = self.bg.get_rect()
		# set up the pygame window to be the same size as the background
		size = width, height = self.bg.get_size() 
		self.screen = pygame.display.set_mode((size[0]+200,size[1]))

		# set up the images for the pipes and floor
		self.wallUp = pygame.image.load("resources/background/bottom_pipe.gif")
		self.wallDown = pygame.image.load("resources/background/top_pipe.gif")
		self.floor = pygame.image.load("resources/background/floor.gif")

		pygame.display.set_caption(caption, 'Genetic Birds')

		# set up the intial walls and their position
		self.wall_1= 300
		self.wall_2 = 700
		# the gap between the pipes
		self.gap = 200
		# the offset of the pipes being higher or lower
		self.offset_1 = 0
		self.offset_2 = random.randint(-200, 200)


	def show_display(self):
		# display the images onto the pygame screen
		self.screen.blit(self.bg, (0,0))
		self.screen.blit(self.wallUp,
			(self.wall_1, 360+self.gap+self.offset_1))
		self.screen.blit(self.wallDown,
			(self.wall_1, 0-self.gap+self.offset_1))
		self.screen.blit(self.wallUp,
			(self.wall_2, 360+self.gap+self.offset_2))
		self.screen.blit(self.wallDown,
			(self.wall_2, 0-self.gap+self.offset_2))
		self.screen.blit(self.floor,
			(0, 900))
		self.screen.blit(self.generation, (25, 25))





	def wall_update(self):
		# makes the wall move and update the new wall if the wall reaches to the middle
		self.wall_1 -= 2
		self.wall_2 -= 2
		if(self.wall_1 == 300):
			self.offset_2 = random.randint(-200, 200)
			self.wall_2 = 700
		elif(self.wall_2 == 300):
			self.wall_1 = 700
			self.offset_1 = random.randint(-200, 200)


	def closest_hor_wall(self):
		# checks for the closest wall and gets its position
		if(self.wall_1 <= -45 and self.wall_2 > self.wall_1):
			return self.wall_2+90
		elif(self.wall_2 <= -45 and self.wall_1 > self.wall_2):
			return self.wall_1+90
		elif(self.wall_1 < self.wall_2):
			return self.wall_1+90
		elif(self.wall_2 < self.wall_1):
			return self.wall_2+90

	def closest_vert_wall(self):
		# gets the closest wall and get its vertical position 
		closest_wall = self.closest_hor_wall()
		if(closest_wall - 90 == self.wall_1):
			return 360+self.offset_1+(self.gap/2)
		elif(closest_wall - 90 == self.wall_2):
			return 360+self.offset_2+(self.gap/2)



