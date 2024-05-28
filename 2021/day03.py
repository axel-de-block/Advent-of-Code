import aoc_lube
import numpy as np

data = aoc_lube.fetch(2021, 3).split("\n")

print(data)

def part_one():
    counter = list(np.zeros(len(data[0])))
    
    for bin in data:
        for i, bit in enumerate(bin):
            if bit == "1":
                counter[i] += 1
            else:
                counter[i] -= 1
    
    gamma = ""
    epsilon = ""
    
    for count in counter:
        if count < 0:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    
    return int(gamma, base=2)*int(epsilon, base=2)

def part_two():
    pass
        
#aoc_lube.submit(2021, 3, 1, part_one)