import aoc_lube
from pprint import pp as pprint

data = aoc_lube.fetch(2023, 13).split("\n")

#with open("TextInputs\\testCases.txt", "r") as open_doc:
#    data = [line.replace("\n", "") for line in open_doc.readlines()]

puzzles = []

#splits each pattern into a seperate list for easier parsing later on
begin_index = 0
for i, line in enumerate(data):
    if line == "":
        end_index = i
        puzzles.append(data[begin_index:end_index])
        begin_index = i+1
        
puzzles.append(data[begin_index:])

vertical_counter = 0
horizontal_counter = 0

def part_one(puzzles: list[list[str]]) -> int:
    global vertical_counter; global horizontal_counter
    
    #vertical mirror scanning
    for puzzle in puzzles:
        for index in range(1, len(puzzle[0])-2):
            #if any line does not mirror, it returns false for the entire pattern
            if vertical_line_checker(index, puzzle):
                vertical_counter += index
                break
                
    #horizontal mirror scanning
        for index, line in enumerate(puzzle[:-1]):
            if line == puzzle[index+1]:
                if horizontal_line_checker(index+1, puzzle):
                    horizontal_counter += index+1
                    break
    
    return vertical_counter + 100*horizontal_counter

def part_two():
    return 1

#checks wether an index is a vertical mirror for the pattern
def vertical_line_checker(index:int, data: list[list[str]]) -> bool:
    lengthMirror = min(len(data[0])-index, index)

    if data[0][index-lengthMirror:index] != data[0][index:index+lengthMirror][::-1]:
        return False
    
    return True

def horizontal_line_checker(index:int, data: list[list[str]]) -> bool:
    lengthMirror = min(len(data)-index, index)
    
    if data[index-lengthMirror:index] != data[index:index+lengthMirror][::-1]:
        return False
    
    return True

print(part_one(puzzles))

#aoc_lube.submit(2023, 13, 1, part_one)