with open("TextInputs\\day04.txt", "r") as open_doc:
    min, max = [line.replace("\n", "") for line in open_doc.readlines()][0].split("-")
    
"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    min, max = [line.replace("\n", "") for line in open_doc.readlines()][0].split("-")
"""

validNumbers = []
validNumbersGrouped = []

for i in range(int(min), int(max)):
    str_i = str(i)
    list_i = list(str_i)
    
    if len(str_i) != 6:
        continue
    
    if not sorted(list_i) == list_i:
        continue
    
    adjacent = False
    group = False
    for j, x in enumerate(list_i[:5]):
        if x == list_i[j+1]:
            adjacent = True
            if list_i.count(x) == 2:
                group = True

    if adjacent:
        validNumbers.append(i)
    if group:
        validNumbersGrouped.append(i)
    
print(len(validNumbers), len(validNumbersGrouped))