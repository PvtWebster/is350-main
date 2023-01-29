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
		print(f"Greetings {self.first_name} {self.last_name}! This user class was imported")
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login(self):
		self.login_attempts = 0
	def getLogin(self):
		print(f"total logins = {self.login_attempts}")