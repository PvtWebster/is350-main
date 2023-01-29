'''
Ch4 is all about loops (specifically for 'each' loops) and manipulating lists: copying and splitting. there is significant emphesis on indentation which is important for python since '{}' are not used to denote code blocks
'''

lineBreak = "----------"
'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''
print(f"{lineBreak} 4.1 {lineBreak}")
pizzas = ["Works", "BBQ Chicken", "Spuds Supreme"]
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("Pizza is my favorite food!")
'''
4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!
'''
print(f"{lineBreak} 4.2 {lineBreak}")
animals = ["cat", "dog", "ferret"]
for pet in animals:
    print(pet)
for pet in animals:
    print(f"A {pet} would make a great pet.")
print(
    "What does these animals have in common? I've lived in a house with each of them as pets."
)

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
print(f"{lineBreak} 4.3 {lineBreak}")
listOfTwenty = list(range(1, 21))
for num in listOfTwenty:
    print(num)

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
print(f"{lineBreak} 4.4 {lineBreak}")
print("****WARNING :: THIS EXERCISE WILL PRINT ONE MILLION VALUES TO SCREEN :: WARNING****")
# oneMil = []
# for num in range(1,1000001):
# 	oneMil.append(num)
# 	print(num)

#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
print(f"{lineBreak} 4.5 {lineBreak}")
oneMil = list(range(1, 1000001))
print(f"min = {min(oneMil)}")
print(f"max = {max(oneMil)}")
print(f"sum = {sum(oneMil)}")

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
print(f"{lineBreak} 4.6 {lineBreak}")
odds = list(range(1, 21, 2))
for num in odds:
    print(num)

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
print(f"{lineBreak} 4.7 {lineBreak}")
threes = []
for num in range(3, 31, 3):
    threes.append(num)
    print(num)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
print(f"{lineBreak} 4.8 {lineBreak}")
cubes = []
for num in range(1, 11):
    cubes.append(num**3)
    print(f"{num}^3 -> {num**3}")

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
print(f"{lineBreak} 4.9 {lineBreak}")
cubeComp = [num**3 for num in range(1, 11)]
print(cubeComp)
'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
'''
print(f"{lineBreak} 4.10 {lineBreak}")
print(f"The first three items in the list are: {cubeComp[0:3]}")
print(f"Three items from the middle of the list are: {cubeComp[4:7]}")
print(f"The last three items in the list are: {cubeComp[7:10]}")
'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
'''
print(f"{lineBreak} 4.11 {lineBreak}")
friend_pizzas = pizzas[:]
pizzas.append("Mac'n'Cheese")
friend_pizzas.append("Hawaiian")
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
print(f"{lineBreak} 4.12 {lineBreak}")
print(
    "Is this not just the same exercise from 4.11? Printing two seperate lists with two seperate loops?"
)
'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the change.
• The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
'''
print(f"{lineBreak} 4.13 {lineBreak}")
foods = ("coleslaw", "mashed potatoes", "mixed vegatables", "rice",
         "baked beans")
for food in foods:
    print(food)
print(
    "**EXCEPTION POSSIBLE IF NEXT LINE NOT COMMENTED OUT - ATTEMPTING TO MODIFY TUPLE CAUSES ERROR**"
)
#foods[2] = "corn"
foods = ("coleslaw", "corn", "mixed vegatables", "rice", "fruit cocktail")
for food in foods:
    print(food)

#4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/ dev/peps/pep-0008/. You won’t use much of it now, but it might be interesting to skim through it.
print(f"{lineBreak} 4.14 {lineBreak}")
print("No output expected")
'''
4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8:
• Use four spaces for each indentation level. Set your text editor to insert four spaces every time you press tab, if you haven’t already done so (see Appendix B for instructions on how to do this).
• Use less than 80 characters on each line, and set your editor to show a vertical guideline at the 80th character position.
• Don’t use blank lines excessively in your program files.
'''
print(f"{lineBreak} 4.15 {lineBreak}")
print(
    "This is something that needs to be done on an IDE, not on replit. If you go into replit settings for indent type, it will automatically update all tab spacing."
)
'''
Pair programming video
-two roles: driver (code writer) and navigator(bug checking, edge case consideration)
-roles switch
-helpful for newer people in org
'''
