'''
Ch7 - User input and while loops
'''

lineBreak = "----------"
print(f"{lineBreak} video code {lineBreak}")
print("the way to get the index of list values is to use the enumerate() function")
days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
for i,d in enumerate(days):
	print(i, d)

print("\nNOTE: also dont do 'input = input(\"some string here\")' because python doesn't like 'input' as a variable name. creates TypeErrors\n")
#7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
print(f"{lineBreak} 7.1 {lineBreak}")
user_in = input("What brand of car would you like for your rental: ")
print(f"Let me see if I can find you a {user_in}.")

#7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
print(f"{lineBreak} 7.2 {lineBreak}")
user_in = input("How many people are in your group: ")
user_in = int(user_in)
if (user_in < 8):
	print("A table is available!")
else:
	print("A table is not available for groups of 8+. Please wait until one becomes available.")

#7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
print(f"{lineBreak} 7.3 {lineBreak}")
user_in = int(input("Please enter a number: "))
if (user_in % 10 == 0):
	print(f"{user_in} is divisible by 10.")
else:
	print(f"{user_in} is not divisible by 10.")

#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.
print(f"{lineBreak} 7.4 {lineBreak}")
user_in = ""
while (user_in != "quit"):
	user_in = input("Please enter a pizza topping or \"quit\": ")
	if(user_in == "quit"):
		print("exiting...")
	else:
		print(f"{user_in} added to pizza.")

#7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
print(f"{lineBreak} 7.5 {lineBreak}")
age = 0
price = 0
while (age <= 0):
	age = int(input("Please enter your age: "))
	if (age > 0) and (age < 3):
		price = 0
	elif (age >=3) and (age < 12):
		price = 10
	else:
		price = 15

	if (age > 0):
		print(f"Your ticket price is ${price}.")
		
'''
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
'''
print(f"{lineBreak} 7.6 {lineBreak}")
print("i chose 7-4")
user_in = ""
count = 0
while (count < 3):
	user_in = input("Please enter a pizza topping or \"quit\": ")
	if(user_in == "quit"):
		print("exiting...")
		break
	else:
		count += 1
		print(f"{user_in} added to pizza. There are {count} total toppings.")

#7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
print(f"{lineBreak} 7.7 {lineBreak}")
print("****WARNING :: THIS EXERCISE REQUIRES AN INFINITE LOOP :: WARNING****")
# CONSTANT = 1
# while (CONSTANT > 0):
# 	print("Infinite loop: 1 always greater than 0")

#7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
print(f"{lineBreak} 7.8 {lineBreak}")
print("Used for loop instead of while loop - see code for example to denumerate list via index values")
san_order = ["reuben", "club", "italian"]
san_fin = []
#source for for loop parameters below: https://realpython.com/python-enumerate/
for i in range(len(san_order) - 1, -1, -1): #range(start pos, end pos (-1 since 0 will not include index 0), increment val)
	print(f"I have made your {san_order[i]} sandwich")
	san_fin.append(san_order[i])
	del san_order[i]
san_fin.reverse()
print(f"orders complete = {san_fin}, orders remaining = {san_order}")

#7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
print(f"{lineBreak} 7.9 {lineBreak}")
sandwich_orders = ["pastrami", "reuben", "club", "pastrami", "italian", "pastrami"]
finished_sandwiches = []
print("deli is out of pastrami")
while ("pastrami" in sandwich_orders):
	sandwich_orders.remove("pastrami")
for san in sandwich_orders:
	finished_sandwiches.append(san)
sandwich_orders.clear()
print(f"remaining orders = {sandwich_orders}, completed = {finished_sandwiches}")

#7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
print(f"{lineBreak} 7.10 {lineBreak}")
results = {}
active = True
while (active == True):
	name = input("Please enter your name: ")
	user_in = input("If you could visit one place in the world, where would you go: ")
	results[name] = user_in
	user_in = input("Does another person need to respond (yes/no): ")
	if (user_in == "no"):
		active = False

print("\n---Results---\n")
for name, answer in results.items():
	print(f"{name} would like to travel to {answer}.")