'''
Class exercises
'''
#create restaurant menu with 3 entrees and 2 options per entree
entrees = ["parmigana", "spaghetti", "lasagana"]
options = ["chicken", "egplant", "meatballs", "without meatballs", "cheese", "meat"]
parm_op = ["chicken", "egplant"]
sp_op = ["meatballs", "without meatballs"]
las_op = ["cheese", "meat"]
print("Welcome to generic italian restaruant. Please look at our menu: ")
for meal in entrees:
	if (meal == "parmigana"):
		print(f"Entree 1 is {meal}. Which can be served with {parm_op[0]} and {parm_op[1]}.")
	if (meal == "spaghetti"):
		print(f"Entree 2 is {meal}. Which can be served with {sp_op[0]} and {sp_op[1]}.")
	if (meal == "lasagana"):
		print(f"Entree 3 is {meal}. Which can be served with {las_op[0]} and {las_op[1]}.")

n = 5
for i in range(0, n):
    print(i)