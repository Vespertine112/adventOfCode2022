with open('input.txt') as f:
    lines = f.read().split("\n\n")               
    totals = []
    for group in lines:
        totals.append(sum([int(x) for x in group.split("\n")]))
    totals.sort()

print(totals[-1])
print(sum(totals[-3:]))