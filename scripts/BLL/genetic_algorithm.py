import random

from scripts import configuration


def start(target_chromosome):
    best_fitness = 0
    while best_fitness < len(target_chromosome):
        pass


def selection(population):
    parents = population.sort_chromosomes()[    ]


def crossover(father_chromosome, mother_chromosome):
    crossover_point = random.randint(0, len(father_chromosome.get_genes()))
    for i in xrange(crossover_point):
        temp = father_chromosome.get_genes()[i]
        father_chromosome.get_genes()[i] = mother_chromosome.get_genes()[i]
        mother_chromosome.get_genes()[i] = temp


def mutate(chromosome):
    index = random.randint(0, len(chromosome.get_genes()) - 1)
    new_value = random.randint(configuration.MIN_GENE_NUMBER, configuration.MAX_GENE_NUMBER)
    mutated_chromosome = list(chromosome)
    mutated_chromosome[index] = new_value
    return mutated_chromosome
