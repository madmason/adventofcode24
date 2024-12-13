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

distance = 0
for i in range(len(leftside)):
    if leftside[i] < rightside[i]:
        distance += rightside[i] - leftside[i]
    else:
        distance += leftside[i] - rightside[i]
print(distance)
