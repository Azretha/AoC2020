def findIt(input):
    with open(input) as f:
        expenses = f.readlines()
        
        for i in expenses:
            for j in expenses:
                if int(i) + int(j) == 2020:
                    return (int(i) * int(j))
                    
answer = findIt('input.txt')
print(answer)
