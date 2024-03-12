with open("TextInputs\\day03.txt", "r") as open_doc:
    lines = [line.replace("\n", "").split(",") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "").split(",") for line in open_doc.readlines()]
"""

wires = [{}, {}] #checking existence in a dictionary is O(1) in dicts vs O(n) in lists

for i, line in enumerate(lines):
    x, y = 0, 0
    
    n = 0
    
    for direction in line:
        #print(f"Iterating over {direction} -> length of lists is now {len(wires[0])} and {len(wires[1])}")
        
        directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
        dir = directions[direction[0]]
        for _ in range(int(direction[1:])):
                n += 1
                x += dir[0]
                y += dir[1]
                wires[i][(x, y)] = n
                
intersections = {}  
distances = [(abs(distance[0]) + abs(distance[1]), wires[0][distance]+wires[1][distance]) for distance in wires[0] if distance in wires[1]]
   
print(f"Part 1: {min(distances, key=lambda x: x[0])[0]} | Part 2: {min(distances, key=lambda x: x[1])[1]}")