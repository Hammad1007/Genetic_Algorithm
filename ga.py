import numpy as np
import pandas as pd
import random as rd

# Now begin with step 1
# First we will initialise the lists and randomly take the inputs

print('Taking the random input in the lists')
i = np.arange(1, 11)                            # values from 1 to 10 arranged
w = np.random.randint(1, 20, size = 10)         # random values from 1 to 20
v = np.random.randint(50, 680, size = 10)       # random values from 50 to 680

ksw = 35                                        # weight of the knapsack
print('The weight of knapsack is:', ksw)
print('The list of items generated')
print('Item     Weight      Worth')
for j in range(i.shape[0]):                     # displays the table of items
    print('{0}          {1}         {2}\n'.format(i[j], w[j], v[j]))

# Making the random population to start with
init_pop_size = 8                                               # determines total 8 parents to begin with
pop_size_init = (init_pop_size, i.shape[0])                     # the size of population
print('Population size = {}'.format(pop_size_init))             # prints the size of 2D list
initial_population = np.random.randint(2, size = pop_size_init)
initial_population = initial_population.astype(int)
num_generations = 50                                            # total number of generations
print('Initial population: \n{}'.format(initial_population))

print('\t\tFitness Function\n')
# Now using the fitness funtion
def Fitness(weight, worth, pop, threshold):
    fitness = np.empty(pop.shape[0])    # np.empty creates an empty list
    for i in range(pop.shape[0]):
        S1 = np.sum(pop[i] * worth)     # value * population given above
        S2 = np.sum(pop[i] * weight)    # weight * population given above
        if S2 <= threshold:             # checks if the value is less than equal to threshold that is ksw = 35
            fitness[i] = S1
        else:
            fitness[i] = 0              # if the fitness is computed
    return fitness.astype(int)

print('\t\tSelection of Parents\n')
# Function select from the parents we need to choose for crossover
def Selection(fitness, num_parents, pop):
    fitness = list(fitness)                             # empty list of fitness
    parents = np.empty((num_parents, pop.shape[1]))
    for i in range(num_parents):
        mfidx = np.where(fitness == np.max(fitness))    # most fit index
        parents[i,:] = pop[mfidx[0][0], :]
        fitness[mfidx[0][0]] = -1000000
    return parents

print('\t\tCrossover step\n')
def Crossover(parents, children):
    children = np.empty((children, parents.shape[1]))
    crosspoint1 = 3         # fist cross over at point 3
    crosspoint2 = 6         # second crossover at point 6
    crossover_rate = 0.8    # crossover rate is set to 0.8
    i = 0
    while (parents.shape[0] < children):
        parent1 = i % parents.shape[0]
        parent2 = (i + 1) % parents.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1 = i % parents.shape[0]
        parent2 = (i + 1) % parents.shape[0]
        children[i, 0:crosspoint1] = parents[parent1, 0:crosspoint1]        # crossover at point 3
        children[i, crosspoint1:] = parents[parent2, crosspoint1:]
        children[i, crosspoint1:crosspoint2] = parents[parent1, crosspoint1:crosspoint2]    # crossover at point 6
        children[i, crosspoint2:] = parents[parent2, crosspoint2:]
        i = i + 1
    return children

print('\t\tMutation Step\n')
def Mutation(children):
    mutation_rate = 0.3      # mutation rate set to 0.3
    mut = np.empty(children.shape)
    for i in range(mut.shape[0]):
        random_val = rd.random()
        mut[i,:] = children[i,:]
        if random_val > mutation_rate:
            continue

        int_random_val = rd.randint(0, children.shape[1]-1)

        if mut[i, int_random_val] == 1:
            mut[i, int_random_val] = 0
        elif mut[i, int_random_val] == 0:
            mut[i, int_random_val] = 1
    return mut

print('\t\tMain Function\n')
def mainfunc(weight, worth, pop, popsize, gen, threshold):
    fitness_his = []
    parameters = []
    num_parents = int(popsize[0] / 2)
    children = popsize[0] - num_parents
    for i in range(gen):
        fitness = Fitness(weight, worth, pop, threshold)        # check the fitness
        fitness_his.append(fitness)                             # append in fitness_his
        parents = Selection(fitness, num_parents, pop)          # Select among parents
        offsprings = Crossover(parents, children)               # Crossover karain
        mutants = Mutation(offsprings)                          # Mutation karain
        pop[0:parents.shape[0], :] = parents
        pop[parents.shape[0]:, :] = mutants

    print('Last generation: \n{}\n'.format(pop))
    fit_last_gen = Fitness(weight, worth, pop, threshold)
    print('Fitness of the last generation: \n{}\n'.format(fit_last_gen))
    most_fit = np.where(fit_last_gen == np.max(fit_last_gen))
    parameters.append(pop[most_fit[0][0], :])
    return parameters, fitness_his

# Main call ho jaye ga yahan par
# ksw = 35
para, fitness_history = mainfunc(w, v, initial_population, pop_size_init, num_generations, ksw)
print('The optimized parameters for the given inputs are: \n{}'.format(para))
chosen_item = para * i
print('\nItems chosen will be selected:')
for i in range(chosen_item.shape[1]):
  if chosen_item[0][i] != 0:
     print('{}\n'.format(chosen_item[0][i]))
