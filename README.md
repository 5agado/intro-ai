Intro AI
========

Sample code for various introductory concepts of artificial intelligence

#Neural Networks
Artificial Intelligence: A Modern Approach (Part V, chapter 18)
##Percetron
Composed by weights, summation processor, activation function and adjustable threshold processor (bias).  
Similarity with neurons. Input from dendrites and output from axon (that then branches into synapses, inhibitory or excitatory).  

The XOR is not linearly separable, so it cannot be computed by a single layer neural network.

##Multi layer
Adding the so called hidden layers. 
Learning types:
	- *Reinforcement*: how wrong you are;
	- *Supervised*: where you are wrong;
	- *Unsupervised*: no feedback at all;
	- *Semi-supervised*:
Back Propagation: adjusting weights at the output level, and then back-propagate error calculation and adjustment to previous layers. Consider delta values in order to emphasize consistent "directions".

#Genetic Algorithm
A chromosome is a single piece of coiled DNA containing many genes. Each chromosome encodes a possible solution to the problem.

Common generic-related operations are the "roulette wheel", the crossover and the mutation.
"Elitism" is instead about keeping the bests in the population. To achieve this we could also change only "losers" (during crossover and mutation)


