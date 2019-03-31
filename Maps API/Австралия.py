import requests
from coordinate import get_coordinate
from static_map_in_pygame import show_map

address = input()
# обращаемся к функции geocode из файла geocode.py
toponym_coords = get_coordinate(address)
# обращаемся к функции show_map из файла static_map_in_pygame.py
show_map(toponym_coords, delta='20', map_type='sat')

