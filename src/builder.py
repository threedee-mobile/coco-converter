from models import Column
from models import XCo2
from models import Place
from uuid import uuid4
import json

def id():
	return uuid4()

def generatePlace(city, region, country, lon, lat, primaryColumn, neighbouringColumns):
	place = Place(id(), city, region, country, lon, lat, primaryColumn, neighbouringColumns)
	# print(place.toJson())
	return place

def generateJson(placesArray):
	placesJson = json.dumps(placesArray, default=lambda o: o.__dict__, sort_keys=True, indent=2)
	file = open("../assets/output.json", "w")
	file.write(placesJson)
	file.close()

def main():
	# RUN FROM COMMAND LINE: python -c 'from builder import *; main()'
	monthly_xco2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
	monthly_uncertainty = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
	xco2 = XCo2(monthly_xco2, monthly_uncertainty)
	column = Column(id(), 43.65, -79.38, xco2)
	neighbouringColumns = [column, column]
	place = generatePlace("Toronto", "Ontario", "CA", 43.65, -79.38, column, neighbouringColumns)

	generateJson([place])