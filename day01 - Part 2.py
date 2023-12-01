"""
with open("TextInputs\\testCases.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]

"""

with open("TextInputs\\day01.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]

nums = []

def filterFunc(i):
    if i.isdigit():
        return True
    return False

for line in lines:
    line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
    line = list(filter(filterFunc, list(line)))
    nums.append(int(line[0]+line[-1]))
    
print(sum(nums))