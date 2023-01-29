#initial setup - global variables
Invite = [
    "Steve Harvey", "Steven Stamkos", "God", "Abe Lincoln", "Kanye West",
    "Paris Hilton"
]  #5th i
Song = [
    "Sun Roof", "22", "back in black", "Black Parade", "asap forever", "Betty",
    "Ner Gonna give you up"
]  #6th
Toppings = [
    "pepperoni", "sausage", "onions", "mushroom", "green pepper",
    "black olive", "ham", "bacon"
]  #7th

team_name = "Chaos"

#print(Invite)
#print(Song)
#print(Toppings)

#Gavin
print("Gavin's favorite guest is " + Invite[0])
print("Gavin's favorite song from the party is " + Song[4])
print("Gavin's favorite pizza topping is " + Toppings[0])
print("Welcome to team " + team_name + ", my teammates are Nick and Richard.")
VIP_g = ["Nikita Kucherov", "Josh Allen", "Stefon Diggs", "Margot Robbie"]

#Invite.append(VIP_g)
print(Invite, VIP_g)
masterList = Invite + VIP_g
print(masterList)

#Nick
print()
print(f"Nicks favorite invited person is {Invite[2]}")
print(f"and favorite song is {Song[5]}")
print(f"and topping {Toppings[2]}")
print(
    f"Welcome to the {team_name} party, we have Gavin, Richard and Nick here")

VIP_N = ["JO", "J.", "Keanu Reeves", "Clifford the average size dog"]
print(*Invite, *VIP_N)
print()

#Richard
print(
    f"Richard's favorites from the list are: {Invite[3]}, {Song[3]}, and {Toppings[0]}."
)
print(
    f"Welcome! My team is Team {team_name} and my teammates are: Nick, Gavin, and Richard."
)
vip_r = ["David Gilmour", "Gerard Way", "Mark Hammil", "John Williams"]
invite_backup = [
    "Steve Harvey", "Steven Stamkos", "God", "Abe Lincoln", "Kanye West",
    "Paris Hilton"
]
new_list_r = invite_backup[:]
for new in vip_r:
    new_list_r.append(new)
print(new_list_r)
print("\n")

print(*Invite, *VIP_N, *VIP_g, *vip_r, '\n')

print(
    f"At the party we will be serving pizza. The different toppings we will offer are: {Toppings}."
)
