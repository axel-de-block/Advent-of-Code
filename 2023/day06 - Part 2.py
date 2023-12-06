with open("TextInputs\\day06.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""
  
time = ""  
times = lines[0][lines[0].index(":")+1:].split()
for i in times:
    time += i
    
time = int(time)
    
distance = ""
distances = lines[1][lines[1].index(":")+1:].split()
for i in distances:
    distance += i
    
distance = int(distance)

lowerBound = 0
upperBound = time

for buttonDuration in range(time):
    if (time - buttonDuration)*buttonDuration > distance:
        lowerBound = buttonDuration
        upperBound = time-buttonDuration+1
        break
           
print(len(range(lowerBound, upperBound)))