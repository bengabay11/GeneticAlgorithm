from PIL import Image
from scripts import config
from scripts.BLL.population import Population


def get_image_values():
    im = Image.open(config.IMAGE_PATH, config.OPEN_FILE_MODE)
    pixels = list(im.getdata())
    pixels_list = []
    for pixel in pixels:
        for value in pixel:
            pixels_list.append(value)

    return pixels_list


def image_values_to_pixels(pixels_list):
    pixels = []
    index = 0
    while index <= len(pixels_list) - 3:
        pixels.append((pixels_list[index], pixels_list[index + 1], pixels_list[index + 2]))
        index += 3

    return pixels


def show_image(pixels):
    image = Image.new(config.COLOR_MODEL, config.IMAGE_SIZE)
    image.putdata(pixels)
    image.show()


def start_algorithm():
    target_chromosome = get_image_values()
    population = Population(config.POPULATION_SIZE, target_chromosome)
    population.sort_chromosomes()
