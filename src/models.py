import json

class Model:
	def toJson(self) -> str:
		 return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=2)

class XCo2(Model):
	def __init__(self, monthly_xco2: float, monthly_uncertainty: float):
		self.monthly_xco2 = monthly_xco2
		self.monthly_uncertainty = monthly_uncertainty
		
class Column(Model):
	def __init__(self, columnId: str, lon: float, lat: float, xco2: XCo2):
		self.id = columnId
		self.lon = lon
		self.lat = lat
		self.xco2 = xco2

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
