import requests
from geocode import geocode

address = input()
# обращаемся к функции geocode из файла geocode.py
toponym = geocode(address)

# Полный адрес топонима:
toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
print(toponym_address, "имеет координаты:", toponym_coodrinates)
