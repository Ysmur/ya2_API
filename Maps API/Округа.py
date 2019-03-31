import requests
from geocode import geocode

address = input()
# обращаемся к функции geocode из файла geocode.py
toponym = geocode(address)

# Детали адреса топонима:
toponym_address_details = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
print(address, 'входит в', toponym_address_details[1]["name"])

