'''
-all of the content in this chapter is already things I know from learning Java for my CS major
-the real challenge moving forward will be to use Python syntax versus my habits from Java
-for the rest of my notes, i'm going to complete the try-it-yourself exercises
'''

lineBreak = "----------"

#2.1 simple message - Assign a message to a variable, and then print that message.
print(f"{lineBreak} 2.1 {lineBreak}")
message21 = "simple message"
print(message21)

#2.2 simple messages - Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message
print(f"{lineBreak} 2.2 {lineBreak}")
message22 = "first print"
print(message22)
message22 = "second print"
print(message22)

#2.3 personal message - Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
print(f"{lineBreak} 2.3 {lineBreak}")
firstName = "Paul"
print(f"Hello {firstName}, would you like to learn some Python today?")

#2.4 name cases - Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
print(f"{lineBreak} 2.4 {lineBreak}")
print(firstName.lower())
print(firstName.upper())
print(firstName.title())

#2.5 famous quote - Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
print(f"{lineBreak} 2.5 {lineBreak}")
print("Yoda once said, \"Do or do not, there is no try.\""
      )  # using \ as an escape character, similar to Java

#2.6 famous quote 2 - Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
print(f"{lineBreak} 2.6 {lineBreak}")
famPerson = "Yoda"
print(f"{famPerson} once said, \"Do or do not, there is no try.\"")

#2.7 stripping names - Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
print(f"{lineBreak} 2.7 {lineBreak}")
stripName = "  \t Strippin  \n"
print(stripName)
print(stripName.lstrip())
print(stripName.rstrip())
print(stripName.strip())
'''
#2.8 number eight - Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this: 
-----------------------
print(5+3)  
-----------------------
Your output should simply be four lines with the number 8 appearing once on each line.
'''
print(f"{lineBreak} 2.8 {lineBreak}")
print(3 + 5)
print(16 / 2)
print(4 * 2)
print(10 - 2)

#2.9 favorite number - Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.
print(f"{lineBreak} 2.9 {lineBreak}")
favNum = 4
print(f"My favorite number is {favNum}.")

#2.10 adding comments
print(f"{lineBreak} 2.10 {lineBreak}")
print(f"reference all previous title heads in these notes")

#2.11 zen of python - Enter 'import this' into a Python terminal session and skim through the additional principles.
print(f"{lineBreak} 2.11 {lineBreak}")
import this
'''
VIDEO NOTES

hello world video
-python is an interpreted language, not a compiled language (like Java)
-python executes code line-by-line rather than be compiled, and executed
-don't like the indentation to create code blocks - seems like readability might be a little more difficult
-functions? this must be the python version of 'methods' from Java

variables/expressions
-sequence types have lists, tuples, dictionaries
-lists in python are like arrays, however it seems that these can hold more than one data type within
-tuple is also like an array in that: immutable, ordered, can have repeated values, contain multiple data types, but values cannot be removed
-wow, so variables that have been previously declared can be redeclared as a different type with no warning or error message....that's totally not going to cause bugs to get hidden deep into complicated programs that efficiently reuse variables.....
-ok so sequence types work like Java when accessing specific values with the index [i]
-slices
print(someList[start:end])
print(list[start:end:skip])
print(list[::-1]) -prints list in reverse order
-dictionaries are like Java: key -> value
-concatenation does not work in python like it does work in Java
System.out.println("string type " + 123); -this WILL print in Java
print("string type " + 123) -this WILL NOT work in python :: need to use print("string type " + str(123))
-for local/global variables, the example is good to illustrate the concept but you should NEVER DO THIS - HIDES BUGS
-'del' can delete variables
'''
