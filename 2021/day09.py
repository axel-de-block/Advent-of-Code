import aoc_lube
    
def find_low_points(data: list[list[int]]) -> list[tuple[int]]:
    low_points = []
    processed_points = []
    
    for y in range(len(data)):
        for x in range(len(data[0])):
            adjacents = find_adjacents_coords((x, y), len(data[0])-1, len(data)-1)
            val_coord = data[y][x]
            
            for adjacent in adjacents:
                if val_coord >= data[adjacent[1]][adjacent[0]]:
                   break
            else:
                low_points.append((x, y))
                
            processed_points.append((x, y))
            
    return low_points

def find_adjacents_coords(coord: tuple[int], max_x: int, max_y: int) -> list[tuple[int]]:
    output = []
    
    if not coord[0] <= 0:
        output.append((coord[0]-1, coord[1]))
        
    if not coord[1] <= 0:
        output.append((coord[0], coord[1]-1))
        
    if not coord[0] >= max_x:
        output.append((coord[0]+1, coord[1]))
        
    if not coord[1] >= max_y:
        output.append((coord[0], coord[1]+1))
    
    return output

def calc_risk_level(low_points: list[tuple[int]], data: list[list[int]]) -> int:
    output = 0
    
    for coord in low_points:
        output += data[coord[1]][coord[0]] + 1
        
    return output

def find_basin(low_points: list[tuple[int]], data: list[list[int]]):
    sizes = []
    
    for low_point in low_points:
        sizes.append(check_point(low_point[0], low_point[1], data))
        
    return sizes
    
# uses recursion to search for all attached points in a basin
def check_point(x: int, y: int, data: list[list[int]]):
    size = 0
    
    if data[x][y] == '.' or data[x][y] == 9:
        return size
    
    data[x][y] = '.'
    size += 1
    
    if y+1 < len(data[0]):
        size += check_point(x, y+1, data)
    if y-1 >= 0:
        size += check_point(x, y-1, data)
    if x+1 < len(data):
        size += check_point(x+1, y, data)
    if x-1 >= 0:
        size += check_point(x-1, y, data)
        
    return size

def main(data: list[list[int]]) -> None:
    low_points = find_low_points(data)
    print("Part one:", calc_risk_level(low_points, data))
    
    basin_sizes = sorted(find_basin(low_points, data))[::-1]
    print("Part two:", basin_sizes[0]*basin_sizes[1]*basin_sizes[2])

if __name__ == "__main__":
    test_data = [[int(x) for x in list(i)] for i in "2199943210\n3987894921\n9856789892\n8767896789\n9899965678".split("\n")]
    #main(test_data)
    
    data = [[int(x) for x in list(i)] for i in aoc_lube.fetch(2021, 9).split("\n")]
    main(data)