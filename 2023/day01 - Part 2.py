"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]

"""

with open("TextInputs\\day01.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]

nums = []

for line in lines:
    filteredLine = []
    for i, letter in enumerate(line):
        if letter.isdigit():
            filteredLine.append(letter)
            continue
        for num, wNum in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(wNum):
                filteredLine.append(str(num+1))
                break

    nums.append(int(filteredLine[0]+filteredLine[-1]))
    
print(sum(nums))