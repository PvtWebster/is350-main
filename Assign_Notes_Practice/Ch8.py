'''
Ch8 - Functions
-python allows arguments to be be out of order if they're defined when called
ex: function(int, string)  -->  function(string="first", int=2)
-python allows, rather handles lists/arrays, using the * character
ex: def multi_add(*args)
	result = 0
	for x in args:
		result = result + x
	return result
'''

lineBreak = "----------"

#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
print(f"{lineBreak} 8.1 {lineBreak}")
def display_message():
	print("This week, in chapter 8, we are learning about functions")
display_message()

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
print(f"{lineBreak} 8.2 {lineBreak}")
def favorite_book(title):
	title = str(title) #require cast to string in case title of book is mistyped by python
	print(f"One of my favorite books is {title.title()}.")
favorite_book(1984)

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
print(f"{lineBreak} 8.3 {lineBreak}")
print("This uses positional arguments")
def make_shirt(size, message):
	print(f"Printing shirt of size {size.title()} with the text: '{message}'.")
make_shirt("L", "first shirt")
make_shirt(message="second shirt", size="M")

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
print(f"{lineBreak} 8.4 {lineBreak}")
print("This uses positional arguments and keyword arguments")
def make_shirt(size, message="I love python"):
	print(f"Printing a {size} shirt with text: '{message}'.")
make_shirt("L")
make_shirt("M")
make_shirt("XL", "third shirt, diff message")

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
print(f"{lineBreak} 8.5 {lineBreak}")
def describe_city(name, country = "united states of america"):
	print(f"{name.title()} is in {country.title()}.")

describe_city("milwaukee")
describe_city("los angeles")
describe_city("tokyo", "japan")

'''
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
-------------------
"Santiago, Chile"
-------------------
Call your function with at least three city-country pairs, and print the values that are returned.
'''
print(f"{lineBreak} 8.6 {lineBreak}")
def city_country(city, country):
	print(f"{city.title()}, {country.title()}")
city_country("sydney", "australia")
city_country("warsaw", "poland")
city_country("rio de janerio", "brazil")

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
print(f"{lineBreak} 8.7 {lineBreak}")
def make_album(artist_name, album_title, songs = None):
	album = {'artist': artist_name.title(), 'album': album_title.title()}
	if songs is not None:
		album['songs'] = songs
	return album
album = make_album("pink floyd", "dark side of the moon")
print(album)
album = make_album("the used", "artwork")
print(album)
album = make_album("my chemical romance", "the black parade", 14)
print(album)

#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
print(f"{lineBreak} 8.8 {lineBreak}")
def make_album(artist_name, album_title, songs = None):
	album = {'artist': artist_name.title(), 'album': album_title.title()}
	if songs is not None:
		album['songs'] = songs
	return album
user_q = ""
print("Enter new entries to album archive. Enter 'n' at anytime to exit.")
while (user_q != "n"):
	name1 = input("Enter artist name: ")
	if (name1 == "n"):
		break
	name2 = input("Enter album title: ")
	if (name2 == "n"):
		break
	album = make_album(name1, name2)
	print(album)
	user_q = input("Would you like to enter another entry? y/n?")

#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
print(f"{lineBreak} 8.9 {lineBreak}")
messages = ["series", "of", "short", "text", "messages"]
def show_messages(list):
	for item in list:
		print(item)
show_messages(messages)

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.
sent_msgs = []
print(f"{lineBreak} 8.10 {lineBreak}")
def send_messages(messages, sent):
		while (len(messages) > 0):
			msg = messages.pop()
			print(f"Sending message: '{msg}' ...")
			sent.append(msg)

send_messages(messages, sent_msgs)
print(f"\nmessages to send: {messages}")
print(f"sent messages: {sent_msgs}")

#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.
print(f"{lineBreak} 8.11 {lineBreak}")
new_msgs = []
send_messages(sent_msgs[:], new_msgs) #[:] copies list to preserve original
print(f"original list: {sent_msgs}")
print(f"list that recieved recieve messages: {new_msgs}")

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
print(f"{lineBreak} 8.12 {lineBreak}")
def sandwich_toppings(*toppings):
	print("making a sandwich with the following toppings: ")
	for i in toppings:
		print(f"- {i}")
	print()
sandwich_toppings("ham")
sandwich_toppings("cheese", "marinara", "italian seasoning")
sandwich_toppings("lettuce", "tomatoes", "onions", "green peppers", "oil", "vinegar")

#8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
print(f"{lineBreak} 8.13 {lineBreak}")
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
user_profile = build_profile('richard', 'mogilka', location='milwaukee', major='computer science', status="tired")
print(user_profile)

'''
8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
--------------------------------------------------------------------
car = make_car('subaru', 'outback', color='blue', tow_package=True)
--------------------------------------------------------------------
Print the dictionary that’s returned to make sure all the information was stored correctly.
'''
print(f"{lineBreak} 8.14 {lineBreak}")
def make_car(make, model, **args): #need ** which will create an empty dictionary to hold additional arguments to put into final dictionary
	args["make"] = make
	args["model"] = model
	return args
car = make_car("nissan", "rogue", color="black", year=2016)
print(car)

#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
print(f"{lineBreak} 8.15 {lineBreak}")
import printing_models as pm
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm.print_models(unprinted_designs, completed_models)
pm.show_completed_models(completed_models)

'''
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
---------------------------------------------
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
---------------------------------------------
'''
print(f"{lineBreak} 8.16 {lineBreak}")
import printing_models
printing_models.describe_city("tokyo1", "japan1")
from printing_models import describe_city
describe_city("tokyo2", "japan2")
from printing_models import describe_city as dc
dc("tokyo3", "japan3")
print("the next 2 calls cause errors because the file is not a callable module, so they are commented out")
# import printing_models as pm
# pm("tokyo4", "japan4")
# from printing_models import *
# describe_city("tokyo5", "japan5")

#8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
print(f"{lineBreak} 8.17 {lineBreak}")
print("my code already follows these conventions")