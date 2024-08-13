import aoc_lube
import numpy as np

data = aoc_lube.fetch(2021, 3).split("\n")

#print(data)

#data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

def part_one():
    counter = list(np.zeros(len(data[0])))
    
    for bin_num in data:
        for i, bit in enumerate(bin_num):
            if bit == "1":
                counter[i] += 1
            else:
                counter[i] -= 1
    
    gamma = ""
    
    for count in counter:
        if count < 0:
            gamma += "0"
        else:
            gamma += "1"
            
    #gamma and epsilon are always inverts of each other, so a quick flip is all that's required        
    epsilon = "".join('1' if bit == '0' else '0' for bit in gamma)        

    return int(gamma, base=2)*int(epsilon, base=2)

def part_two():
    oxygen = data
    carbon = data
    
    for i in range(len(data[0])):
        output = split_lists(oxygen, carbon, i)
        oxygen, carbon = output[0], output[1]
        print(oxygen)
        print(carbon)
        print(" --------- " + str(i))
        
    return int(oxygen[0], base=2)*int(carbon[0], base=2)

def split_lists(oxygen: list[str], carbon: list[str], index: int) -> tuple[list[str], list[str]]:
    if len(oxygen) == 1:
        oxygen_out = oxygen
    else:
        oxygen_out = split_list(oxygen, True, index)
    
    if len(carbon) == 1:
        carbon_out = carbon
    else:
        carbon_out = split_list(carbon, False, index)
    
    return (oxygen_out, carbon_out)

def split_list(data: list[str], bigger: bool, index: int) -> list[str]:
    zeroes = []
    ones = []
    counter = 0
    
    for bin_num in data:
        if bin_num[index] == "1":
            ones.append(bin_num)
            counter += 1
        else:
            zeroes.append(bin_num)
            counter -= 1
    
    #bit criteria is a head ache
    if bigger:
        if counter >= 0:
            return ones
        else: 
            return zeroes
    else:
        if counter < 0:
            return ones
        else: 
            return zeroes
            
part_two()
      
#aoc_lube.submit(2021, 3, 1, part_one)
#aoc_lube.submit(2021, 3, 2, part_two)

def remove_elem_from_list(list_nums: list[int], elem: int):
    limit = len(list_nums)
    i = 0
    removed_nums = 0
    while True:
        if i >= limit-removed_nums:
            return i
        
        if list_nums[i] != elem:
            i += 1
            continue
        
        list_nums[i], list_nums[-(1+removed_nums)] = list_nums[-(1+removed_nums)], list_nums[i]
        removed_nums += 1
        
list_nums = [1, 4, 7, 2, 3, 5, 7, 2, 3, 2]
print(list_nums)

remove_elem_from_list(list_nums, 7)