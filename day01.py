with open("TextInputs\day01.txt", "r") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

nums = []

lines = ["aa1", "bb23"]

def filterFunc(i):
    if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return True
    return False

for line in lines:
    line = filter(filterFunc, line)
    print(line[0])