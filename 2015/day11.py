import string

def main(data: str) -> None:
    new_password = increment_password(data)
    while True:
        if password_fits_requirements(new_password):
            print("Part one:", new_password)
            break
        
        new_password = increment_password(new_password)
    
    new_password = increment_password(new_password)
    while True:
        if password_fits_requirements(new_password):
            print("Part two:", new_password)
            break
        
        new_password = increment_password(new_password)

def increment_password(data: str) -> str:
    letter_counter = list(string.ascii_lowercase)
    data_list = list(data)
    
    i = -1
    turnover = False
    
    while True:
        data_list[i] = letter_counter[(letter_counter.index(data_list[i])+1)%26]
        if data_list[i] == "a":
            turnover = True
        else:
            turnover = False
        
        if -i > len(data) or not turnover:
            break
        
        i -= 1
    
    return "".join(data_list)

def password_fits_requirements(data: str) -> bool:
    if requirement_one(data) and requirement_two(data) and requirement_three(data):
        return True
    
    return False

def requirement_one(data: str) -> bool:
    for i in range(len(data)-2):
        substring = data[i:i+3]
        if substring_is_increasing(substring):
            return True
    else:
        return False

def substring_is_increasing(substring: str) -> bool:
    letter_counter = list(string.ascii_lowercase)
    index_first = letter_counter.index(substring[0])
    
    if letter_counter.index(substring[1]) == index_first + 1 and letter_counter.index(substring[2]) == index_first + 2:
        return True
    
    return False

def requirement_two(data: str) -> bool:
    for letter in data:
        if letter in ["i", "o", "l"]:
            return False
    
    return True
    
def requirement_three(data: str) -> bool:
    i = 0; n = 0
    
    while True:
        if i >= len(data)-1:
            return False
        
        if data[i:i+2] == data[i]*2:
            n += 1
            if n == 2:
                return True
            i += 1
        
        i += 1
          

if __name__ == "__main__":
    data = "vzbxkghb"
    main(data)