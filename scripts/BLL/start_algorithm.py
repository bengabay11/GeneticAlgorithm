import config
from scripts.BLL.population import Population


def start_algorithm():
    target_chromosome = get_image_values()
    population = Population(config.POPULATION_SIZE, target_chromosome)
    population.sort_chromosomes()
