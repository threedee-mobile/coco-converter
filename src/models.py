import json

class Model:
	def toJson(self):
		 return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=2)

class Column(Model):
	def __init__(self, columnId, lon, lat, xco2):
		self.id = columnId
		self.lon = lon
		self.lat = lat
		self.xco2 = xco2

class XCo2(Model):
	def __init__(self, monthly_xco2, monthly_uncertainty):
		self.monthly_xco2 = monthly_xco2
		self.monthly_uncertainty = monthly_uncertainty

class Place(Model):
	def __init__(self, placeId, city, region, country, lon, lat, primaryColumn, neighouringColumns):
		self.id = placeId
		self.city = city
		self.region = region
		self.country = country
		self.lon = lon
		self.lat = lat
		self.primaryColumn = primaryColumn
		self.neighouringColumns = neighouringColumns
