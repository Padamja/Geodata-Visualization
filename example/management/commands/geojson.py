from django.core.management.base import BaseCommand, CommandError
import csv,json


class Command(BaseCommand):
	help = 'Convert Data in CSV in GeoJSON'

	def handle(self, *args, **options):  
		csv_reader =  csv.reader(open('Earthquakes_7day.csv','r'))
		geo_data = {
			"type" : "FeatureCollection",
			"features" : []
		}
		next(csv_reader)
		for row in csv_reader:
			latitude = float(row[4])
			longitude = float(row[5])
			magnitude  = float(row[6])
			coordinates = [latitude,longitude]
			geo_json_feature = {
				"type" : "Feature",
				"geometry" : {
					"type":"Point",
					"coordinates" : coordinates
				},
				"properties":{
					"magnitude" : magnitude,
					"region" : row[9]
				}
			}
			geo_data['features'].append(geo_json_feature)
		with open('geo_data.json', 'w') as f:
			f.write(json.dumps(geo_data, indent=4))