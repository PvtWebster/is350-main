class Vehicle:
	"""vehicle class"""
	def __init__(self,name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage
	def getAttributes(self):
		print(f"Name of {type(self).__name__} = {self.name}\nMaximum Speed = {self.max_speed}\nMileage = {self.mileage}") #use type function to get the object name for printing
class Bus(Vehicle):
	"""bus child class from vehicle class"""
	def __init__(self, name, max_speed, mileage):
		super().__init__(name, max_speed, mileage)

print("--------------------------------11.14.2022 LAB------------------------------------")
bus = Bus("Volvo", 180, 12)
bus.getAttributes()