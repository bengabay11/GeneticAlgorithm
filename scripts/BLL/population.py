from chromosome import Chromosome


class Population:
    def __init__(self, size, target_chromosome):
        self._population_size = size
        self._target_chromosome = target_chromosome
        self.chromosomes = []

    def init_chromosomes(self):
        for i in xrange(self._population_size):
            new_chromosome = Chromosome(self._target_chromosome)
            new_chromosome.init_genes()
            self.chromosomes.append(new_chromosome)

    def sort_chromosomes(self):
        self.chromosomes = self.chromosomes.sort(key=lambda x: x.get_fitness(), reverse=True)

    def get_chromosomes(self):
        return self.chromosomes

    def get_fittest(self):
        max_fitness = 0
        max_fitness_index = 0
        for i in xrange(len(self.chromosomes)):
            if max_fitness <= self.chromosomes[i].get_fitness():
                max_fitness = self.chromosomes[i].get_fitness()
                max_fitness_index = i

        # fittest = self._chromosomes[max_fitness_index].get_fitness()
        return self.chromosomes[max_fitness_index]
