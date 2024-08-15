import aoc_lube

def main(data: str) -> None:
    return

if __name__ == "__main__":
    test_data = [[int(x) for x in list(i)] for i in "2199943210\n3987894921\n9856789892\n8767896789\n9899965678".split("\n")]
    print(test_data)
    
    data = [[int(x) for x in list(i)] for i in aoc_lube.fetch(2021, 9).split("\n")]
    #main(data)