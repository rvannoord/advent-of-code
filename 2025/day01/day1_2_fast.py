countzero = 0
dial = 50
lastdial = 50

with open("input") as f:
    for line in f:
        move = int(line[1:])
        countzero += move // 100  # full hundreds count

        if line[0] == "L":
            dial -= move % 100
        else:  # assuming only 'L' or 'R'
            dial += move % 100

        # Wrap dial around 0-99
        if dial < 0:
            dial += 100
            if lastdial != 0:
                countzero += 1
        elif dial > 99:
            dial -= 100
            if dial != 0:
                countzero += 1

        if dial == 0:
            countzero += 1

        lastdial = dial

print(countzero)
