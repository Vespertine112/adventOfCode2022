
rpc = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
map = {
    "A":"X",
    "B":"Y",
    "C":"Z",
}
wins = {
    "Y":"C",
    "Z":"A",
    "X":"B"
}
lose = {
    "C":"Y",
    "A":"Z",
    "B":"X"
}
winMap = {
    "C":"X",
    "A":"Y",
    "B":"Z"
}
total = 0
with open('input.txt') as f:
    lines = f.read().split("\n")
    for group in lines:
        turn = group.split(" ")
        # Strat translation
        if (True):
            if turn[1] == "Y": turn[1] = map[turn[0]]
            elif turn[1] == "Z": turn[1] = winMap[turn[0]]
            elif turn[1] == "X": turn[1] = lose[turn[0]]
        # catch
        if (len(turn) == 1 or len(turn)== 0):continue
        # tie
        elif (rpc[turn[0]] == rpc[turn[1]]): total += 3 + rpc[turn[1]]
        # lose
        elif (wins[turn[1]] == turn[0]): total += rpc[turn[1]]
        # win
        else: total += 6+rpc[turn[1]]
    print(total)