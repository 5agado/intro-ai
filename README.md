Intro AI
========

Sample code for various introductory concepts of artificial intelligence

#Neural Networks
##Percetron
Composed by weights, summation processor, activation function and adjustable threshold processor (bias).  
Similarity with neurons. Input from dendrites and output from axon (that then branches into synapses, inhibitory or excitatory).  

The XOR is not linearly separable, so it cannot be computed by a single layer neural network.

##Multi layer
Adding the so called hidden layers. 
Learning types:
	- *Reinforcement*: how wrong you are;
	- *Supervised*: where you are wrong;
Back Propagation: adjusting weights at the output level, and then back-propagate error calculation and adjustment to previous layers. Consider delta values in order to emphasize consistent "directions".

