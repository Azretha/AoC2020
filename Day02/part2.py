import re

##
## not a working solution yet
##

def readFile(input):
    passwords = []
    with open(input) as f:
        for line in f:
            m = re.search(r'(\d+)-(\d+)\s(\w):\s(\w+)', str(line))
            passwords.append([m.group(1),m.group(2),m.group(3),m.group(4)])
    return passwords

answer = readFile('inputsmall.txt')

valids = 0

for line in answer:
    pos1 = int(line[0])+1 #correcting for zero-based indexing
    pos2 = int(line[1])+1 #same
    c = str(line[2])
    pw = str(line[3])

    if c in pw:
        # if both positions are in index range
        if (pos1 in range(len(pw))) and (pos2 in range(len(pw))):
            if ((pw[pos1] == c and pw[pos2] != c) or (pw[pos1] != c and pw[pos2] == c)):
                print(pw)
                print(pw[pos1])
                print(pw[pos2])
                #valids += 1               
        elif ((pos1 in range(len(pw))) and (pos2 not in range(len(pw)))):
            if pw[pos1] == c:
                print(pw)
                print(pw[pos1])
                #valids += 1                
        elif ((pos2 in range(len(pw))) and (pos1 not in range(len(pw)))):
            if pw[pos2] == c:
                print(pw)
                print(pw[pos2])
                #valids += 1
        else:
            pass

print('Total number of valid passwords in file: ' + str(valids))

