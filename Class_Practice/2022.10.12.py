listA = ["Warsaw", "Kyoto", "Tokyo", "Sydney", "Florianopolis"]
listB = ["Denver", "Washington DC", "Minneapolis", "Santa Barbara", "Chicago"]
listC = ["pizza", "ramen", "biala", "burgers", "burritos"]
listD = ["english", "polish", "french", "japanese", "german"]
listE = ["star wars", "lord of the rings", "1984", "band of brothers", "the pacific"]
listF = ["coco curry", "that steakhouse i went to in brazil", "that kobe beef steakhouse in kobe", "that greek place i went to in sydney", "crave burgers"]
listG = ["andrew", "nick", "chris", "matt", "frank"]
listH = ["sup", "whats up", "what it do", "whats crackin", "yo"]

for item in range(0,5):
	print(f"In {listA[item]} and {listB[item]} I love to eat {listC[item]} while speaking {listD[item]} and enjoying {listE[item]} at {listF[item]} with {listG[item]} while saying {listH[item]} to people walking by.\n")
print("-------------------------------\n")
#iterate sequentially through lists
for item in range(0,5):
	print(f"In {listA[(item)%5]} and {listB[(item+1)%5]} I love to eat {listC[(item+1)%5]} while speaking {listD[(item+3)%5]} and enjoying {listE[(item+4)%5]} at {listF[(item+5)%5]} with {listG[(item+6)%5]} while saying {listH[(item+7)%5]} to people walking by.\n")

# 0-5 -> 0,1,2,3,4
# 1-6 -> 1,2,3,4,-1
# 2-7 -> 2,3,4,-1,-2
# 3-8 -> 3,4,-1,-2,-3
# 4-9 -> 4,-1,-2,-3,-4
# 5-10 -> -1,-2,-3,-4,-5
# 6-11 -> -2,-3,-4,0,1
# 7-12 -> -3,-4,0,1,2
# 8-13 -> -4,0,1,2,3
# #if -5, set i to 0