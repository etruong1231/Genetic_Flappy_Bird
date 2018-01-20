import pygame
import Map
import numpy as np
import random
import os

class Bird:

	def __init__(self, Map, image1, image2,name,Weights):
		'''set up the map and the type of bird class'''
		# makes sure all the bird is using the same screen
		self.map = Map
		# set up what type of bird it is 
		self.name = name
		# images for the birds for flying and diving
		self.bird_up =  pygame.image.load(image1)
		self.bird_down = pygame.image.load(image2)
		# set the image as the bird going down
		self.bird_type = self.bird_down

		self.bird_dim = (width, height) = self.bird_up.get_width(), self.bird_up.get_height()


		# the status of the bird
		self.alive = True

		# set up the weights for the neural network
		self.weights = Weights

		# the starting position of the birds
		self.curr_pos = np.random.randint(200,500)
		self.x_pos = 50
		self.gravity = 0

		# the fitness score of how far the birds move along the map
		self.score = 0

	# activation function for the birds
	def sigmoid(self,x):
		sig = 1 / (1 + np.exp(-x))
		return sig


	# updates the bird everytime it does flap or does not	
	def show_bird(self):
		''' displays the bird onto the screen'''
		# check if the bird is alive before doing any action
		if(self.alive):
			self.map.screen.blit(self.bird_type,(
				self.x_pos,self.curr_pos))
			self.curr_pos+= 5.22 + self.gravity
			self.gravity += .01
			self.bird_type = self.bird_down
			self.score+= 1
		# the bird is dead and move out of screen
		else:
			self.curr_pos = 2000

	
	def check_collision(self):
		'''check if the bird is colliding with the pipes'''
		# get the width and height of the pipe 
		wall = (width, height) = self.map.wallUp.get_width(), self.map.wallUp.get_height()
		
		# get the bird dim on the map
		bird_rect = pygame.Rect(self.x_pos,self.curr_pos, self.bird_dim[0], self.bird_dim[1])
		
		# get the rect of the first set of pipe and position
		upRect1 = pygame.Rect(self.map.wall_1,
			360 + self.map.gap + self.map.offset_1+5,
            wall[0], wall[1])
		downRect1 = pygame.Rect(self.map.wall_1,
            0 - self.map.gap + self.map.offset_1-5,
            wall[0]-5 ,wall[1])
		# get the rect of the second set of pipe and position
		upRect2 = pygame.Rect(self.map.wall_2,
			360 + self.map.gap + self.map.offset_2+5,
            wall[0], wall[1])

		downRect2 = pygame.Rect(self.map.wall_2,
            0 - self.map.gap + self.map.offset_2-5,
            wall[0] ,wall[1])

		# check if the position of the bird hits the roof or the floor
		if(not bird_rect[1] <= 900 or not bird_rect[1] >= 0):
			self.alive = False

		# checks the bird collides with any of the pipes
	
		if ((bird_rect.colliderect(upRect1)) or 
			(bird_rect.colliderect(downRect1)) or 
		    (bird_rect.colliderect(upRect2)) or
		    (bird_rect.colliderect(downRect2))):
			self.alive = False
			
	def fitness_score(self):
		'''fitness score of the bird'''
		#print(self.name, self.score)
		return self.score

	def action(self):
		''' the action will be determined by the neural network'''
		# the two input would be the horizontal difference between the bottom of the pipe and the bird
		# gets the pipe that is closest to the bird
		hor_wall = self.map.closest_hor_wall()
		vert_wall = self.map.closest_vert_wall()

		# differences of the bird to the set of pipes
		horiz_dif = np.float((hor_wall-(self.x_pos+self.bird_dim[0])))/100
		verti_dif = np.float(vert_wall-(self.curr_pos+(self.bird_dim[1]/2)))/100
		#print(horiz_dif,verti_dif)

		# the input layer will consist of horiz_dif and verti_dif
		input_layer = np.array([verti_dif,horiz_dif])
		# does feed forwward to the next layer of the network
		hidden_layer1 = self.sigmoid(np.dot(input_layer,self.weights[0]))
		hidden_layer2 = self.sigmoid(np.dot(hidden_layer1, self.weights[1]))
		#after feeding each layer it gets the single output.
		output = self.sigmoid(np.dot(hidden_layer2,self.weights[2]))

		return output

	def bird_update(self):
		# if the bird does flap forward
		if(self.alive):
			action = self.action()
			#print(self.name,str(action))
			if(action >= .50 ):
				self.curr_pos-= 62.33
				self.bird_type = self.bird_up
				self.gravity = 0
				
		else:
			self.curr_pos = 2000






