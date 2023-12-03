
with open("TextInputs\\day03.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

symbols = ['*', '$', '/', '=', '+', '@', '-', '%', '&', '#']

numbers = []
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
        if letter.isdigit() and curNum == "":
            curNum+=letter
            xLeft=x
        elif letter.isdigit():
            curNum+=letter
        elif not letter.isdigit() and curNum != "":
            numbers.append(number(curNum, xLeft, x, i))
            curNum=""

#iterates over lines to check vicinity using slicing (max and mins are for numbers that are on the edge of the list)    
for num in numbers:
    stop = False
    print(f"Now analyzing {num.num} on line {num.y}")
    for line in lines[max(0, num.y-1):min(len(lines)-1, num.y+2)]:
        if stop:
            break
        slicedLine = line[max(0, num.xLeft-1):min(len(line), num.xRight+1)]
        print(slicedLine)
        for sym in symbols:
            if sym in slicedLine:
                sumNumbers += num.num
                print(f"Appending {num.num} on line {num.y} because {sym} was found.")
                stop = True
                break
    print("--------------------------------")
            
print(sumNumbers)