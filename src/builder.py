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

def co2MonthAvg(ds, long, lat, month):
    checkLong, checkLat = ds['lon'][:], ds['lat'][:]
    longInd = np.argsort(np.abs(checkLong - long))[0]
    latInd = np.argsort(np.abs(checkLat - lat))[0]
    print(longInd, latInd)
    return ds['land'][month-1, latInd, longInd]

def id() -> str:
	return str(uuid.uuid4())

def generateCell(lon: float, lat: float, ff_co2: float, ib_co2: float) -> Cell:
	cell = Cell(id(), lat, lon, ff_co2, ib_co2)
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

        '''
        # Boundary latitudes/longitudes for scanning the data. [Canada]
        latMin, latMax = 42, 83
        lonMin, lonMax = -141, -53
        '''
        #'''
        # Boundary latitudes/longitudes for scanning the data. [North America]
        latMin, latMax = 10, 83
        lonMin, lonMax = -180, -53
        #'''
        
        for year in [2016, 2017, 2018]:
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

                                        # Ignore any data points that fall outside the boundaries we set.
                                        if (lat < latMin or lat > latMax or lon < lonMin or lon > lonMax):
                                                continue
                                        
                                        ff_co2, ib_co2 = ffList[month, i, j], ibList[month, i, j]

                                        # Ignore any data points that have no emission.
                                        if (ff_co2 == 0 and ib_co2 == 0):
                                                continue

                                        # Create a data cell from this data, at this point.
                                        c = generateCell(float(lon), float(lat), float(ff_co2), float(ib_co2))
                                        cellArray.append(c)

                        # Aggregate all the cells for a given month to create a data profile for the month.
                        m = MonthData(monthList[month], cellArray)
                        monthArray.append(m)

                # Aggregate all the data from all months to create a profile for the year.
                y = YearData(year, monthArray)
                yearArray.append(y)
                print("\n")

        # Put together all years to generate the Json file.
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
