from models import Cell
from models import Month
from models import MonthData
from models import YearData
from models import Data
import json
import uuid

def id() -> str:
	return str(uuid.uuid4())

def generateCell(lon: float, lat: float, ff_co2: float, ib_co2: float) -> Cell:
	cell = Cell(id(), lon, lat, ff_co2, ib_co2)
	# print(place.toJson())
	return cell

def generateJson(data: Data):
	resultJson = json.dumps(data, default=lambda o: o.__dict__, sort_keys=False, indent=2)
	file = open("../assets/output.json", "w")
	file.write(resultJson)
	file.close()
	print("DONE")

def main():
	# Sample data generation
	c1 = generateCell(43.1, -79.3, 2.8, 1.9)
	c2 = generateCell(41.6, -77.5, 2.9, 1.25)
	monthData1 = MonthData(Month.JAN, [c1, c2])

	c3 = generateCell(42.1, -78.3, 2.7, 1.8)
	c4 = generateCell(41.65, -77.22, 3.9, 1.9)
	monthData2 = MonthData(Month.FEB, [c3, c4])
	
	yearData1 = YearData(2018, [monthData1, monthData2])

	c5 = generateCell(42.3, -79.1, 2.85, 1.9)
	c6 = generateCell(42.6, -77.2, 2.29, 1.25)
	monthData3 = MonthData(Month.JAN, [c5, c6])

	c7 = generateCell(44.1, -78.05, 2.4, 1.58)
	c8 = generateCell(45.65, -77.12, 3.14, 12.0)
	monthData4 = MonthData(Month.FEB, [c7, c8])
	
	yearData2 = YearData(2019, [monthData3, monthData4])
	
	generateJson(Data([yearData1, yearData2]))
