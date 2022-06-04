# Genetic_Algorithm

A thief enters a shop carrying bag which can carry 35 kgs of weight. The shop has 10 items, each
with a specific weight and price. Now, the thief’s dilemma is to make such a selection of items
that it maximizes the value (i.e., total price) without exceeding the knapsack weight. We have to
help the thief to make the selection.

Available Items are:

![image](https://user-images.githubusercontent.com/76726810/172024147-b0317da4-e98e-442b-8eb1-7c3484a3a35e.png)


Initial population:

![image](https://user-images.githubusercontent.com/76726810/172024160-3001a006-ccb5-4e7d-b10f-f88f133fec30.png)


![image](https://user-images.githubusercontent.com/76726810/172024122-1fd025e4-3c4b-4333-be0a-1b0eef49a0b0.png)

where,
n = chromosome length
Ci = ith gene
Vi = ith value
Wi = ith weight
kw = allowed weight

To generate new population:
1- Two-point crossover
Example of two-point cross-over. Choose the positions as in the example.

2- Mutate offspring got from cross over at 2 random positions. Select 2 random
positions: if you find 1change it to 0 and vice versa.

Always keep 8 best chromosomes, 50% from initial population and 50% from new generation. If
your program taking time you can iterate for fixed number of iterations.
