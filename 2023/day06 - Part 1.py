import numpy as np

"""
with open("TextInputs\\day06.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]


times, distances = [int(i) for i in lines[0][lines[0].index(":")+1:].split()], [int(i) for i in lines[1][lines[1].index(":")+1:].split()]

marginOfError = []

for i in range(len(times)):
    curRace = []
    for buttonDuration in range(times[i]):
        curIteration = (times[i] - buttonDuration)*buttonDuration
        if curIteration > distances[i]:
            curRace.append(curIteration)
    marginOfError.append(len(curRace))
    
print(np.prod(marginOfError))