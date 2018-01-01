from Map import Map
import pygame
import numpy as np
import os
from Genetic_Algor import Genetic_Algor as ga

class Simulation:


	def __init__(self):
		# current generation is at
		self.generation = 1
		# lets the map show what generation it is on
		self.map = Map(self.generation)
		# starts the genetic algorithm
		self.gene_alg = ga()
		# gets the population of birds from the algorithm
		self.birds = self.gene_alg.population(self.map)
	
		
		

	def check_all_bird_alive(self):
		'''check if all birds are alive or not'''
		for birds in self.birds.values():
			if (birds.alive == True):
				return True
		return False

	def simulate(self):
		# the handler that runs the simulation
		while(True):
			self.run()
			
			

	def run(self):
		# set the clock for the pygame to run at
		game_clock = pygame.time.Clock()
		# set a custom event that happens every 140ms for the bird to flap or not
		pygame.time.set_timer(pygame.USEREVENT+1, 140)
		running = True
		try:
		    while running:
		    	# set the fps of the simulation
		    	game_clock.tick(60)
		    	# the event that could happen with pygame
		        for event in pygame.event.get():
		        	# in case if user quit the simulation
		            if event.type == pygame.QUIT:
		                running = False
		            # does the custom action for the bird
		            elif event.type == pygame.USEREVENT+1:
		            	for birds in self.birds.values():
		        			birds.bird_update()
		       	# display the pipes and background
		        self.map.show_display()
		        # update the position of the birds onto the maps
		        for birds in self.birds.values():
		        	birds.show_bird()
		        # updates the pipes and background for the game
       			self.map.wall_update()
       			# update the whole pygame
          		pygame.display.flip()
          		# need to check for collsiion
          		for birds in self.birds.values():
          			birds.check_collision()
          		#check if all the birds are dead 
          		if(not self.check_all_bird_alive()):
          			# create a new population of the top 4 birds
          			self.generation+=1
          			self.map = Map(self.generation)
          			self.birds = self.gene_alg.breed(self.map, self.birds)
          			game_clock = pygame.time.Clock()
          			
		    pygame.quit()
		    quit()
		except SystemExit:
			print("Quitting")
		    






if __name__ == '__main__':
	genetic_sim = Simulation()
	genetic_sim.simulate()
