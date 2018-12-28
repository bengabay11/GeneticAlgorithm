from chromosome import Chromosome


class Population:
    def __init__(self, size, target_chromosome):
        self._chromosomes = []
        self._population_size = size
        self.init_chromosomes(target_chromosome)

    def init_chromosomes(self, target_chromosome):
        for i in xrange(self._population_size):
            self._chromosomes.append(Chromosome(target_chromosome))

    def sort_chromosomes(self):
        self._chromosomes.sort(key= lambda x: x.get_fitness(), reverse=True)