def findIt(input):
    with open(input) as f:
        expenses = f.readlines()
        
        for i in expenses:
            for j in expenses:
                for k in expenses:
                    if int(i) + int(j) + int(k) == 2020:
                        return (int(i) * int(j) * int(k))
                    
answer = findIt('input.txt')
print(answer)
