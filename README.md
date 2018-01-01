# Genetic_Flappy_Bird
Implementation of Genetic Algorithm
Created with Python, Pygame

1) Created a Population of Birds with its own Neural Network
2) Each Neural Network has 4 layers (input layer, hidden layer 1, hidden layer 2, and output layer)
        - the input consist of the horizontal and vertical difference from the pipe to the bird
        - if output is greater than .5, itll flap to go up.
3) Once all the birds deads, itll repopulate with the top 3 birds to breed a new population of 10.
4) the Genetic Algorithm has a 20% chance to mutate each layer of each bird's neural network.
5) it will keep repopulating until they find a neural network that works well.
        

