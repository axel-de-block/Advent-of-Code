
with open("TextInputs\\day09.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

lines = [[int(i) for i in line.split()] for line in lines]

dataPredictions = []
historyPredictions = []

def generateDifferences(history: list[int]) -> list[int]:
    differences = []   
    for i, value in enumerate(history[:-1]):
        differences.append(history[i+1]-value)  
    return differences

def predict(history: list[int], reducedHistory: list[int]) -> list[int]:
    history.append(history[-1]+reducedHistory[-1])
    history.insert(0, history[0]-reducedHistory[0])
    return history

for line in lines:
    histories = [line]
    while histories[-1].count(0) != len(histories[-1]): #generates list of extrapolations
        histories.append(generateDifferences(histories[-1]))
        
    for i in range(1, len(histories)):
        histories[-(i+1)] = predict(histories[-(i+1)], histories[-i])
    
    dataPredictions.append(histories[0][-1])
    historyPredictions.append(histories[0][0])

print(sum(dataPredictions), sum(historyPredictions))