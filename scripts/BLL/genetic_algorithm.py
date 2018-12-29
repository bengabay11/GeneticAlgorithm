import random
from scripts import configuration
from scripts.BLL.population import Population


def start(target_chromosome):
    best_fitness = 0
    generation_count = 0
    population = Population(configuration.POPULATION_SIZE, target_chromosome)
    population.init_chromosomes()
    print "Starting Algorithm..."
    while best_fitness < len(target_chromosome):
        print_generation(population, generation_count)

        current_generation = population.chromosomes

        parents = selection(current_generation)

        new_generation = crossover(parents)

        for i in xrange(len(new_generation)):
            new_generation[i] = mutation(new_generation[i])

        population.chromosomes = new_generation

        best_chromosome = population.get_fittest()
        best_fitness = best_chromosome.get_fitness()
        generation_count += 1

    print "Best Fitness: " + str(best_fitness)


def print_generation(population, generation_count):
    print "Generation: " + str(generation_count)
    print "Current Fitness: " + str(population.get_fittest().get_fitness())


def selection(generation):
    parents = []
    sum_fitness = 0
    fitness_dict = {}
    for i in xrange(len(generation)):
        sum_fitness += generation[i].get_fitness()
        fitness_dict[i] = sum_fitness

    while len(parents) < len(generation):
        random_number = random.randint(1, sum_fitness)
        chosen_chromosome_index = 0
        for x in fitness_dict.keys():
            if random_number < fitness_dict[x]:
                chosen_chromosome_index = x
                break

        parents.append(generation[chosen_chromosome_index])

    return parents


def crossover(parents):
    index = 0
    new_generation = []
    while index < len(parents):
        if index + 1 < len(parents):
            offspring1, offspring2 = create_offsprings(parents[index], parents[index + 1])
            new_generation.append(offspring1)
            new_generation.append(offspring2)
            index += 2
        else:
            index += 1

    return new_generation


def create_offsprings(father_chromosome, mother_chromosome):
    if random.random() < configuration.CROSSOVER_PROBABILITY:
        crossover_point = random.randint(0, len(father_chromosome.genes))
        for i in xrange(crossover_point):
            temp = father_chromosome.genes[i]
            father_chromosome.genes[i] = mother_chromosome.genes[i]
            mother_chromosome.genes[i] = temp

    return father_chromosome, mother_chromosome
    

def mutation(chromosome):
    if random.random < configuration.MUTATION_PROBABILITY:
        index = random.randint(0, len(chromosome.get_genes()) - 1)
        new_value = random.randint(configuration.MIN_GENE_NUMBER, configuration.MAX_GENE_NUMBER)
        updated_genes = chromosome.genes
        updated_genes[index] = new_value
        chromosome.genes = updated_genes

    return chromosome
