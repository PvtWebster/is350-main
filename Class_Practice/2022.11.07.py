#1. Write a Python function to find the Max of three numbers. Go to the editor
def find_max(list):
	max = list[0]
	for i in list:
		if i > max:
			max = i
	return print(f"max = {max}")

list = [1,2,3,4,5,6,7,8,9,10]
find_max(list)

'''
2. Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''
def sum(list):
	total = 0
	for i in list:
		total = total + i
	return print(f"summation = {total}")
sum(list)

'''
3. Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''
def multiply(list):
	total = 1
	for i in list:
		total = total * i
	return print(f"multiply = {total}")
multiply(list)

'''
4. Write a Python program to reverse a string. Go to the editor
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''
def revStr(string):
	rev = string[::-1]
	print(f"original string = {string} : reversed string = {rev}")
	return rev

str = "ABCDEFG"
revStr(str)

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. Go to the editor
def factorial(int):
	if int <= 0:
		return print("error: integer is negative or 0")
	else:
		factor = 1
		for i in range(1,int):
			factor = factor * i

#6. Write a Python function to check whether a number falls in a given range. Go to the editor
