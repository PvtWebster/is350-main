class Privileges:
	"""privileges class"""
	def __init__(self):
		self.privileges = ["can add post2", "can delete post2", "can ban user2"]
	def show_privileges(self, name):
		print("this is imported privileges")
		for i in self.privileges:
			print(f"'{name}' can {i}")