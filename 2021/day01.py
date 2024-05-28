import aoc_lube

data = [int(i) for i in aoc_lube.fetch(2021, 1).split("\n")]

def part_one():
    n = 0
    
    for i in range(len(data)-1):
        if data[i]-data[i+1] < 0:
            n += 1
            
    return n

def part_two():
    n = 0
    
    for i in range(len(data)-3):
        sum_one = sum(data[i:i+3])
        sum_two = sum(data[i+1:i+4])
        
        if sum_two > sum_one:
            n += 1
    
    return n

print(part_one())
print(part_two())

#aoc_lube.submit(2021, 1, 1, part_one)
aoc_lube.submit(2021, 1, 2, part_two)