'''
Ch10 - Files and Exceptions

VIDEO NOTES:
-'f.mode' checks what mode the file is currently in: read, write, append; this can also be used to check if the file exists
'''
import json
lineBreak = "----------"

#10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.
print(f"{lineBreak} 10.1 {lineBreak}")
filepath = "/home/runner/IS350/Assign_Notes_Practice/learning_python.txt"#absolute filepath for replit, based on the shell dir structure
with open(filepath) as file_object:
	contents = file_object.read()#1 - read entire file
print(contents)#1
print("*************end print 1**************")
with open(filepath) as file_object:
	for line in file_object:
		print(line)#2 - print line every loop
print("*************end print 2**************")
with open(filepath) as file_object:
	lines = file_object.readlines()#3 - store line in list for last printing task
for line in lines:
	print(line.rstrip())
print("*************end print 3**************")
'''
10-2. Learning C: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
----------------------------------------
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
----------------------------------------
Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.
'''
print(f"{lineBreak} 10.2 {lineBreak}")
with open(filepath) as file_object:
	for line in file_object:
		print(line.replace("python", "C").rstrip())#NOTE: this does not WRITE to the file, simply reads, modifies, then prints to screen

#10-3. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
print(f"{lineBreak} 10.3 {lineBreak}")
with open("guest.txt", "w") as file_object:
	std_in = input("Please enter your name: ")
	file_object.write(std_in)
	print(f"name '{std_in}' added to 'guest.txt' file")

#10-4. Guest Book: Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.
print(f"{lineBreak} 10.4 {lineBreak}")
std_in = "y"
while (std_in != "n"):
	file_object = open("guest_book.txt", "a")
	std_in = input("Please enter your name: ")
	file_object.write(std_in+"\n")
	print(f"welcome {std_in}!\n")
	std_in = input("enter another guest name? y/n?")
	if std_in == "n":
		file_object.close()
	
#10-5. Programming Poll: Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.
print(f"{lineBreak} 10.5 {lineBreak}")
std_in = "y"
while (std_in != "n"):
	file_object = open("programming.txt", "a")
	std_in = input("why do you like programming: ")
	file_object.write(std_in+"\n")
	std_in = input("enter another reason? y/n?")
	if std_in == "n":
		file_object.close()

#10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.
print(f"{lineBreak} 10.6 {lineBreak}")
def numNoRepeat():
	"""take int input from user - catch and print exception if input not int"""
	print("provide two numbers and i will add them together")
	numbers = []
	while len(numbers) < 2:
		num = input("enter number: ")
		try:
			num = int(num)
		except ValueError:
			print(f"non-numeric input \"{num}\" detected! exiting program...")
			return #return instead of break to prevent code after while loop from running if exception occurred
		numbers.append(num)
	sum = numbers[0] + numbers[1]
	print(f"the sum of {numbers[0]} + {numbers[1]} = {sum}")

numNoRepeat()

#10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.
print(f"{lineBreak} 10.7 {lineBreak}")
def numWithRepeat():
	"""take int input from user - catch/print exception if not int and reprompt new input from user"""
	print("provide two numbers and i will add them together")
	numbers = []
	while len(numbers) < 2:
		num = input("enter number: ")
		validEntry = False
		while (validEntry == False):
			try:
				num = int(num)
			except ValueError:
				print(f"non-numeric input \"{num}\" detected!") #return instead of break to prevent code after while loop from running if exception
				break
			#isinstance(object, class): Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof. If object is not an object of the given type, the function always returns False
			if isinstance(num, int) == True:
				validEntry = True
				numbers.append(num)
	sum = numbers[0] + numbers[1]
	print(f"the sum of {numbers[0]} + {numbers[1]} = {sum}")

numWithRepeat()

#10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
print(f"{lineBreak} 10.8 {lineBreak}")
print("this section is commented out as it will produce errors/exceptions as files are created, moved, and accessed via absolute paths")
# import shutil
# with open("cats.txt", "w") as cats:
# 	cats.write("black\ntabby\ncalico")
	
# with open("dogs.txt", "w") as dogs:
# 	dogs.write("lab\nhusky\npomeranian")

# filename = "/home/runner/IS350/cats.txt"
# with open(filename, "r") as cat_read:
# 	for cat in cat_read:
# 		print(cat)

# shutil.move("dogs.txt", "/home/runner/IS350/Assign_Notes_Practice/")
# filename = "/home/runner/IS350/dogs.txt"
# try:
# 	with open(filename, "r") as dog_read:
# 		for dog in dog_read:
# 			print(dog)
# except FileNotFoundError:
# 	print("file not found")

# shutil.move("dogs.txt", "/home/runner/IS350/")#move dogs back to original location

#10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.
print(f"{lineBreak} 10.9 {lineBreak}")
print("the only thing necessary would be to not print anything in the except block - 'pass' can be used as a placeholder")
	
'''
10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer. You can use the count() method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:
-----------------------------------------
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
-----------------------------------------
Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted. Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is.
'''
print(f"{lineBreak} 10.10 {lineBreak}")
def countWords(file, word):
	"""count the number of occurances of a given prompt in a text file"""
	search_word = word
	try:
		with open(file, encoding="utf-8") as f:
			contents = f.readlines()
	except FileNotFoundError:
		print(f"{file} doesn't exist")
	else:
		count = 0
		for line in contents:
			words = line.split()
			for word in words:
				#print(word)
				if word == search_word:
					count += 1
	
	return print(f"total count of the word '{search_word}' in '{file}' is: {count}")
countWords("The Odyssey.txt", "the")
countWords("The Odyssey.txt", "the ")

#10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”
print(f"{lineBreak} 10.11 {lineBreak}")
favNum = input("enter your favorite number: ")
filename = "favNum.json"
with open(filename, "w") as j:
	json.dump(favNum, j)
with open(filename, "r") as j:
	favNum = json.load(j)
	print(f"I know your favorite number! it's {favNum}")
#10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.
print(f"{lineBreak} 10.12 {lineBreak}")
print("NOTE: code from 10.11 conflicts with this section")
def greet():
	"""Greet the user by name."""
	filename = 'favNum.json'
	try:
		with open(filename) as f:
			favNum = json.load(f)
	except FileNotFoundError:
		favNum = input("enter your favorite number: ")
		with open(filename, 'w') as f:
			json.dump(favNum, f)
			print(f"We'll remember your number when you come back!")
	else:
		print(f"I know your favorite number! it's {favNum}")

greet()
#10-13. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program. Before printing a welcome back message in greet_user(), ask the user if this is the correct username. If it’s not, call get_new_username() to get the correct username.
print(f"{lineBreak} 10.13 {lineBreak}")

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
		return username
def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		verfication = input(f"is {username} the correct username: y/n?")
		if verfication == "n":
			username = get_new_username()
			print(f"We'll remember you when you come back, {username}!")
		else:
			print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

greet_user()