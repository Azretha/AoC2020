import re

def readFile(input):
    passwords = []
    with open(input) as f:
        for line in f:
            m = re.search(r'(\d+)-(\d+)\s(\w):\s(\w+)', str(line))
            passwords.append([m.group(1),m.group(2),m.group(3),m.group(4)])
            #print(m.group(1)) #min
            #print(m.group(2)) #max
            #print(m.group(3)) #char policy
            #print(m.group(4)) #password
    return passwords

answer = readFile('input.txt')

valids = 0

for line in answer:
    minCnt = int(line[0])
    maxCnt = int(line[1])
    c = line[2]
    pw = line[3]
    cnt = len(re.findall(c,pw))
    if (minCnt <= cnt <= maxCnt):
        valids += 1

print('Total number of valid passwords in file: ' + str(valids))

