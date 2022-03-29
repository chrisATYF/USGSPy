import urllib.request
import json

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
url_request = urllib.request.Request(url)

url_fetch = urllib.request.urlopen(url_request).read()
raw_data = json.loads(url_fetch.decode('utf-8'))
earthquakes = []

records_amount = 0
for features in raw_data['features']:
    earthquakes.append({'mag':features['properties']['mag'], 'place':features['properties']['place']})
    records_amount+=1

with open('earthquakeData.json', 'w+') as outfile:
    json.dump(earthquakes, outfile, indent=4)

print('Records found: ', records_amount)