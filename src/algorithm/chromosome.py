import random
import string


class Chromosome:
    def __init__(self, target_chromosome):
        self._genes = []
        self._target_chromosome = target_chromosome

    @property
    def genes(self):
        if not self._genes:
            self._init_genes()

        return self._genes

    @genes.setter
    def genes(self, new_genes):
        self._genes = new_genes

    def _init_genes(self):
        for i in range(len(self._target_chromosome)):
            self._genes.append(random.choice(string.ascii_letters + " ."))

    def get_fitness(self):
        fitness = 0
        for i in range(len(self._genes)):
            if self.genes[i] == self._target_chromosome[i]:
                fitness += 1

        return fitness

