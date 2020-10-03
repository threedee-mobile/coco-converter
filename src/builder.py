from models import Column
from models import XCO2
from models import Place
import json
import uuid

def id() -> str:
	return str(uuid.uuid1())

def generatePlace(city: str, region: str, country: str, lon: float, lat: float, monthly, neighbouringColumns) -> Place:
	place = Place(id(), city, region, country, lon, lat, monthly, neighbouringColumns)
	# print(place.toJson())
	return place

def generateJson(*placesArray: Place):
	placesJson = json.dumps(placesArray, default=lambda o: o.__dict__, sort_keys=False, indent=2)
	file = open("../assets/output.json", "w")
	file.write(placesJson)
	file.close()
	print("DONE")

def main():
	# RUN FROM COMMAND LINE: python -c 'from builder import *; main()'
	xco2 = XCO2(350, 5)
	monthly = [xco2, xco2, xco2, xco2, xco2, xco2, xco2, xco2, xco2, xco2, xco2, xco2]
	column = Column(id(), 43.65, -79.38, xco2)
	neighbouringColumns = [column, column]

	place = generatePlace("toronto", "ontario", "ca", 43.65, -79.38, monthly, neighbouringColumns)

	generateJson([place])
