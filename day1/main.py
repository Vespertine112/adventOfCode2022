with open('input.txt') as f:
    lines = f.read().split("\n\n")               
    totals = []
    for group in lines:
        numbers = [int(x) for x in group.split("\n")]
        if len(totals) == 0 or sum(numbers) > totals[-1]: 
            totals.append(sum(numbers))

print(totals[-1])
print(sum(totals[-3:]))