class Restaurant:
	"""Restaurant class - updated to include total number of customers served"""
	def __init__(self, name, type):
		self.restaurant_name = name
		self.cuisine_type = type
		self.number_served = 0
	def describe_restaurant(self):
		print(f"The restaurant's name is '{self.restaurant_name}' and it serves {self.cuisine_type} food. this restaurant class is imported")
	def open_restaruant(self):
		print(f"{self.restaurant_name} is open!")
	def addNumberServed(self, num):
		self.number_served += num
		print(f"{num} added to {self.restaurant_name} total customers served. current total = {self.number_served}")