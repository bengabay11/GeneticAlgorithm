import random
import string


class Chromosome:
    def __init__(self, target_chromosome):
        self.genes = []
        self._target_chromosome = target_chromosome

    def init_genes(self):
        for i in range(len(self._target_chromosome)):
            self.genes.append(random.choice(string.ascii_letters + " ."))

    def get_fitness(self):
        fitness = 0
        for i in range(len(self.genes)):
            if self.genes[i] == self._target_chromosome[i]:
                fitness += 1

        return fitness
