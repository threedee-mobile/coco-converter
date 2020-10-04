from enum import Enum
import json

class Model:
	def toJson(self) -> str:
		 return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=2)

		
'''
Represents a "cell" defined in the ODIAC data set
@param id       Random UUID
@param lat      The longitude at the center of the cell
@param lon      The latitude at the center of the cell
@param ff_co2   CO2 emissions value from fossil fuel combustion, cement production and gas flaring
@param ib_co2   CO2 emissions value from international aviation and marine bunker, plus antarctic fishery
'''
class Cell(Model):
	def __init__(self, cellId: str, lat: float, lon: float, ff_co2: float, ib_co2):
		self.id = cellId
		self.lat = lat
		self.lon = lon
		self.ff_co2 = ff_co2
		self.ib_co2 = ib_co2

class Month(str, Enum):
        JAN = "january"
        FEB = "february"
        MAR = "march"
        APR = "april"
        MAY = "may"
        JUN = "june"
        JUL = "july"
        AUG = "august"
        SEP = "september"
        OCT = "october"
        NOV = "november"
        DEC = "december"

monthArray = [
        Month.JAN,
        Month.FEB,
        Month.MAR,
        Month.APR,
        Month.MAY,
        Month.JUN,
        Month.JUL,
        Month.AUG,
        Month.SEP,
        Month.OCT,
        Month.NOV,
        Month.DEC
]

'''
@param month    The Month corresponding to the Cells
@param cells    Array of Cells from the data occurring in the given Month
'''
class MonthData(Model):
        def __init__(self, month: Month, cells):
                self.month = month
                self.monthIndex = monthArray.index(month)
                self.cells = cells

'''
@param year         The year corresponding to the MonthData
@param monthlyData  Array of MonthData from the data occurring in the given year
'''
class YearData(Model):
	def __init__(self, year: int, monthlyData):
		self.year = year
		self.monthlyData = monthlyData
