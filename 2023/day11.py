import numpy as np

with open("TextInputs\\day11.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""
   
lines = np.array([list(line) for line in lines])

listOfGalaxies = [] #tuples of indexs of galaxies
listOfDistances = []
grownRows = [] #list of row indexes that are bigger than they appear in the image
grownColumns = [] #list of column indexes that are bigger than they appear in the image
rateOfExpansions = 999_999 #I'm a genius, imagine appending new lines :kek:

#used to check for empty rows and columns
for i in range(len(lines[0])):
    if np.count_nonzero(lines[ :,i] == "#") == 0:
        grownColumns.append(i)
    if np.count_nonzero(lines[i] == "#") == 0:
        grownRows.append(i)
        continue

#looks for all galaxy locations
for y, line in enumerate(lines):
    for x, value in enumerate(line):
        if value == "#":
            listOfGalaxies.append((x, y))

#parses through all possible combinations of galaxies to calculate distance
upperLimit = len(listOfGalaxies)           
for i, galaxy in enumerate(listOfGalaxies):
    for target in listOfGalaxies[i+1: upperLimit]:
        distance = abs(target[0]-galaxy[0])+abs(target[1]-galaxy[1])
        for row in grownRows:
            if row in range(min(target[1], galaxy[1]), max(target[1], galaxy[1])):
                distance += rateOfExpansions
        for column in grownColumns:
            if column in range(min(target[0], galaxy[0]), max(target[0], galaxy[0])):
                distance += rateOfExpansions
        listOfDistances.append(distance)

print(sum(listOfDistances))