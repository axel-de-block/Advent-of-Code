import aoc_lube    
import numpy as np

class BingoCard:
    def __init__(self, cardRows) -> None:
        rows = [cr.replace('  ', ' ').split(' ') for cr in cardRows]
        self.grid = np.array(rows, dtype = int)

    def markCard(self, number):
        self.grid[self.grid == number] = -1

    def getScore(self, lastCalled):
        return np.sum((self.grid != -1) * self.grid) * lastCalled

    def isWinner(self):
        if any(np.sum(self.grid, axis=0) == -5):
            return True
        if any(np.sum(self.grid, axis = 1) == -5):
            return True
        return False

# read numbers in first line, and remove the lines from the dataset
lines = [i.strip() for i in aoc_lube.fetch(2021, 4).split("\n")] 
numbers = [int(x) for x in lines[0].strip().split(',')]
lines = lines[2:]

# read bingo cards
# each bingo card represents a 5x5 grid of numbers
bingoCards = [BingoCard(lines[i*6:i*6+5])for i in range(0, len(lines) // 6)]

# run the bingo game
scores = []
for number in numbers:
    # mark all the cards
    [card.markCard(number) for card in bingoCards]
    # find all the winner cards and remove them 
    scores += [card.getScore(number) for card in bingoCards if card.isWinner()]
    bingoCards = [card for card in bingoCards if not card.isWinner()]
    
print('part 1:', scores[0])
print('part 2:', scores[-1])