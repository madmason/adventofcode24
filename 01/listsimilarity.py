import csv

leftside = []
rightside = []
with open('input.csv') as csvFile:
    spamreader = csv.reader(csvFile, delimiter=',')
    for row in spamreader:
        leftside.append(int(row[0]))
        rightside.append(int(row[1]))
leftside.sort()
rightside.sort()

similarityScore = 0
rightDict = {}
for x in rightside:
    if x in rightDict:
        rightDict[x] += 1
    else:
        rightDict[x] = 1

for x in leftside:
    if x in rightDict:
        similarityScore += x * rightDict[x]

print(similarityScore)
