'''
Ch9 - Classes
'''

lineBreak = "----------"

#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
print(f"{lineBreak} 9.1 {lineBreak}")
class Restaurant:
	"""Restaurant class"""
	def __init__(self, name, type):
		self.restaurant_name = name
		self.cuisine_type = type
	def describe_restaurant(self):
		print(f"The restaurant's name is '{self.restaurant_name}' and it serves {self.cuisine_type} food.")
	def open_restaruant(self):
		print(f"{self.restaurant_name} is open!")

res1 = Restaurant("9.1 restaurant", "italian")
res1.describe_restaurant()
res1.open_restaruant()

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
print(f"{lineBreak} 9.2 {lineBreak}")
res2 = Restaurant("mario's", "italian")
res3 = Restaurant("xian's", "chinese")
res4 = Restaurant("jose's", "mexican")
res2.describe_restaurant()
res3.describe_restaurant()
res4.describe_restaurant()

#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.
print(f"{lineBreak} 9.3 {lineBreak}")
class User:
	def __init__(self, first, last, age, gender, status):
		self.first_name = first
		self.last_name = last
		self.age = age
		self.gender = gender
		self.marital_status = status
	def describe_user(self):
		print(f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nMarital Status: {self.marital_status}\n")
	def greet_user(self):
		print(f"Greetings {self.first_name} {self.last_name}!")

user1 = User("richard", "mogilka", 36, "male", "single")
user2 = User("paul", "mogilka", 72, "male", "married")
user3 = User("grazyna", "mogilka", 68, "female", "married")
user1.greet_user(), user1.describe_user(), user2.greet_user(), user2.describe_user(), user3.greet_user(), user3.describe_user()

#9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.
print(f"{lineBreak} 9.4 {lineBreak}")
class Restaurant:
	"""Restaurant class - updated to include total number of customers served"""
	def __init__(self, name, type):
		self.restaurant_name = name
		self.cuisine_type = type
		self.number_served = 0
	def describe_restaurant(self):
		print(f"The restaurant's name is '{self.restaurant_name}' and it serves {self.cuisine_type} food.")
	def open_restaruant(self):
		print(f"{self.restaurant_name} is open!")
	def addNumberServed(self, num):
		self.number_served += num
		print(f"{num} added to {self.restaurant_name} total customers served. current total = {self.number_served}")

res5 = Restaurant("bill's", "american")
print(f"number of customers served at {res5.restaurant_name}: {res5.number_served}")
res5.addNumberServed(10)
res5.addNumberServed(55)

#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). Write a method called increment_login _attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
print(f"{lineBreak} 9.5 {lineBreak}")
class User:
	"""User class - updated to include login attempts"""
	def __init__(self, first, last, age, gender, status):
		self.first_name = first
		self.last_name = last
		self.age = age
		self.gender = gender
		self.marital_status = status
		self.login_attempts = 0
	def describe_user(self):
		print(f"Name: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nMarital Status: {self.marital_status}\nLogin Attempts: {self.login_attempts}\n")
	def greet_user(self):
		print(f"Greetings {self.first_name} {self.last_name}!")
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login(self):
		self.login_attempts = 0
	def getLogin(self):
		print(f"total logins = {self.login_attempts}")

user5 = User("nine", "five", 95, "male", "single")
user5.increment_login_attempts(), user5.increment_login_attempts(), user5.increment_login_attempts(), user5.increment_login_attempts()
user5.getLogin()
user5.reset_login()
user5.getLogin()

#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
print(f"{lineBreak} 9.6 {lineBreak}")
class IceCreamStand(Restaurant):
	"""child class of (parent) restaurant class"""
	def __init__(self, name, type, flavors):
		super().__init__(name, type)
		self.flavors = flavors
	def printFlavors(self):
		print(f"the flavors for {self.restaurant_name} are: ")
		for i in self.flavors:
			print(i)
ics1 = IceCreamStand("kopps", "desert", ["chocolate", "vanilla", "strawberry", "flavor of the day"])
ics1.printFlavors()

#9-7. Admin: An administrator is a special kind of user. Write a class calledAdmin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
print(f"{lineBreak} 9.7 {lineBreak}")
class Admin(User):
	"""Admin class - child class of User with privileges field added"""
	def __init__(self, first, last, age, gender, status):
		super().__init__(first, last, age, gender, status)
		self.privileges = ["can add post", "can delete post", "can ban user"] 
	def show_privileges(self):
		for i in self.privileges:
			print(f"'{self.first_name}' can {i}")
admin1 = Admin("addy", "admin", 9000, "admin", "online")
admin1.show_privileges()

#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
print(f"{lineBreak} 9.8 {lineBreak}")
class Privileges:
	"""privileges class"""
	def __init__(self):
		self.privileges = ["can add post2", "can delete post2", "can ban user2"]
	def show_privileges(self, name):
		print(self.privileges)
		for i in self.privileges:
			print(f"'{name}' can {i}")
class Admin(User):
	"""Admin class - child class of User with privileges field added"""
	def __init__(self, first, last, age, gender, status):
		super().__init__(first, last, age, gender, status)
		self.privileges = Privileges()
	def getName(self):
		print(self.first_name)

admin2 = Admin("addy2", "admin2", 10000, "admin2", "online2")
admin2.privileges.show_privileges(admin2.first_name)

#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 100 if it isn’t already. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.
print(f"{lineBreak} 9.9 {lineBreak}")
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")	
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
				self.odometer_reading = mileage
		else:
				print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery:
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
				range = 260
		elif self.battery_size == 100:
				range = 315
		print(f"This car can go about {range} miles on a full charge.")
	def upgrade_battery(self):
		"""check if battery size at least 100 - if less than, set to 100"""
		if self.battery_size < 100:
			self.battery_size = 100
			print("battery upgraded")
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

my_car = ElectricCar('thor', 'storm', 2022)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
print(f"{lineBreak} 9.10 {lineBreak}")
from Assign_Notes_Practice.Restaurant import Restaurant as R
res6 = R("david's", "thai")
res6.describe_restaurant()
'''
https://stackoverflow.com/questions/4534438/typeerror-module-object-is-not-callable
'''

#9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
print(f"{lineBreak} 9.11 {lineBreak}")
from Assign_Notes_Practice.Admin import Admin as A
admin3 = A("addy3", "admin3", 11000, "admin3", "online3")
admin3.privileges.show_privileges(admin3.first_name)

#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
print(f"{lineBreak} 9.12 {lineBreak}")
from Assign_Notes_Practice.Admin import Admin as A_U
admin4 = A_U("addy4", "admin4", 12000, "admin4", "online4")
admin4.greet_user()
admin4.privileges.show_privileges(admin4.first_name)

#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
print(f"{lineBreak} 9.13 {lineBreak}")
import random
class Die:
	def __init__(self, sides=6):
		self.sides = sides
	def roll_die(self):
		print(f"rolled = {random.randint(1,self.sides)}")
print("**********6-sided die**********")
die1 = Die()
for i in range(10):
	die1.roll_die()
print("**********10-sided die**********")
die2 = Die(10)
for i in range(10):
	die2.roll_die()
print("**********20-sided die**********")
die3 = Die(20)
for i in range(10):
	die3.roll_die()
#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four numbers or letters from the list and print a message saying that any ticket matching these four numbers or letters wins a prize.
print(f"{lineBreak} 9.14 {lineBreak}")
lotto = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5, 6, 7, 8, 9, 10]
def create_ticket():
	"""Create lottery ticket containing 4 nonrepeating values"""
	ticket = []
	while (len(ticket) < 4):
		valid = True
		index = random.randint(0, 14)
		value = lotto[index]
		for i in ticket:
			if i == value:
				valid = False
		if valid == True:
			ticket.append(value)
	return ticket
my_ticket = create_ticket()
print(f"9.14 ticket = {my_ticket}")
#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
print(f"{lineBreak} 9.15 {lineBreak}")
count = 0
my_ticket = create_ticket()
victory = False
while (victory == False):
	winning_ticket = create_ticket()
	count += 1
	i = 0
	for i in range(4):
		if my_ticket[i] != winning_ticket[i]:
			break
		if my_ticket[i] == winning_ticket[i]:
			if i == 3:
				victory = True

print(f"my_ticket = {my_ticket} and winning_ticket = {winning_ticket}. total pulls = {count}")
#print("this section commented out because, using a permutaion of 15P4, there are over 32000 possible ticket combinations. ")
#9-16. Python Module of the Week: One excellent resource for exploring the Python standard library is a site called Python Module of the Week. Go to https://pymotw.com/ and look at the table of contents. Find a module that looks interesting to you and read about it, perhaps starting with the random module.
print(f"{lineBreak} 9.16 {lineBreak}")
print("no output expected")