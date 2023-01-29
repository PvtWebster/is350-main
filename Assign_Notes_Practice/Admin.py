#from Assign_Notes_Practice.User import User #9.11 exercise version
from Snipets.User import User #9.12 exercise verions
from Assign_Notes_Practice.Privileges import Privileges
class Admin(User):
	"""Admin class - child class of User with privileges field added"""
	def __init__(self, first, last, age, gender, status):
		super().__init__(first, last, age, gender, status)
		self.privileges = Privileges()
	def getName(self):
		print(self.first_name)