import json

class Model:
	def toJson(self) -> str:
		 return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=2)

'''
@param monthly_xco2         An array of size 12 containing the average XCO2 (in units of ppm) for the month corresponding to the index 
@param monthly_uncertainty  An array of size 12 containing the uncertainty (in units of ppm) associated with the monthly XCO2 at the same index
'''
class XCo2(Model):
	def __init__(self, monthly_xco2: float, monthly_uncertainty: float):
		self.monthly_xco2 = monthly_xco2
		self.monthly_uncertainty = monthly_uncertainty
		
'''
Represents the column defined by the OCO-2 data 
@param columnId   Random UUID
@param lon        The longitude at the center of the sounding field-of-view
@param lat        The latitude at the center of the sounding field-of-view
@param xco2       The XCO2 calculated over the year
'''
class Column(Model):
	def __init__(self, columnId: str, lon: float, lat: float, xco2: XCo2):
		self.id = columnId
		self.lon = lon
		self.lat = lat
		self.xco2 = xco2

'''
Represents a city or point of interest in our data set 
@param placeId             Random UUID
@param city                Lowercase name of the city
@param region              Lowercase name of the province or state
@param country             2-character country code 
@param lon 				
@param lat 					
@param primaryColumn       The closest OCO-2 column to this location
@param neighouringColumns  An array of OCO-2 columns in the 50km radius around this location
'''
class Place(Model):
	def __init__(self, placeId: str, city: str, region: str, country: str, lon: float, lat: float, primaryColumn: Column, neighouringColumns):
		self.id = placeId
		self.city = city
		self.region = region
		self.country = country
		self.lon = lon
		self.lat = lat
		self.primaryColumn = primaryColumn
		self.neighouringColumns = neighouringColumns
