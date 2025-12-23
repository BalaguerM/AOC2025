fileInput = "Day 5\\inputD5.txt"

with open(fileInput, "r", encoding="utf-8") as f: file = f.readlines()

array = [line.strip() for line in file]

ids = array[array.index("")+1:]

ranges = []
rangedIds = []
counterP1 = 0
counterP2 = 0

for value in array[:array.index("")]: ranges.append(value.split("-"))

for interval in ranges: rangedIds.append([range(int(ranges[ranges.index(interval)][0]), int(ranges[ranges.index(interval)][1]))])

for idx in ids:
    for pos in range(len(rangedIds)):
        if int(idx) in rangedIds[pos][0]:
            counterP1 += 1
            break

print(counterP1)