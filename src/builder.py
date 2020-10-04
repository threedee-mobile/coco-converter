from models import Cell
from models import Month
from models import MonthData
from models import YearData
import json
import uuid

def id() -> str:
	return str(uuid.uuid4())

def generateCell(lon: float, lat: float, ff_co2: float, ib_co2: float) -> Cell:
	cell = Cell(id(), lon, lat, ff_co2, ib_co2)
	# print(place.toJson())
	return cell

def generateJson(yearData: YearData):
	resultJson = json.dumps(yearData, default=lambda o: o.__dict__, sort_keys=False, indent=2)
	file = open("../assets/output.json", "w")
	file.write(resultJson)
	file.close()
	print("DONE")

def main():
	# RUN FROM COMMAND LINE: python -c 'from builder import *; main()'
	c1 = generateCell(43.65, -79.38, 2.89, 1.98)
	c2 = generateCell(41.65, -77.38, 2.99, 1.25)
	monthData1 = MonthData(Month.JAN, [c1, c2])
	monthData2 = MonthData(Month.FEB, [c1, c2])
	yearData = YearData(2019, [monthData1, monthData2])
	
	generateJson(yearData)
