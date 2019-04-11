import requests
import math


def get_geo_info(city_name, type_info):
    try:
        # url, по которому доступно API Яндекс.Карт
        url = "https://geocode-maps.yandex.ru/1.x/"
        # параметры запроса
        params = {
            # город, координаты которого мы ищем
            'geocode': city_name,
            # формат ответа от сервера, в данном случае JSON
            'format': 'json'
        }
        # отправляем запрос
        response = requests.get(url, params)
        # получаем JSON ответа
        json = response.json()
        # получаем первый топоним.
        toponym = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']

        # получает географические координаты города по его имени
        if type_info == "coordinates":
            coordinates_str = toponym['Point']['pos']
            # Превращаем string в список, так как точка - это пара двух чисел - координат
            long, lat = map(float, coordinates_str.split())
            # Вернем ответ
            return long, lat

        # вернёт страну, в которой находится указанный город
        elif type_info == "country":
            return toponym['metaDataProperty']['GeocoderMetaData']['AddressDetails'][
                'Country']['CountryName']

    except Exception as e:
        return e


# вычисление расстояний между двумя точками
def get_distance(p1, p2):
    # p1 и p2 - это кортежи из двух элементов - координаты точек
    radius = 6373.0

    lon1 = math.radians(p1[0])
    lat1 = math.radians(p1[1])
    lon2 = math.radians(p2[0])
    lat2 = math.radians(p2[1])

    d_lon = lon2 - lon1
    d_lat = lat2 - lat1

    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(a ** 0.5, (1 - a) ** 0.5)

    distance = radius * c
    return distance