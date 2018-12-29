import random

from scripts import configuration


class Chromosome:
    def __init__(self, target_chromosome):
        self.genes = []
        self._target_chromosome = target_chromosome

    def init_genes(self):
        for i in xrange(len(self._target_chromosome)):
            self.genes.append(random.randint(configuration.MIN_GENE_NUMBER, configuration.MAX_GENE_NUMBER))

    def get_fitness(self):
        fitness = 0
        for i in xrange(len(self.genes)):
            if self.genes[i] == self._target_chromosome[i]:
                fitness += 1

        return fitness
