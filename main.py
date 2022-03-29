import urllib.request
import json
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
req = urllib.request.Request(url)

r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
record = 0
earthquakes = []

class Earthquake:

    mag = ''
    place = ''

    def __init__(self, mag, place):
        self.mag = mag
        self.place = place

for item in cont['features']:
    quake = Earthquake(mag=item['properties']['mag'], place=item['properties']['place'])
    earthquakes.append({'mag':quake.mag, 'place':quake.place})
    record+=1

with open('earthquakeData.json', 'w+') as outfile:
    json.dump(earthquakes, outfile, indent=4)

print('Records found: ', record)