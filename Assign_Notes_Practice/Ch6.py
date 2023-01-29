'''
Ch6 - Dictionaries, Sets (dictionary with non repetitive key:values and not in a specific order)
Note: video notes are after chapter exercises
'''

lineBreak = "----------"

#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
print(f"{lineBreak} 6.1 {lineBreak}")
jc_denton = {"first_name":"JC", "last_name":"Denton", "age":23, "city":"NYC"}
print(jc_denton)

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
print(f"{lineBreak} 6.2 {lineBreak}")
fav_num = {"richard":4, "matt":31, "nick":55, "sam":16, "paul":12}
for person in fav_num:
	print(f"{person.title()}'s favorite number is {fav_num[person]}.")

'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
'''
print(f"{lineBreak} 6.3 {lineBreak}")
glossary = {
	"list":"python's version of an array. not restricted to one data type",
	"tuple":"an immutable list",
	"dir()":"this function will list what methods can be used with the object inside the ()",
	"interpreted":"python is an interpreted language, meaning that code is run line-by-line by target machine, not compiled",
	"indentation":"python requires indentation"
}
for entry in glossary:
	print(f"-{entry} : {glossary[entry]}")

#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
print(f"{lineBreak} 6.4 {lineBreak}")
glossary["set"] = "a collection with no repeated elements"
glossary["dictionary.items()"] = "will return both key and value"
glossary["dictionary.keys()"] = "will return only keys"
glossary["dictionary.values()"] = "will return the values in dictionary, including duplicated values"
glossary["sorted(dictionary)"] = "can be called in a loop to sort keys first and print in sorted order"

#loop in 6.3 would work, but this is another loop method
for k, v in glossary.items():
	print(f"Key: {k}\nValue: {v}\n")

'''
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
'''
print(f"{lineBreak} 6.5 {lineBreak}")
rivers = {"mississippi":"america", "nile":"egypt", "amazon":"brazil"}
for k, v in rivers.items():
	print(f"The {k.title()} runs through {v.title()}.")

for key in rivers.keys():
	print(key)

for value in rivers.values():
	print(value)
'''
6-6. Polling: Use the code in favorite_languages.py (page 97).
• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
'''
print(f"{lineBreak} 6.6 {lineBreak}")
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
poll = ["jen", "sarah", "richard", "edward"]
for person in poll:
	if person not in favorite_languages.keys():
		print(f"{person.title()}, please take our poll!")
	else:
		print(f"{person.title()}, thanks for taking our poll!")

#6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
print(f"{lineBreak} 6.7 {lineBreak}")
paul_denton = {"first_name":"Paul", "last_name":"Denton", "age":34, "city":"NYC"}
adam_jenson = {"first_name":"Adam", "last_name":"Jenson", "age":59, "city":"Detroit"}
people = [jc_denton, paul_denton, adam_jenson]
for person in people:
	print(person)

#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
print(f"{lineBreak} 6.8 {lineBreak}")
ted = {"type":"cat", "owner_name":"bill"}
ray = {"type":"dog", "owner_name":"larry"}
mike = {"type":"parrot", "owner_name":"steve"}
pets = [ted, ray, mike]
for pet in pets:
	print(pet)

#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.
print(f"{lineBreak} 6.9 {lineBreak}")
favorite_places = {"richard":["japan", "poland", "australia"], "matt":["australia"], "paul":["DC", "NYC"]}
for name, places in favorite_places.items():
	print(f"{name.title()}'s favorite places are: ")
	for place in places:
		print(f"\t{place}")		

#6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers. 
print(f"{lineBreak} 6.10 {lineBreak}")
fav_num2 = {"richard":[4, 16, 86], "matt":[31], "nick":[55, 99], "sam":[16], "paul":[12, 48, 22]}
for person, numbers in fav_num2.items():
	print(f"{person.title()}'s favorite numbers are: ", end = "")
	for number in numbers:
		print(f"{number}, ", end = "")
	print()

#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
print(f"{lineBreak} 6.11 {lineBreak}")
cities = {
	"tokyo": {
		"country": "japan",
		"population": "38.468 million",
		"fact": "hosted the most recent olympics in 2021",
	},
	"warsaw": {
	"country": "poland",
	"population": "3.1 million",
	"fact": "has the tallest building in the EU as of 2022 - Varso Place",
	},
	"rio de janerio": {
		"country": "brazil",
		"population": "12.280 million",
		"fact": "more Portuguese speaking people live here than in the entire country of Portugal",
	},
}
for city_name, city_info in cities.items():
	print(f"\nCity: {city_name.title()}")
	print(f"\tCountry: {city_info['country'].title()}")#NOTE: single quote ' REQUIRED - using double quotes causes error
	print(f"\tPopulation: {city_info['population']}")
	print(f"\tFact: {city_info['fact']}")

#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.
print(f"{lineBreak} 6.12 {lineBreak}")
print("i chose to update 6.7\n")
for person in people:
	name = f"{person['first_name'].title()} {person['last_name'].title()}"
	print(f"{name} is {person['age']} years old and lives in {person['city']}.")

'''
-git video: 
	i am familar with git and github from previous CS coursework
-dictionaries video: 
	dictionaries have a default constructor 
 	video also discusses try/except which is like java's try/catch 
	get() provides a method to create default return for a key that doesn't exist
-hackathon video:
	-'//' is integer division operator for python
 	-
'''