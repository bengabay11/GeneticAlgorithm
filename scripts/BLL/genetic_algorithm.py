import random
from scripts import configuration
from scripts.BLL.population import Population


def start(target_chromosome):
    best_fitness = 0
    population = Population(configuration.POPULATION_SIZE, target_chromosome)
    population.init_chromosomes()
    while best_fitness < len(target_chromosome):
        parents = selection(population)
        crossover(parents)
        for chromosome in population.get_chromosomes():
            mutation(chromosome)


def selection(population):
    parents = []
    sum_fitness = 0
    fitness_dict = {}
    for i in xrange(len(population.get_chromosomes())):

        sum_fitness += population.get_chromosomes()[i].get_fitness()
        fitness_dict[i] = sum_fitness

    while len(parents) < len(population.get_chromosomes):
        random_number = random.randint(1, sum_fitness)
        chosen_chromosome_index = 0
        for x in fitness_dict.keys():
            if random_number < fitness_dict[x]:
                chosen_chromosome_index = x
                break

        parents.append(population.get_chromosomes()[chosen_chromosome_index])

    return parents


def crossover(parents):
    index = 0
    while index < len(parents):
        if index + 1 < len(parents):
            create_offsprings(parents[index], parents[index + 1])
            index += 2
        else:
            index += 1


def create_offsprings(father_chromosome, mother_chromosome):
    if random.random < configuration.CROSSOVER_PROBABILITY:
        crossover_point = random.randint(0, len(father_chromosome.get_genes()))
        for i in xrange(crossover_point):
            temp = father_chromosome.get_genes()[i]
            father_chromosome.get_genes()[i] = mother_chromosome.get_genes()[i]
            mother_chromosome.get_genes()[i] = temp


def mutation(chromosome):
    if random.random < configuration.MUTATION_PROBABILITY:
        index = random.randint(0, len(chromosome.get_genes()) - 1)
        new_value = random.randint(configuration.MIN_GENE_NUMBER, configuration.MAX_GENE_NUMBER)
        mutated_chromosome = list(chromosome)
        mutated_chromosome[index] = new_value