
with open("TextInputs\\day02.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

possibleIDs = []

for line in lines:
    curID = line[5:line.index(":")]
    sets = [item.split(", ") for item in line[line.index(":")+2:].split("; ")]
    #print("Currently parsing:", sets)
    
    maxRGB = [0, 0, 0]
    
    for pull in sets:
        for color in pull:
            if "red" in color and int(color[:color.index("red")]) > maxRGB[0]:
                maxRGB[0] = int(color[:color.index("red")])
            if "green" in color and int(color[:color.index("green")]) > maxRGB[1]:
                maxRGB[1] = int(color[:color.index("green")])
            if "blue" in color and int(color[:color.index("blue")]) > maxRGB[2]:
                maxRGB[2] = int(color[:color.index("blue")])
    #print("Max rgb values:", maxRGB)
        
    if maxRGB[0] <= 12 and maxRGB[1] <= 13 and maxRGB[2] <= 14:
        possibleIDs.append(int(curID))
    
print(sum(possibleIDs))