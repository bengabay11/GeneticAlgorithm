import time

from src import config
from src.algorithm.genetic_algorithm import GeneticAlgorithm


def main():
    try:
        start_time = time.time()
        target = config.PHRASE
        genetic_algorithm = GeneticAlgorithm(target, config.POPULATION_SIZE)
        best_chromosome = genetic_algorithm.start_algorithm()
        if best_chromosome:
            end_time = time.time()
            final_time = end_time - start_time
            print("\nFound the best chromosome in {} seconds.".format(final_time))
            print(best_chromosome)
        else:
            print("Can't find the target chromosome.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
