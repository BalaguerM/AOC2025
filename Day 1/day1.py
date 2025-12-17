fileInput = input(">>> ")

with open(fileInput, "r", encoding="utf-8") as f: file = f.readlines()

password = 50
counter_p1 = 0
counter_p2 = 0

for line in file:
    line = line.rstrip("\n")
    value = int(line[1:])

    if password == 0: counter_p1 = counter_p1 + 1

    if line[0] == "R":
        first_k = 100 if password == 0 else password
        if first_k <= value: counter_p2 += 1 + (value - first_k) // 100
        password = (password - value) % 100


    if line[0] == "L":
        first_k = 100 if password == 0 else (100 - password)
        if first_k <= value: counter_p2 += 1 + (value - first_k) // 100
        password = (password + value) % 100

print("Part 1:", counter_p1, "// Part 2:", counter_p2)