import pygame
import requests
import sys
import os


class MapParams(object):
    # Параметры по умолчанию.
    def __init__(self):
        self.lat = 55.729738  # Координаты центра карты на старте.
        self.lon = 37.664777
        self.zoom = 0.005  # Масштаб карты на старте.
        self.type = "map"  # Тип карты на старте.


    # Обновление параметров карты по нажатой клавише.
    def update(self, event):
        pass

# Создание карты с соответствующими параметрами.
def load_map(mp):
    # Собираем запрос для статик карт.
    map_api_server = "http://static-maps.yandex.ru/1.x/"

    toponym_longitude = str(mp.lon)
    toponym_lattitude = str(mp.lat)

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(mp.zoom), str(mp.zoom)]),
        "l": mp.type,
    }
    response = requests.get(map_api_server, params=map_params)


    if not response:
        print("Ошибка выполнения запроса:")
        print(map_api_server, params=map_params)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

    return map_file


def main():
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    # Заводим объект, в котором будем хранить все параметры отрисовки карты.
    mp = MapParams()


    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:  # Выход из программы
            break
        elif event.type == pygame.KEYUP:  # Обрабатываем различные нажатые клавиши.
            mp.update(event)
        else:
            continue

        # Загружаем карту, используя текущие параметры.
        map_file = load_map(mp)

        # Рисуем картинку, загружаемую из только что созданного файла.
        screen.blit(pygame.image.load(map_file), (0, 0))


        # Переключаем экран и ждем закрытия окна.
        pygame.display.flip()

    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_file)


if __name__ == "__main__":
    main()
