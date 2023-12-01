with open("TextInputs\day01.txt", "r") as open_doc:
    lines = [line.replace("\n", "") for line in open_doc.readlines()]

nums = []

def filterFunc(i):
    numL = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if i in numL:
        return True
    return False

for line in lines:
    line = list(filter(filterFunc, list(line)))
    nums.append(int(line[0]+line[-1]))
    
print(sum(nums))