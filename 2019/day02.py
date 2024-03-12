from copy import deepcopy

with open("TextInputs\\day02.txt", "r") as open_doc:
    lines = [int(i) for i in open_doc.readline().replace("\n", "").split(",")]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [int(i) for i in open_doc.readline().replace("\n", "").split(",")]
"""

def intCodeParser(lines: list[int], noun: int, verb: int) -> int:

    lines[1], lines[2] = noun, verb

    pointer = 0
    while True:
        if lines[pointer] == 99:
            return lines[0]
        
        if lines[pointer] == 1:
            lines[lines[pointer+3]] = lines[lines[pointer+1]]+lines[lines[pointer+2]]
        elif lines[pointer] == 2:
            lines[lines[pointer+3]] = lines[lines[pointer+1]]*lines[lines[pointer+2]]
        
        pointer += 4

def intCodeNounVerb(lowerLimit: int, upperLimit: int, target: int) -> int:
    for noun in range(lowerLimit, upperLimit):
        for verb in range(lowerLimit, upperLimit):
            if intCodeParser(deepcopy(lines), noun, verb) == target:
                return 100* noun + verb
  
print(intCodeParser(deepcopy(lines), 12, 2)) #part 1
print(intCodeNounVerb(0, 100, 19690720)) #part 2