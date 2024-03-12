from math import floor

with open("TextInputs\\day01.txt", "r") as open_doc:
    lines = [int(line.replace("\n", "")) for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

totalFuel = 0
totalFuelExtra = 0

for line in lines:
    newFuel = floor(line/3)-2
    totalFuel += newFuel
    while True:
        newFuel = floor(newFuel/3)-2
        if newFuel < 0:
            break
        totalFuelExtra += newFuel
    
print(totalFuel, totalFuelExtra+totalFuel) #part 1, part 2