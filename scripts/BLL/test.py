import random

list1 = [32, 60, 71, 4, 0, 7, 34]
sum_fitness = 0
index = 0
fitness_dict = {}
for current_fitness in list1:
    sum_fitness += current_fitness
    fitness_dict[index] = sum_fitness
    index += 1

random_number = random.randint(1, sum_fitness)
print random_number
chosen_chromosome = 0
for x in fitness_dict.keys():
    if random_number < fitness_dict[x]:
        chosen_chromosome = x
        break

print fitness_dict
print list1[chosen_chromosome]
