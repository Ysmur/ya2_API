from bolder import bolder
from coordinate import get_coordinate
from static_map_in_pygame import show_map

import sys


def main():
    toponym_to_find = " ".join(sys.argv[1:])

    if toponym_to_find:
        # Показываем карту с фиксированным масштабом.
        show_map(get_coordinate(toponym_to_find), delta='15', map_type='map')

        # Показываем карту с масштабом, подобранным по заданному объекту.
        show_map(get_coordinate(toponym_to_find), bolder(toponym_to_find), map_type='map')

        # Добавляем исходную точку на карту.
        show_map(get_coordinate(toponym_to_find), str(bolder(toponym_to_find)), map_type='map', pt=True)
    else:
        print('No data')


if __name__ == "__main__":
    main()
