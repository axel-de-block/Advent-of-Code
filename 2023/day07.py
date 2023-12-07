
with open("TextInputs\\day07.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]
"""

winnings = 0

combos = [[] for _ in range(6)] #fives, fours, houses, threes, twos and ones
sortedCombos = []

#sorts hands in their respective category -> now I need a sorted of those categories 
for line in lines:
    skip = False
    hand, bid = line.split()
    hand = ["0123456789TJQKA".index(i) for i in hand]
    setHand = list(set(hand))
    if len(setHand) == 1: #five of a kind
        combos[5].append([hand, int(bid)])
    elif len(setHand) == 5: #high card
        continue
    elif len(setHand) == 4: #one of a kind
        combos[0].append([hand, int(bid)])
    elif max([hand.count(card) for card in hand]) == 4: #four of a kind
        combos[4].append([hand, int(bid)])
    elif len(setHand) == 2: #Full house
        combos[3].append([hand, int(bid)])
    elif max([hand.count(card) for card in hand]) == 3: #three of a kind
        combos[2].append([hand, int(bid)])
    else: #two of a kind
        combos[1].append([hand, int(bid)])    
        
for group in combos:
    sortedCombos.extend([i[1] for i in sorted(group)])

for i, num in enumerate(sortedCombos, 1):
    winnings += i*num
    
print(winnings)

#cheating

with open('TextInputs\\day07.txt') as f:
    data = f.read().splitlines()

data = [line.split() for line in data]
print(data)

cards = '2 3 4 5 6 7 8 9 T J Q K A'.split()
strength_dict = {card:index for index,card in enumerate(cards)}
sorted_hands = []
hand_types = [[] for _ in range(7)]

def find_hand_type(hand,hand_set):
    #5 of a kind
    if len(hand_set) == 1:
        return 6
    #1 pair
    elif len(hand_set) == 4:
        return 1
    #High card
    elif len(hand_set) == 5:
        return 0
    #4 of a kind
    elif max([hand.count(card) for card in hand]) == 4:
        return 5
    #Full house
    elif len(hand_set) == 2:
        return 4
    #3 of a kind
    elif max([hand.count(card) for card in hand]) == 3:
        return 3
    return 2

for info in data:
    hand = list(info[0])
    hand_set = set(hand)
    hand_types[find_hand_type(hand,hand_set)].append(info)
    
for hand_type in hand_types:
    print(sorted(hand_type,key=lambda info: [strength_dict[card] for card in info[0]]))
    sorted_hands.extend((sorted(hand_type,key=lambda info: [strength_dict[card] for card in info[0]])))

part1 = sum([index * int(info[1]) for index,info in enumerate(sorted_hands,1)])
print(part1)