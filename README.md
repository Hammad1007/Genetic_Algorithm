# Genetic_Algorithm

A thief enters a shop carrying bag which can carry 35 kgs of weight. The shop has 10 items, each
with a specific weight and price. Now, the thief’s dilemma is to make such a selection of items
that it maximizes the value (i.e., total price) without exceeding the knapsack weight. We have to
help the thief to make the selection.

Available Items are:

Item No. Weight Value
1 3 266
2 13 442
3 10 671
4 9 526
5 7 388
6 1 245
7 8 210
8 8 145
9 2 126
10 9 322

Initial population:

[[0 1 0 1 1 0 0 1 1 1]
[1 1 1 1 0 1 1 1 0 0]
[0 1 0 0 0 0 1 1 0 1]
[0 0 1 0 1 1 0 0 0 0]
[0 0 1 1 0 0 0 0 0 1]
[0 1 0 1 1 0 1 0 0 0]
[1 1 1 0 0 0 1 0 1 0]
[0 0 0 0 1 1 1 0 0 0]]

Fitness Function:
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
