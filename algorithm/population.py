from .chromosome import Chromosome


class Population:
    def __init__(self, size, target_chromosome):
        self._population_size = size
        self._target_chromosome = target_chromosome
        self._chromosomes = self._init_chromosomes()

    @property
    def population_size(self):
        return self._population_size

    @population_size.setter
    def population_size(self, new_population_size):
        self._population_size = new_population_size

    @property
    def chromosomes(self):
        return self._chromosomes

    @chromosomes.setter
    def chromosomes(self, new_chromosomes):
        self._chromosomes = new_chromosomes

    @property
    def target_chromosome(self):
        return self._target_chromosome

    @target_chromosome.setter
    def target_chromosome(self, new_target_chromosome):
        self._target_chromosome = new_target_chromosome

    def _init_chromosomes(self):
        chromosomes = []
        for i in range(self._population_size):
            new_chromosome = Chromosome(self._target_chromosome)
            chromosomes.append(new_chromosome)

        return chromosomes

    def sort_chromosomes(self):
        self._chromosomes.sort(key=lambda x: x.get_fitness(), reverse=True)

