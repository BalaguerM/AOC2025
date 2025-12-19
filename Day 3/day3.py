fileInput = input(">>> ")

with open(fileInput, "r", encoding="utf-8") as f: file = f.readlines()

totalJoltageP1 = 0

for line in file:
    line = line.rstrip("\n")

    buffer = "00"

    for firstNum in range(len(line)):
        for secondNum in range(firstNum + 1, len(line)):
            candidate = line[firstNum] + line[secondNum]
            if candidate > buffer: buffer = candidate

    totalJoltageP1 += int(buffer)

print("Part 1: ", totalJoltageP1)