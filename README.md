Intro AI
========

Sample code for various introductory concepts of artificial intelligence

#Neural Networks
??space of candidate hypothesis

Artificial Intelligence: A Modern Approach (Part V, chapter 18)
Machine Learning [Mitchell T.] (chapter 4)
##Percetron
Composed by weights, summation processor, activation function and adjustable threshold processor (bias).  
Similarity with neurons. Input from dendrites and output from axon (that then branches into synapses, inhibitory or excitatory).  

We can consider the "decision space" as a n-dimensional hyperplane with n equal to the number of inputs. 
The XOR is not linearly separable, so it cannot be computed by a single layer neural network.
??However we can use another function instead of the step one, like Delta Rule
The *Delta Rule* use the concept of gradient descent (incremental: error summed over all examples before update, or stochastic: update at each example).
!!Almost the same as the basic perceptron rule (change only from linear to to thresholded output)

??Decay of learning rate during training session

##Multi layer
Adding the so called hidden layers. 
Learning types:
	- *Reinforcement*: how wrong you are;
	- *Supervised*: where you are wrong;
	- *Unsupervised*: no feedback at all;
	- *Semi-supervised*:
*Back Propagation*: adjusting weights at the output level, and then back-propagate error calculation and adjustment to previous layers. 
Use momentum in order to emphasize consistent "directions".

!!overfitting phenomenon

#Genetic Algorithm
Machine Learning [Mitchell T.] (chapter 9, pg 249)

A chromosome is a single piece of coiled DNA containing many genes. Each chromosome encodes a possible solution to the problem.

Common generic operations are the selection, the crossover and the mutation.
"Elitism" is instead about keeping the bests in the population. To achieve this we could also change only "losers" (during crossover and mutation)

*Selection*: "roulette wheel", tournament or rank selection 
*Crossover*: single-point, two-point or uniform

??Genetic programming
