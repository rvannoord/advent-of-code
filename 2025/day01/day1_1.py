lines = open("input").read().splitlines()
dial = 50
countzero = 0

for line in lines:
    if not line:              # skip empty lines
        continue
    if line[0] not in ("L", "R"):   # skip invalid/non-instruction lines
        continue

    direction = line[0]
    steps = int(line[1:]) % 100

    if direction == "L":
        dial = (dial - steps) % 100
    else:  # direction == "R"
        dial = (dial + steps) % 100

    if dial == 0:
        countzero += 1

print(countzero)
