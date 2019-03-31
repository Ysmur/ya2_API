import requests
import sys
import pygame
import os


def show_map(lon_lat=None, delta=0.005, map_type='map'):
    """ Статическая картинка в PyGame по координатам """
    # Собираем запрос для статик карт.
    map_api_server = "http://static-maps.yandex.ru/1.x/"

    toponym_longitude, toponym_lattitude = lon_lat.split(" ")
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta, delta]),
        "l": map_type
    }

    # Выполняем запрос.
    response = None
    try:
        response = requests.get(map_api_server, params=map_params)
        if response:
            # Запишем полученное изображение в файл.
            map_file = "map.png"
            try:
                with open(map_file, "wb") as file:
                    file.write(response.content)
            except IOError as ex:
                print("Ошибка записи временного файла:", ex)
                sys.exit(2)

            # Инициализируем pygame
            pygame.init()
            screen = pygame.display.set_mode((600, 450))
            # Рисуем картинку, загружаемую из только что созданного файла.
            screen.blit(pygame.image.load(map_file), (0, 0))
            # Переключаем экран и ждем закрытия окна.
            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            pygame.quit()

            # Удаляем за собой файл с изображением.
            os.remove(map_file)

        else:
            print("Ошибка выполнения запроса:")
            print(map_api_server, params=map_params)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
    except:
        print("Запрос не удалось выполнить. Проверьте подключение к сети Интернет.")
        sys.exit(1)
