print("--------------------11.30.2022 LAB------------------------")
class Player:
	'''player class - contains name and results'''
	def __init__(self, name, results):
		self.name = name
		self.results = results


def add_to_file(file):
	'''add player to file'''
	with open(file, "w") as f:
		name = input("Enter player name: ")
		results = input("Enter player score: ")
		#player = Player(name, result)
		f.write(f"{name} : {results}")


def read_file(file):
	'''print contents of file to screen'''
	with open(file, "r") as f:
		for line in f:
			print(line)

results = open("results.txt", "w")  #create file
#player1 = Player("player_one", "1st place")  #create player
add_to_file("results.txt")  #add player to file
read_file("results.txt")  #print file
results.close()  #close file

##################MY TEAM########################
team_file = open("myteam.txt", "w")
team = ["richard", "gavin", "nick"]
def add_to_file2(file, list):
	'''add member to file'''
	for name in list:
		file.write(f"{name}")
add_to_file2("myteam.txt", team)
read_file(team_file)

'''
#Creates the files, and reads it.
def file_read(fname):
        with open(fname, "w") as myfile:
                myfile.write("My Team Members Are: \n")
                myfile.write("Kyle, Samantha, Alex, Tom \n")
        txt = open(fname)
        print(txt.read())
file_read('myteam.txt')

#Repeating, and adding Joanna - we could also just open and edit the file.
def file_read(fname):
        with open(fname, "w") as myfile:
                myfile.write("My Team Members Are Now: \n")
                myfile.write("Kyle, Samantha, Alex, Tom, Joanna \n")
        txt = open(fname)
        print(txt.read())
file_read('myteam.txt')

#Who Has The Longest Name?
def longest_word(fname):
    with open(fname, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print ("The Longest Name Is:")
print(longest_word('myteam.txt'))



#Read the file and store it in a variable
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print("The Data Variable Holding All File Contents Reads:")
                print(data)
file_read('myteam.txt')
'''