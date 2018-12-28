import random

import configuration


class Chromosome:
    def __init__(self, target_chromosome):
        self._genes = []
        self._target_chromosome = target_chromosome
        self.init_genes()

    def init_genes(self):
        for i in xrange(len(self._target_chromosome)):
            self._genes.append(random.randint(configuration.MIN_GENE_NUMBER, configuration.MAX_GENE_NUMBER))

    def get_fitness(self):
        fitness = 0
        for i in xrange(len(self._genes)):
            if self._genes[i] == self._target_chromosome[i]:
                fitness += 1

        return fitness

    def get_genes(self):
        return self._genes
