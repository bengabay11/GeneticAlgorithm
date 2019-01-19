import random

from scripts.BLL.chromosome import Chromosome
from scripts.BLL.genetic_algorithm import crossover, create_offsprings, selection, calc_fit, mutation
from scripts.main import generate_random_target_chromosome

t = generate_random_target_chromosome(200)

list1 = []
for i in xrange(1000):
    c1 = Chromosome(t)
    c1.init_genes()
    list1.append(c1)

parents = selection(list1)
print "Selection effect: " + str(calc_fit(parents) - calc_fit(list1))

new_generation = crossover(parents)
print "crossover effect: " + str(calc_fit(new_generation) - calc_fit(parents))

copy = new_generation
for i in xrange(len(new_generation)):
    new_generation[i] = mutation(new_generation[i])

print "mutate effect: " + str(calc_fit(new_generation) - calc_fit(copy))
