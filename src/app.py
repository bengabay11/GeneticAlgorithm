from src import config
from src.algorithm.genetic_algorithm import GeneticAlgorithm
from src.algorithm.population import Population


def main():
    target = config.PHRASE
    genetic_algorithm = GeneticAlgorithm(target, config.POPULATION_SIZE)
    genetic_algorithm.start_algorithm()


if __name__ == '__main__':
    main()
