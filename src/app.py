from PIL import Image
from src import config
from src.algorithm.genetic_algorithm import GeneticAlgorithm


def get_image_values():
    im = Image.open(config.IMAGE_PATH, config.OPEN_FILE_MODE)
    pixels = list(im.getdata())
    pixels_list = []
    for pixel in pixels:
        for value in pixel:
            pixels_list.append(value)

    return pixels_list


def main():
    genetic_algorithm = GeneticAlgorithm(config.PHRASE)
    genetic_algorithm.start_algorithm()


if __name__ == '__main__':
    main()
