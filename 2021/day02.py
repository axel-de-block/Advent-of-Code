import aoc_lube

data = aoc_lube.fetch(2021, 2).split("\n")

def part_one():
    horizontal = 0
    depth = 0
    
    for instruction in data:
        val = int(instruction[instruction.index(" ")+1:])
        instruct = instruction[:instruction.index(" ")]
        
        if instruct == "forward":
            horizontal += val
        elif instruct == "down":
            depth += val
        else:
            depth -= val
    
    return horizontal*depth

def part_two():
    horizontal = 0
    aim = 0
    depth = 0
    
    for instruction in data:
        val = int(instruction[instruction.index(" ")+1:])
        instruct = instruction[:instruction.index(" ")]
        
        if instruct == "forward":
            horizontal += val
            depth += aim*val
        elif instruct == "down":
            aim += val
        else:
            aim -= val
    
    return horizontal*depth

part_two()

#aoc_lube.submit(2021, 2, 1, part_one)
aoc_lube.submit(2021, 2, 2, part_two)