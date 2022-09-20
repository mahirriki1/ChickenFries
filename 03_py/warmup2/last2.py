def last2(str):
    if len(str) < 0:
        return 0
    count = 0 
    end = str[len(str)-2:]
    for i in range(len(str)-2):
        substring = str[i:i+2]
        if substring == end:
            count += 1
    return count