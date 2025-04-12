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

line = file1.readline()
print(getPositions(line))

line = file1.readline()
while line.find("]") == -1:
    line = file1.readline()
# pi - priority | TD - total distance traveled
def score(pi, TD):
    weighted_sum = 0
    for priority_multiplier in pi:
        weighted_sum += priority_multiplier * 1000
    return weighted_sum  - TD

