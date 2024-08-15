import aoc_lube

def part_one(data: list[list[list[str]]]) -> int:
    occurence = 0
    
    for couple in data:
        for num in couple[1]:
            if len(num) in [2, 3, 4, 7]:
                occurence += 1
    
    return occurence

# this entire thing ugs in the ugly
# it works, but boy is she ugly
# speed should be fine though
def part_two(data: list[list[list[str]]]) -> int:
    output = 0
    
    for couple in data: 
        translation_layer = {}
        to_be_removed = []
        
        # finds 1, 4, 7, and 8 in one iteration
        for num in couple[0]:
            if len(num) == 2:
                sorted_num = "".join(sorted(list(num)))
                translation_layer.update({sorted_num: 1, 1: sorted_num})
                to_be_removed.append(num)
            elif len(num) == 3:
                sorted_num = "".join(sorted(list(num)))
                translation_layer.update({sorted_num: 7, 7: sorted_num})
                to_be_removed.append(num)
            elif len(num) == 4:
                sorted_num = "".join(sorted(list(num)))
                translation_layer.update({sorted_num: 4, 4: sorted_num})
                to_be_removed.append(num)
            elif len(num) == 7:
                sorted_num = "".join(sorted(list(num)))
                translation_layer.update({sorted_num: 8, 8: sorted_num})
                to_be_removed.append(num)
        
        for num in to_be_removed:
            couple[0].remove(num)
        
        three = find_three(couple[0], translation_layer)
        couple[0].remove(three)
        sorted_three = "".join(sorted(list(three)))
        translation_layer.update({sorted_three: 3, 3: sorted_three})
        
        zero = find_zero(couple[0], translation_layer)
        couple[0].remove(zero)
        sorted_zero = "".join(sorted(list(zero)))
        translation_layer.update({sorted_zero: 0, 0: sorted_zero})
        
        six_nine = find_six_nine(couple[0], translation_layer)
        for num in six_nine:
            couple[0].remove(num)
        sorted_six = "".join(sorted(list(six_nine[0])))
        sorted_nine = "".join(sorted(list(six_nine[1])))
        translation_layer.update({sorted_six: 6, 6: sorted_six, sorted_nine: 9, 9: sorted_nine})
        
        if len(find_difference(couple[0][0], translation_layer[9])) == 1:
            five = couple[0][0]
            two = couple[0][1]
        else:
            five = couple[0][1]
            two = couple[0][0]
            
        sorted_two = "".join(sorted(list(two)))
        sorted_five = "".join(sorted(list(five)))
        translation_layer.update({sorted_two: 2, 2: sorted_two, sorted_five: 5, 5: sorted_five})
        
        for i, num in enumerate(couple[1]):
            couple[1][i] = str(translation_layer["".join(sorted(list(num)))])
        
        print(int("".join(couple[1])))
        output += int("".join(couple[1]))
        #print(output)
        
    return output

def find_six_nine(left_couple, translation_layer) -> list[str]:
    sixes = []
    
    seven = translation_layer[7]
    
    for num in left_couple:
        if len(num) == 6:
            sixes.append(num)
    
    for letter in seven:
        if letter not in sixes[0]:
                return [sixes[0], sixes[1]]
    
    return [sixes[1], sixes[0]]

def find_zero(left_couple, translation_layer) -> str:
    four = list(translation_layer[4])
    
    for letter in translation_layer[1]:
        four.remove(letter)
        
    three = translation_layer[3]
    
    for letter in four:
        if letter in three:
            middle = letter
            
    for num in left_couple:
        if len(num) == 6 and middle not in num:
            return num

def find_three(left_couple, translation_layer) -> str:
    one = list(translation_layer[1])
    
    for num in left_couple:
        if len(num) == 5:
            # for-else loop, 7 needs to fit inside 3, but can't fit inside 2 or 5
            # 
            for letter in one:
                if letter not in num:
                    break
            else:
                return num
            
def find_difference(num1, num2) -> set[str]:
    output = []
    
    for letter in num1:
        if letter not in num2:
            output.append(letter)
    for letter in num2:
        if letter not in num1:
            output.append(letter)
            
    return set(output)

def main(data: list[list[list[str]]]) -> None:
    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
    
if __name__ == "__main__":
    test_data = [[x.split() for x in "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf".split(" | ")]]
    #main(test_data)
    
    data = [[x.split() for x in i.split(" | ")] for i in aoc_lube.fetch(2021, 8).split("\n")]
    main(data)