import numpy as np
import os
from Birds import Bird
import random

class Genetic_Algor:


	def __init__(self):
		''' gets the bird objects and get the fitness scores and breed'''
		# for testing for a set of random seed
		#np.random.seed(9)
		# neurons at each layer of the neural network for each bird
		self.neurons = [2,10,5,1]
		# gets all the birds from the file and create them
		self.bird_dir_path = os.listdir("resources/birds/")

	def population(self, cur_map):
		''' creates a initial population for the simulation'''
		# creates a dictionary for the population
		# a dict of birds
		bird = {}
		for birds in self.bird_dir_path:
			# set up the weights for the neural network each bird
			weights = [2*np.random.random((self.neurons[x], 
				self.neurons[x+1]))-1 for x in range(3)]
			# create birds object with each of it own neural network
			bird[birds[:-4]] = Bird(cur_map,"resources/birds_2/"+str(birds),"resources/birds/"+str(birds), str(birds[:-4]),weights)
		return bird

	def mutation(self, weight1, weight2, weight3):
		''' has a chance to mutation the weights'''
		# gets the weight for the birds
		new_weights = [weight1,weight2,weight3]
		# give each layer of the neural network a chance to mutate
		for x in range(3):
			chance = np.random.randint(100)
			# .21 chance to mutate a layer
			if(chance <= 10):
				new_weights[x] = 2*np.random.random((self.neurons[x], 
				self.neurons[x+1]))- 1
		return new_weights




	def breed(self, cur_map, birds):
		''' breed 10 new birds from the top 3 scoring birds'''
		# gets the fitnes scores
		# gets all the keys from the dict
		key = list(birds.keys())
		# in case if all birds are tied every time, shuffle the fitness cores
		key = random.shuffle(key)
		random_list = [(key, birds[key]) for key in birds]

		
		# sort the fitness score of the birds
		fitness_scores = [(k,v) for (k,v) in sorted(random_list, key = lambda (k,v): v.fitness_score(), reverse= True)]
		# gets the top 3 birds 
		best_birds = fitness_scores[:4]
		# creates a new population with the top 3 birds
		new_birds = {}
		
		# creates a new population for each color of the birds
		for birds in self.bird_dir_path:
			par_1 = fitness_scores[np.random.randint(3)][1]
			par_2 = fitness_scores[np.random.randint(3)][1]
			par_3 = fitness_scores[np.random.randint(3)][1]
			# give the weights a chance to mutate
			new_weights = self.mutation(par_1.weights[0],par_2.weights[1],par_3.weights[2])
			# create the new bird population from the parents
			new_birds[birds[:-4]] = Bird(cur_map,"resources/birds_2/"+str(birds),"resources/birds/"+str(birds), str(birds[:-4]),new_weights)
		return new_birds



