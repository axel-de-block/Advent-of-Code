from math import floor

with open("TextInputs\\day04.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""


points = 0

cards = []

for line in lines:
    cards.append(line[line.index(":")+2:].split(" | "))

cardsQuantity = [1]*len(lines) #part 2

def removeEmpty(list: list) -> list: 
    while "" in list:
        list.remove("")
    return list

for i, card in enumerate(cards):
    curPoints = 0.5
    matchingNumbers = 0
    winningNumbers = removeEmpty(card[0].split(" "))
    potentialNumbers = removeEmpty(card[1].split(" "))
    for number in winningNumbers:
        if number in potentialNumbers:
            curPoints *= 2
            cardsQuantity[i+matchingNumbers+1] += cardsQuantity[i]
            matchingNumbers += 1

    points += int(floor(curPoints))

print(cardsQuantity)
print(points, sum(cardsQuantity))