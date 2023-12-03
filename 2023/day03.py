import numpy as np
from pprint import pprint

with open("TextInputs\\day03.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

symbols = ['*', '$', '/', '=', '+', '@', '-', '%', '&', '#']

numbers = []
gears = {}
sumNumbers = 0

#object used to define search boundaries
class number:
    def __init__(self, num, xLeft, xRight, y) -> None:
        self.num = int(num)
        self.y = y
        self.xLeft = xLeft
        self.xRight = xRight

#step 1 -> get all numbers out of the lines
#step 2 -> when obtaining numbers make sure to get it's coordinates and attach them to this number via a class
#step 3 -> iterate over every number and check vicinity in lines

#grabs all numbers and their coordinates
for i, line in enumerate(lines):
    curNum = ""
    xLeft = 0
    for x, letter in enumerate(line):
        if letter.isdigit() and curNum == "": #start datacollection for a new number
            curNum+=letter
            xLeft=x
        elif letter.isdigit():
            curNum+=letter
            if x == len(line)-1: #required if the number ends on the last digit of a line
                numbers.append(number(curNum, xLeft, x+1, i))
                curNum=""
        elif not letter.isdigit() and curNum != "":
            numbers.append(number(curNum, xLeft, x, i))
            curNum=""

#iterates over lines to check vicinity using slicing (max and mins are for numbers that are on the edge of the list)    
for num in numbers:
    stop = False
    slicedLines= []
    for line in lines[max(0, num.y-1):min(len(lines), num.y+2)]:
        if stop:
            break
        slicedLines.append(line[max(0, num.xLeft-1):min(len(line), num.xRight+1)])
    for i, slicedLine in enumerate(slicedLines):
        for sym in symbols:
            if sym in slicedLine:
                sumNumbers += num.num
                if sym == "*": #part 2
                    gearCood = str(min(num.y-(len(slicedLines)-2), len(lines)-2)+i) + "." + str(max(0,num.xLeft-1)+slicedLine.index("*")) #find the coordinates -> turn it into a identifier -> update dict based on id
                    if gearCood in gears:
                        gears.update({gearCood:gears[gearCood]+[num.num]})
                    else:
                        gears.update({gearCood:[num.num]})
                stop = True
                break

#part 2   
gearsSum = 0

for value in gears.values():
    if len(value) == 1:
        continue
    gearsSum += np.prod(value)
            
print(sumNumbers, gearsSum)