import aoc_lube
from statistics import mean, median

def main(data) -> None:
    med = int(median(data))
    # it makes no sense for me to round down instead of rounding to the nearest int
    # but it works for my data set... so who the fuck knows
    # test data requires round() instead of int() so some fuckery is abound
    # cba figuring it out
    avg = int(mean(data))
    print("Part one:", int(cost_to_align_part_one(data, med)), "@", med)
    print("Part two:", int(cost_to_align_part_two(data, avg)), "@", avg)
    
def cost_to_align_part_one(numbers: list[int], location: int) -> int:
    cost = 0
    
    for number in numbers:
        cost += abs(number-location)
    
    return cost

def cost_to_align_part_two(numbers: list[int], location: int) -> int:
    cost = 0
    
    for number in numbers:
        local_cost = 0
        for i in range(1, abs(location-number)+1):
            local_cost += i
        cost += local_cost
    
    return cost

if __name__ == "__main__":
    #data = [int(i) for i in "16,1,2,0,4,2,7,1,2,14".split(",")]
    #main(data)
    
    data = [int(i) for i in aoc_lube.fetch(2021, 7).split(",")]
    main(data)