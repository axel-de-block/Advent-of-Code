from datetime import datetime
startTime = datetime.now()

with open("TextInputs\\day05.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
        
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

seeds = [int(i) for i in lines[0].split(": ")[1].split()]
seeds = [[seeds[i], seeds[i]+seeds[i+1]-1] for i in range(0, len(seeds)-1, 2)]

def createTranslationLayer(listOfInstructions: list, layer = None) -> dict: 
    if not layer:
        layer = {}
    for line in listOfInstructions:
        line = [int(i) for i in line.split()]
        layer.update({(line[1], line[1]+line[2]-1):line[0]})
    return layer

#splits seed into two seeds if the content of fit into two different translation layers
def refactorSeeds(layer:dict) -> list:
    global seeds
    for i, seed in enumerate(seeds):
        for key in layer.keys():
            if key[0]<=seed[0]<=key[1]:
                if not key[0]<=seed[1]<=key[1]:
                    seeds[i] = [seed[0], key[1]]
                    seeds.insert(i+1, [key[1]+1,seed[1]])

def operateOnSeeds(layer) -> None:
    global seeds
    for i, seed in enumerate(seeds):
        for key in layer.keys():
            movement = layer[key] - key[0]
            if key[0]<=seed[0]<=key[1]:
                seeds[i][0] = seed[0] + movement
                seeds[i][1] = seed[1] + movement
                break

beginIndex = 3
for i, line in enumerate(lines[2:]):
    if "map" in line:
        beginIndex = i+3
        continue
    if line == '' or line == lines[-1]:
        endIndex = i+2 + 1*(line == lines[-1])
        layer = createTranslationLayer(lines[beginIndex:endIndex])
        refactorSeeds(layer)
        operateOnSeeds(layer)
        
print(f"A minumum of {min([i[0] for i in seeds])} from {seeds}.")
print((datetime.now()-startTime)/1000)