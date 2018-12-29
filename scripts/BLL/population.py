from chromosome import Chromosome


class Population:
    def __init__(self, size, target_chromosome):
        self._chromosomes = []
        self._population_size = size
        self._target_chromosome = target_chromosome

    def init_chromosomes(self):
        for i in xrange(self._population_size):
            self._chromosomes.append(Chromosome(self._target_chromosome))

    def sort_chromosomes(self):
        self._chromosomes = self._chromosomes.sort(key=lambda x: x.get_fitness(), reverse=True)

    def get_chromosomes(self):
        return self._chromosomes

    def get_fittest(self):
        max_fitness = 0
        max_fitness_index = 0
        for i in xrange(len(self._chromosomes)):
            if max_fitness <= self._chromosomes[i].get_fitness():
                max_fitness = self._chromosomes[i].get_fitness()
                max_fitness_index = i

        # fittest = self._chromosomes[max_fitness_index].get_fitness()
        return self._chromosomes[max_fitness_index]
