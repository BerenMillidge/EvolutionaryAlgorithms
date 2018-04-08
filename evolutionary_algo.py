# following the tutorial from here - https://blog.sicara.com/getting-started-genetic-algorithms-python-tutorial-81ffa1dd72f9
# thought it would be a good idea to get some idea how evolutioanry algorithms work
# since that is interesting and they are a whole section of AI and stochastic optimisation
# territory that I know very little about at the moment - starting off with jsut a very simple
# wxample tutorial - to crack a password

from __future__ import division
import numpy as np 
import math
import random
import operator


def fitness(password, test_word):
	if (len(test_word) !=len(password)):
		raise ValueError('password and test word must be same length')

	score = 0
	i = 0
	while i <len(password):
		if password[i] == test_word[i]:
			score+=1
		i+=1
	return score * 100 / len(password)

#create a population of words consisting of random lettesr to get maximum variability

def generateAWord(length):
	result = ""
	for i in range(length):
		letter = chr(97+int(26*random.random())) #is this a direct conversion to unicode?
		result +=letter
	return result

def generateFirstPopulation(population_size, password)
population = []
for i in range(population_size):
	population.append(generateAWord(len(password)))
return population


# so each generation select N of the best specimens and M lucky fews without distinciton of fitness
# to evolve the population randomly

def computePerfPopulation(population, password):
	populationPerf = {}
	for individual in population:
		populationPerf[individual] = fitness(password, individual)
	return sorted(populationPerf.items(), key=operator.itemgetter(1), reverse=True)

def selectFromPopulation(populationSorted, best_sampel, lucky_few):
	nextGeneration = []
	#add the best samples
	for i in range(best_sample):
		nextGeneration.append(populationSorted[i][0])

	for i in range(lucky_few):
		nextGeneration.append(random.choide(populationSorted)[0])
	random.shuffle(nextGeneration)
	return nextGeneration

# so the next step is the "breeding" of solutions - here it just randomly creates the child
# by taking the letter of parent a or parent b randomly

def create_child(individual1, individual2):
	if len(individual1)!=len(individual2):
		raise ValueError('Lengths of the indivudals must be equal')

	child = ""
	for i in range(len(individual1)):
		if int(random.random<=0.5):
			child+=individual1[i]
		else: 
			child +=individual2[i]
	return child

#and create the children just from the population selecting randomly
def createChildren(breeders, number_of_children):
	nextPopulation = []
	for i in range(len(breeders)/2):
		for j in range(number_of_children):
			nextPopulation.append(createChild(breeders[i], breeders[len(breeders)-1 -i]))
		return nextPopulation

#the final step is mutation - i.e. after breeding each individual must have a small oepration
# fortheir dna to change a little- so to hence stop the algorithm being blocked in a local minimum

def mutateWord(word):
	index_modification = int(random.random()*len(word))
	if (index_modification==0):
		word = chr(97+int(26*random.random())) + word[1:]
	else:
		word = word[:index_modification] + chr(97+int(26*random.random()))  + word[index_modification+1:]
	return word

def mutatePopulation(population, chance_of_mutatoin):
for i in range(len(population)):
	if random.random()*100 <chance_of_mutatoin:
		population[i] = mutateWord(population[i])
return population 

