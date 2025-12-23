fileInput = input(">>> ")

with open(fileInput, "r", encoding="utf-8") as f: file = f.readlines()

password = 50
counterP1 = 0
counterP2 = 0

for line in file:
    line = line.rstrip("\n")
    value = int(line[1:])

    if password == 0: counterP1 = counterP1 + 1

    if line[0] == "R":
        firstBound = 100 if password == 0 else password
        if firstBound <= value: counterP2 += 1 + (value - firstBound) // 100
        password = (password - value) % 100


    if line[0] == "L":
        firstBound = 100 if password == 0 else (100 - password)
        if firstBound <= value: counterP2 += 1 + (value - firstBound) // 100
        password = (password + value) % 100

print("Part 1:", counterP1, "// Part 2:", counterP2)