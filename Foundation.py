import math #math.dist
def replaceBrack(x):
    x = x.replace("\n", "")
    x = x.replace("(", "")
    x = x.replace(")", "")
    x = x.replace("[", "")
    x = x.replace("]", "")
    return x

file1 = open("1.txt", "r")
#get zoo dimentions
line = (file1.readline())
zooDim = replaceBrack(line).split(",")
#get drone depot
line = (file1.readline())
droneDepot = replaceBrack(line).split(",")
#get battery capacity
line = (file1.readline())
batteryCap = replaceBrack(line)

# splits all of the lists, creates list of lists
def getPositions(line):
    delim = line.find("),(")
    foodStorages = list()
    while delim != -1:
        foodStorages.append(replaceBrack(line[0:delim]).split(","))
        line = line[delim + 2: len(line)- 1]
        delim = line.find("),(")

    delim = line.find("]")
    foodStorages.append(replaceBrack(line[0:delim]).split(","))
    return foodStorages
#gets food storage locations
line = file1.readline()
foodStorages = getPositions(line)
#gets animal enclosure locations
line = file1.readline()
while line.find("]") == -1:
    line = line + file1.readline()
line = line + file1.readline()
animalEnclosures = getPositions(line)

print(foodStorages, animalEnclosures)

# pi - priority | TD - total distance traveled
def score(pi, TD):
    weighted_sum = 0
    for priority_multiplier in pi:
        weighted_sum += priority_multiplier * 1000
    return weighted_sum  - TD

summedPrioH = 0.0
summedPrioC = 0.0
summedPrioO = 0.0
for i in range(len(animalEnclosures) - 1): #sums up the priority, grouped by diet (h,c,o)
    if animalEnclosures[i][4] == "h":
        summedPrioH += float(animalEnclosures[i][3])
    elif animalEnclosures[i][4] == "c":
        summedPrioC += float(animalEnclosures[i][3])
    else:
        summedPrioO += float(animalEnclosures[i][3])
print(summedPrioH)
print(summedPrioC)
print(summedPrioO)
