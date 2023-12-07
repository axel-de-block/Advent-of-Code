
with open("TextInputs\\day07.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

winnings = 0

combos = [[] for _ in range(7)]
sortedCombos = []

def typeOfHand(hand:list[int]) -> int:
    handSet = list(set(hand))
    if len(handSet) == 5: #high card
        return 0
    if len(handSet) == 1: #five of a kind
        return 6 
    if len(handSet) == 2:
        if hand.count(handSet[0]) in [1, 4]:
            return 5 #four of a kind
        return 4 #full house
    if len(handSet) == 3:
        if max(hand.count(handSet[0]), hand.count(handSet[1]), hand.count(handSet[2])) == 3:
            return 3 #thee of a kind
        return 2 #two of a kind
    return 1 #one of a kind  

for line in lines:
    skip = False
    hand, bid = line.split()
    hand = ["23456789TJQKA".index(i) for i in hand]
    combos[typeOfHand(hand)].append([hand, int(bid)])
               
i = 1
for group in combos:
    for item in sorted(group):
        winnings += i*item[1]
        i += 1
    
print(winnings)