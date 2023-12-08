from math import lcm
from functools import reduce

with open("TextInputs\\day08.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

instruct = {"L": 0, "R": 1}
instructionSet = lines[0]
nodes = {}
currentNodes = []
steps = 0
stepsLCM = {}
end = False

class map:
    def __init__(self, label, destinations):
        self.label = label
        left, right = destinations.replace("(", "").replace(")", "").split(", ")
        self.left = left
        self.right = right        
    def __repr__(self):
        return f"{self.label} -> {self.left} or {self.right}"

for line in lines[2:]:
    nodeName, nodeDestinations = line.split(" = ")
    nodes.update({nodeName:map(nodeName, nodeDestinations)})
    if nodeName[2] == "A":
        currentNodes.append(nodes[nodeName])

while True:
    direction = instruct[instructionSet[steps%len(instructionSet)]]
    
    for i, currentNode in enumerate(currentNodes):
        if direction:
            currentNodes[i] = nodes[currentNode.right]
        else:
            currentNodes[i] = nodes[currentNode.left]
    steps += 1  
    
    
    for currentNode in currentNodes:
        if currentNode.label[2] == "Z" and currentNodes.index(currentNode) not in stepsLCM:
            stepsLCM.update({currentNodes.index(currentNode):steps})
                
    if len(stepsLCM) == len(currentNodes):
        break
    
print(stepsLCM)
    
print(reduce(lcm, [value for value in stepsLCM.values()]))