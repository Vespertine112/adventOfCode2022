import math

# Build letter map
letters = 'abcdefghijklmnopqrstuvwxyz'
valMap = {}
counter = 1
for char in (letters+letters.upper()):
    valMap[char] = counter
    counter+=1

with open('input.txt') as f:
    lines = f.read().split("\n")
    totalSum = 0
    groupSize = 3
    groupCounter = 0
    groupArray = []

    for group in lines:
        # Part Two
        if (True):
            groupCounter +=1
            groupArray.append(group)
            if groupCounter == groupSize:
                groupCounter = 0
                duplicates = []
                comboMap = {}
                for x in range(len(groupArray)):
                    group = groupArray[x]
                    if x == 0:
                        for char in group:
                            comboMap[char] = {'value': 1, 'seen':False}
                        continue
                    for key,value in comboMap.items():
                        comboMap[key]['seen'] = False
                    for char in group:
                        if comboMap.get(char) != None and comboMap[char].get('seen') == False:
                            comboMap[char]['value'] += 1
                            comboMap[char]['seen'] = True
                for key,value in comboMap.items():
                    if value['value'] == 3:
                        totalSum += valMap[key]
                groupArray = []
        # Part one
        if (False):
            duplicates = []
            comboMap = {}
            total = 0
            firstHalf = group[:math.ceil((len(group)/2))]
            secondHalf = group[math.ceil(len(group)/2):]
            for char in firstHalf:
                comboMap[char] = True
            for char in secondHalf:
                if comboMap.get(char) != None and comboMap.get(char) == True:
                    duplicates.append(char)
                    comboMap[char] = False
            for char in duplicates:
                total += valMap[char]
            totalSum += total
    print(totalSum)


