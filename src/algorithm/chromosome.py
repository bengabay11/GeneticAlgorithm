import random
import string


class Chromosome:
    def __init__(self, target_chromosome):
        self._target_chromosome = target_chromosome
        self._genes = self._init_genes()

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, new_genes):
        self._genes = new_genes

    @property
    def target_chromosome(self):
        return self._target_chromosome

    @target_chromosome.setter
    def target_chromosome(self, new_target_chromosome):
        self._target_chromosome = new_target_chromosome

    def _init_genes(self):
        genes = []
        for i in range(len(self._target_chromosome)):
            genes.append(random.choice(string.ascii_letters + " ."))

        return genes

    def get_fitness(self):
        fitness = 0
        for i in range(len(self._genes)):
            if self._genes[i] == self._target_chromosome[i]:
                fitness += 1

        return fitness

