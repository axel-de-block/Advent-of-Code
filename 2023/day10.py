
with open("TextInputs\\day10.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

lines = [list(line) for line in lines]

pipeDirections = {"F": ["RIGHT", "DOWN"], "|": ["UP", "DOWN"], "L": ["UP", "RIGHT"], "-":["LEFT", "RIGHT"], "J":["LEFT",  "UP"], "7":["DOWN", "LEFT"], "S":["UP", "DOWN", "LEFT", "RIGHT"]}
movement = {"UP": [0, -1], "DOWN": [0, 1], "LEFT": [-1, 0], "RIGHT": [1, 0]}
sTranslation = {0:"F", 1:"J", 2:"F", 3:"L", 4:"|", 5:"-"}
sTransList = [[[-1,0],[0,1]], [[-1,0],[0,-1]], [[1,0],[0,1]], [[1,0],[0,-1]], [[0,1],[0,-1]], [[1,0],[-1,0]]]
mazeTrack = []

#gets the two pipes connected to the current pipe, ignores the one you just came from and returns the new one
#uses movement x and y values to adjust current x and y
#no need to check if it's a valid connection since it's a guaranteed loop
def getConnectingPipe(x: int, y: int, currentPipe: str) -> list[int]:
    global lines
    global mazeTrack
    global pipeDirections
    global movement
    
    directions = [movement[direction] for direction in pipeDirections[currentPipe]]
    
    for direction in directions:
        if [x+direction[0], y+direction[1]] not in mazeTrack:
            return [x+direction[0], y+direction[1]]

#quick way to get the sort of pipe at location
def getPipe(cood: list[int]) -> str:
    global lines
    return lines[cood[1]][cood[0]]

for y, line in enumerate(lines):
    if "S" in line:
        x = line.index("S")
        mazeTrack.append([x, y])
        
        #this shitshow chooses the first connected pipe to S and returns it as next pipe so we can get started looping
        #need to find a way to put this into getConnectingPipes without making it look just as fucked up
        if lines[max(y-1, 0)][x] in ["|", "7", "F"] and [x, max(y-1, 0)] not in mazeTrack:
            mazeTrack.append([x, y-1])
            break
        if lines[y][max(x-1, 0)] in ["-", "F", "L"] and [max(x-1, 0), y] not in mazeTrack:
            mazeTrack.append([x-1, y])
            break
        if lines[min(y+1, len(lines)-1)][x] in ["|", "J", "L"] and [x, min(y+1, len(lines)-1)] not in mazeTrack:
            mazeTrack.append([x, y+1])
            break
        if lines[y][min(x+1, len(lines[0])-1)] in ["-", "J", "7"] and [min(x+1, len(lines[0])-1), y] not in mazeTrack:
            mazeTrack.append([x+1, y])
            break

while True:
    curX, curY = mazeTrack[-1]
    newPipe = getConnectingPipe(curX, curY, getPipe(mazeTrack[-1]))
    if newPipe is None: #this will occur when the loop is complete as the above functions returns None if both connections are in the track already
        break
    mazeTrack.append(newPipe)

#replace S with the actual pipe -> needed for contour checking  
#part 2 starts here  
sMovement = [[mazeTrack[1][0]-mazeTrack[0][0], mazeTrack[1][1]-mazeTrack[0][1]], [mazeTrack[-1][0]-mazeTrack[0][0], mazeTrack[-1][1]-mazeTrack[0][1]]]

if sMovement in sTransList:
    sReplacer = sTranslation[sTransList.index(sMovement)]
else:
    sMovement.reverse()
    sReplacer = sTranslation[sTransList.index(sMovement)]

lines[mazeTrack[0][1]][mazeTrack[0][0]] = sReplacer

insideCounter = 0

#print(type(lines[1][9]))

for y, line in enumerate(lines):
    for x, value in enumerate(line):
        boundariesCrossed = 0
        contourCheck = False
        if [x, y] in mazeTrack:
            continue
        
        for i in range(len(line)-x):
            #print(f"{getPipe([x, y])} @ {[x, y]} with {boundariesCrossed} crossings @ {getPipe([x+i, y])}")
            #print(contourCheck)
            if [x+i, y] in mazeTrack and getPipe([x+i, y]) != "-":
                if getPipe([x+i, y]) == "F":
                    contourCheck = "F"
                    #print(f"Contour starting with {getPipe([x+i, y])} @ {[x+i, y]}")
                    continue
                if getPipe([x+i, y]) == "L":
                    contourCheck = "L"
                    #print(f"Contour starting with {getPipe([x+i, y])} @ {[x+i, y]}")
                    continue
                if contourCheck == "F" and (getPipe([x+i, y]) == "7"):
                    #print(f"{getPipe([x+i, y])}")
                    contourCheck = False
                    #print(f"Contour ending with {getPipe([x+i, y])} @ {[x+i, y]}")
                    continue
                if contourCheck == "L" and getPipe([x+i, y]) == "J":
                    contourCheck = False
                    #print(f"Contour ending with {getPipe([x+i, y])} @ {[x+i, y]}")
                    continue
                contourCheck = False 
                
                boundariesCrossed +=1
                
            
        if boundariesCrossed%2 != 0:
            #print(getPipe([x, y]), [x, y])
            insideCounter += 1

print(int(len(mazeTrack)/2), insideCounter)