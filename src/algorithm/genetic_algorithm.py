import random
from src import config
import string
from src.algorithm.population import Population


class GeneticAlgorithm:
    def __init__(self, target_chromosome, population_size):
        self._target_chromosome = target_chromosome
        self._population = Population(population_size, self._target_chromosome)

    def start_algorithm(self):
        best_fitness = 0
        generation_count = 0
        best_chromosome = None
        while best_fitness < len(self._target_chromosome):
            # self.print_generation(generation_count)
            self.selection()
            self.crossover()
            self.mutation()

            self._population.sort_chromosomes()
            best_chromosome = self._population.chromosomes[0]
            best_fitness = best_chromosome.get_fitness()
            generation_count += 1
            self.print_current_generation(best_chromosome, best_fitness, generation_count)

        return best_chromosome

    def selection(self):
        generation = self._population.chromosomes
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
        generation = self._population.chromosomes
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
        for chromosome in self._population.chromosomes:
            if random.random() < config.MUTATION_PROBABILITY:
                index = random.randint(0, len(chromosome.genes) - 1)
                new_value = random.choice(string.ascii_letters)
                chromosome.genes[index] = new_value

    def print_current_generation(self, best_chromosome, best_fitness, generation_count):
        best_chromosome_string = "".join(best_chromosome.genes)
        print("Best Chromosome: {}".format(best_chromosome_string), end="\r")
        print("Fitness: {}".format(str(best_fitness)), end="\r")
        print("Generation: {}".format(str(generation_count)), end="\r")
