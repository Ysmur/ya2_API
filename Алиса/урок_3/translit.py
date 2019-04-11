import requests


def translit(text):
    # Собираем запрос для переводчика.
    translit_api_server = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    translit_params = {"lang": "ru-en",
                       "text": text,
                       "format": "plain",
                       "key": "trnsl.1.1.20190411T143351Z.3dd5c8c366016877.ea975ba0c69fba6a19ded96fe70e7e864c5d4952"}

    # Выполняем запрос.
    response = None
    try:
        response = requests.get(translit_api_server, params=translit_params)
        print(response)
        if response:
            # Преобразуем ответ в json-объект
            json_response = response.json()

            # Получаем первый топоним из ответа геокодера.
            # Согласно описанию ответа он находится по следующему пути:
            return json_response
        else:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
    except:
        print("Запрос не удалось выполнить. Проверьте подключение к сети Интернет.")

print(translit("привет, мир!"))