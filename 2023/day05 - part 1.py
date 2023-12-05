with open("TextInputs\\day05.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

seeds = [int(i) for i in lines[0].split(": ")[1].split()]

def createTranslationLayer(listOfInstructions: list, layer = None) -> dict: 
    if not layer:
        layer = {}
    for line in listOfInstructions:
        line = [int(i) for i in line.split()]
        layer.update({(line[1], line[1]+line[2]):line[0]})
    return layer

def operateOnSeeds(layer) -> None:
    global seeds
    for i, seed in enumerate(seeds):
        for key in layer.keys():
            movement = layer[key] - key[0]
            if key[0]<=seed<key[1]:
                seeds[i] = seed + movement

layer = createTranslationLayer(lines[3:5])

beginIndex = 3

for i, line in enumerate(lines[2:]):
    if "map" in line:
        beginIndex = i+3
        continue
    if line == '':
        endIndex = i+2
        layer = createTranslationLayer(lines[beginIndex:endIndex])
        operateOnSeeds(layer)
    if line == lines[-1]:
        layer = createTranslationLayer(lines[beginIndex:])
        operateOnSeeds(layer)
        
print(min(seeds))