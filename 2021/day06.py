import aoc_lube

# using a hashmap is infinitly faster than simulating individual fish, holy smokes
def main() -> None:
    data = [int(i) for i in aoc_lube.fetch(2021, 6).split(",")]
    #data = [3, 4, 3, 1, 2]
    
    lanternfish = generate_lanternfish_map()
        
    for num in data:
        lanternfish.update({num: lanternfish[num]+1})

    for _ in range(256):
        new_lanternfish = generate_lanternfish_map()
        
        for i in range(9):
            if i == 0:
                new_lanternfish.update({8: lanternfish[i]})
                new_lanternfish.update({6: lanternfish[i]})
            elif i == 7:
                new_lanternfish.update({i-1: new_lanternfish[i-1] + lanternfish[i]})
            else:
                new_lanternfish.update({i-1: new_lanternfish[i-1] + lanternfish[i]})
            
        lanternfish = new_lanternfish
    
    print(sum_map(lanternfish))
       
def generate_lanternfish_map() -> dict:
    lanternfish = {}
    for i in range(9):
        lanternfish.update({i: 0})
        
    return lanternfish

def sum_map(map: dict) -> int:
    sum = 0
    
    for key in map.keys():
        sum += map[key]
        
    return sum 

if __name__ == "__main__":
    main()