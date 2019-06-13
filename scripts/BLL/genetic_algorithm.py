import random
import config
from scripts.BLL.population import Population
import string


class GeneticAlgorithm:
    def __init__(self, target_chromosome):
        self._target_chromosome = target_chromosome
        self._population = Population(config.POPULATION_SIZE, self._target_chromosome)
        self._population.init_chromosomes()

    def start_algorithm(self):
        best_fitness = 0
        generation_count = 0
        while best_fitness < len(self._target_chromosome):
            # self.print_generation(generation_count)

            self.selection()
            self.crossover()
            self.mutation()

            self._population.sort_chromosomes()
            best_chromosome = self._population.get_chromosomes()[0]
            best_fitness = best_chromosome.get_fitness()
            generation_count += 1
            print("Best Fitness: " + str(best_fitness))
            print("Best Chromosome: " + str(best_chromosome.genes))

        print("Best Fitness: " + str(best_fitness))
        print("Best Chromosome: " + str(best_chromosome.genes))

    def selection(self):
        generation = self._population.get_chromosomes()
        potential_parents = generation
        generation = []
        sum_fitness = 0
        fitness_dict = {}
        for i in range(len(potential_parents)):
            sum_fitness += potential_parents[i].get_fitness()
            fitness_dict[i] = sum_fitness

        while len(generation) < len(potential_parents):
            random_number = random.randint(1, sum_fitness)
            chosen_chromosome_index = 0
            for x in list(fitness_dict.keys()):
                if random_number <= fitness_dict[x]:
                    chosen_chromosome_index = x
                    break

            generation.append(potential_parents[chosen_chromosome_index])

    def crossover(self):
        generation = self._population.get_chromosomes()
        index = 0
        while index + 1 < len(generation):
            father_chromosome, mother_chromosome = generation[index], generation[index + 1]
            if random.random() < config.CROSSOVER_PROBABILITY:
                crossover_point = random.randint(1, len(father_chromosome.genes))
                for i in range(crossover_point):
                    temp = father_chromosome.genes[i]
                    father_chromosome.genes[i] = mother_chromosome.genes[i]
                    mother_chromosome.genes[i] = temp
            index += 2

    def mutation(self):
        for chromosome in self._population.get_chromosomes():
            if random.random() < config.MUTATION_PROBABILITY:
                index = random.randint(0, len(chromosome.genes) - 1)
                new_value = random.choice(string.ascii_letters)
                chromosome.genes[index] = new_value

    def print_generation(self, generation_count):
        print("-------------------------------------------")
        print("Generation: " + str(generation_count))
        print("Best chromosome: " + str(self._population.get_chromosomes()[0].genes) + \
              ", " + str(self._population.get_chromosomes()[0].get_fitness()))
