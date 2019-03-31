import requests
from geocode import geocode

address = input()
# обращаемся к функции geocode из файла geocode.py
toponym = geocode(address)

# Детали адреса топонима:
toponym_postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
print(address, 'почтовый индекс -', toponym_postal_code)
