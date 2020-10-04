from models import Cell
from models import Month
from models import MonthData
from models import YearData
from models import Data
import json
import uuid
import numpy as np
import netCDF4 as nc
import os

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
        monthList = [Month.JAN, Month.FEB, Month.MAR, Month.APR, Month.MAY, Month.JUN, Month.JUL, Month.AUG, Month.SEP, Month.OCT, Month.NOV, Month.DEC]
        yearArray = []
        
        for year in [2018]:
                print(year)
                ds = nc.Dataset("../../DATA/odiac2019_1x1d_" + str(year) + ".nc")
                lonList, latList, ffList, ibList = ds['lon'][:], ds['lat'][:], ds['land'][:], ds['intl_bunker'][:]
                monthArray = []

                for month in np.arange(12):
                        print(monthList[month])
                        cellArray = []

                        for i in range(len(latList)):
                                for j in range(len(lonList)):
                                        lon, lat = lonList[j], latList[i]
                                        ff_co2, ib_co2 = ffList[month, i, j], ibList[month, i, j]
                                        c = generateCell(float(lon), float(lat), float(ff_co2), float(ib_co2))
                                        cellArray.append(c)

                        m = MonthData(monthList[month], cellArray)
                        monthArray.append(m)

                y = YearData(year, monthArray)
                yearArray.append(y)
                print("\n")

        generateJson(Data(yearArray))
        
        '''
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
        '''

main()
