import aoc_lube
import numpy as np

from pprint import pp as pretty

# list comprehensions are love, list comprehensions are life
# converts raw data string into lists of couples forming start and end coordinate
data = [[[int(number) for number in couple.split(",")] for couple in i.split(" -> ")] for i in aoc_lube.fetch(2021, 5).split("\n")]
#data = [[[0, 9], [5, 9]], [[8, 0], [0, 8]], [[9, 4], [3, 4]], [[2, 2], [2, 1]], [[7, 0], [7, 4]], [[6, 4], [2, 0]], [[0, 9], [2, 9]], [[3, 4], [1, 4]], [[0, 0], [8, 8]], [[5, 5], [8, 2]]]

grid = np.zeros((1000, 1000))

for group in data:
    # checking horizontals
    if group[0][0] == group[1][0] and not group[0][1] == group[1][1]:
        for i in range(min(group[0][1], group[1][1]), max(group[0][1], group[1][1])+1):
            grid[i][group[0][0]] += 1
    # checking verticals
    elif group[0][1] == group[1][1] and not group[0][0] == group[1][0]:
        for i in range(min(group[0][0], group[1][0]), max(group[0][0], group[1][0])+1):
            grid[group[0][1]][i] += 1
    # checking diagonals
    else:
        one = group[0]
        two = group[1]
        for i in range(abs(one[0]-two[0])+1):
            x_coord = one[0]+i*((-1)**(one[0] > two[0]))
            y_coord = one[1]+i*((-1)**(one[1] > two[1]))
            grid[y_coord][x_coord] += 1
        
# complicated way to count all non zeroes?
answer_part_one = sum([1 for x in np.nditer(grid) if x >= 2])

print(answer_part_one)    