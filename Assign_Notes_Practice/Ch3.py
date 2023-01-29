'''
-lists, or arrays as i would call them, seem to overall function in the same way
-they have an index, which also starts at zero, and values are also accessed the same way: list[0]
-unlike Java, a complete list can be printed without using a loop with one print statement
-the last item of a list can be accessed with index [-1], which in Java would be an OutOfBoundsException. this continues, so the penultimate item is accessed with [-2], the next [-3], etc
'''

lineBreak = "----------"

#3.1 names - Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
print(f"{lineBreak} 3.1 {lineBreak}")
names = ["matt", "andrew", "frank", "chris"]
for name in names:
    print(f"{name.title()}")

#3.2 greetings - Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
print(f"{lineBreak} 3.2 {lineBreak}")
for name in names:
    print(f"{name.title()} is my friend.")

#3.3 your own list - Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
print(f"{lineBreak} 3.3 {lineBreak}")
modeTrans = [
    "I really enjoyed the subway/metro system in Tokyo.",
    "I do enjoying driving my Nissan.",
    "My most/least liked mode of transport is flying."
]
for mode in modeTrans:
    print(mode)
'''
-after reading more, it seems that lists are more alike to ArrayList rather than a primative array. methods like append(), insert(), and remove() all act like ArrayList methods: no elements shifting or array resizing is required - it's dynamic
-lists seem to, like arrays, prefer to work with items at the beginning and end
-pop() is a straight up Stack method, HOWEVER, you can specifiy the index you want to pop. this somewhat goes against the intention of pop()
-remove() will search the list for the value to remove, but after testing it will not remove ALL values (if there are repeated values) (NOTE on pg 42 mentions this)
'''

#3.4 guest list - If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
print(f"{lineBreak} 3.4 {lineBreak}")
invite = ["Mark Hammil", "John Williams", "Ewan McGregor"]
for person in invite:
    print(f"{person.title()}, I would like to invite you for dinner.")
'''
#3.5 changing guest list - You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
'''
print(f"{lineBreak} 3.5 {lineBreak}")
print("John Williams cannot make it.")
invite.remove(invite[1])  #invite.remove("John Williams")
invite.append("Carrie Fisher")
for person in invite:
    print(f"{person.title()}, I would like to invite you for dinner.")
'''
#3.6 more guests - You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''
print(f"{lineBreak} 3.6 {lineBreak}")
print("A larger dinner table has been successfully reserved.")
invite.insert(0, "Christopher Lee")  #beginning
invite.insert(2, "Samuel L. Jackson")  #middle
invite.append("George Lucas")  #end
for person in invite:
    print(f"{person.title()}, I would like to invite you for dinner.")
'''
#3.7 shrinking guest list - You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
'''
print(f"{lineBreak} 3.7 {lineBreak}")
print(
    "The larger dinner table will not be available in time for the start of dinner, so there is only space for two guests."
)
while (len(invite) > 2):
    print(
        f"Apologies {invite.pop()}, we cannot invite you for dinner tonight.")
for person in invite:
    print(f"{person.title()}, you are still invited for dinner tonight.")
while (len(invite) > 0):
    del invite[0]
print(invite)
'''
-python sorts lists with sort() and reverse()
-how does python sort words/strings that are lower vs uppercase?
-also, how does python sort a list containing different data types, for example ["one", 1.0, 1, "One", "One point zero", 1/1]
'''

#3.8 seeing the world - Think of at least five places in the world you’d like to visit.
print(f"{lineBreak} 3.8 {lineBreak}")
#Store the locations in a list. Make sure the list is not in alphabetical order.
visit = ["south korea", "france", "germany", "uk", "italy"]
#Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(visit)
#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(visit))
#Show that your list is still in its original order by printing it.
print(visit)
#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(
    sorted(visit, reverse=True)
)  #this DOES sort the list in reverse alphabetically - just using 'reverse()' will simply mirror the unsorted list
#Show that your list is still in its original order by printing it again.
print(visit)
#Use reverse() to change the order of your list. Print the list to show that its order has changed.
visit.reverse()
print(visit)
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
visit.reverse()
print(visit)
#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
visit.sort()
print(visit)
#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
visit.sort(reverse=True)
print(visit)

#3.9 dinner guests - Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.
print(f"{lineBreak} 3.9 {lineBreak}")
print(
    f"3.7 asks us to remove all values from the invitation list used in exercises 3.4-3.7. Adding values back is too much work; therefore, I will provide the length for the country list from 3.8 which equals {len(visit)}."
)

# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
print(f"{lineBreak} 3.10 {lineBreak}")
threeTen = []
print(threeTen)
threeTen.append("first")
print(threeTen)
threeTen.insert(0, "second")
print(threeTen)
threeTen.append("third")
print(threeTen)
threeTen.sort()
print(threeTen)
threeTen.sort(reverse=True)
print(threeTen)
print(f"length = {len(threeTen)}")
threeTen.pop()
print(threeTen)
threeTen.remove("second")
print(threeTen)
del threeTen[0]
print(threeTen)

#3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.
print(
    f"{lineBreak} 3.11 {lineBreak}\nAn Error is expected below for purposes of this exercise\n|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t|\t")
print(visit[5])  #IndexError: list index out of range
'''
VIDEO notes
-"Flipped Classroom" video was viewed in class
-"python lists video" notes
-there is a list constructor 'list.()' to build lists; research this later
-order matters in lists, unlike sets
-negative indicies only loop once, for list[0,1,2,3]: list[-4]=0 BUT list[-5]=indexOutOfBoundsException
-spliting list via index work by list[startIndex:endIndex] NOTE 'startIndex' is INCLUSIVE BUT 'endIndex' is EXCLUSIVE
-lists can be concatenated: list + list = newList
-dir() function will list what methods can be used with the object inside the (). so dir(someList) will provide a list of methods usable on lists. the help() methods will provide a brief description of that method. EX help(someList.reverse) will provide documentation on the reverse method for lists
'''
