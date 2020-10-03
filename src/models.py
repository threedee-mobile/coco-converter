import json

class Model:
	def toJson(self) -> str:
		 return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=2)

'''
@param value         An XCO2 (in units of ppm) reading from the OCO-2 data
@param uncertainty   The uncertainty (in units of ppm) associated with the reading
'''
class XCO2(Model):
	def __init__(self, value: float, uncertainty: float):
		self.value = value
		self.uncertainty = uncertainty
		
'''
Represents the column defined by the OCO-2 data 
@param id     Random UUID
@param lon    The longitude at the center of the sounding field-of-view
@param lat    The latitude at the center of the sounding field-of-view
@param xco2   XCO2 data of ths column
'''
class Column(Model):
	def __init__(self, columnId: str, lon: float, lat: float, xco2: XCO2):
		self.id = columnId
		self.lon = lon
		self.lat = lat
		self.xco2 = xco2

'''
Represents a city or point of interest in our data set 
@param id                   Random UUID
@param city                 Lowercase name of the city
@param region               Lowercase name of the province / state
@param country              Lowercase 2-character country code 
@param lon 				
@param lat 					
@param monthly              An array of 12 containing the average XCO2 for the month corresponding to the index 
@param neighbouringColumns  An array of Columns in the 50km radius around this location
'''
class Place(Model):
	def __init__(self, placeId: str, city: str, region: str, country: str, lon: float, lat: float, monthly, neighbouringColumns):
		self.id = placeId
		self.city = city
		self.region = region
		self.country = country
		self.lon = lon
		self.lat = lat
		self.monthly = monthly
		self.neighbouringColumns = neighbouringColumns
