import requests
from geocode import geocode


def get_coordinate(address):
    """ координаты объекта по его адресу
    обращаемся к функции geocode из файла geocode.py"""
    toponym = geocode(address)
    if toponym:
        return toponym["Point"]["pos"]
    return None


# print(get_coordinate('Красная пл-дь, 1'))