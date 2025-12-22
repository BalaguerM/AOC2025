fileInput = "Day 4\\inputD4.txt"

with open(fileInput, "r", encoding="utf-8") as f: file = f.readlines()

array = [list(line.strip()) for line in file]
directions = (-1, -1), (1, 1), (0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1)
countP1 = 0
countP2 = 0

while True:
    for x in range(len(array)):
        for y in range(len(array[x])):
            buffer = 0
            if array[x][y] == "@":            
                for dx, dy, in directions:
                    if 0 <= x+dx < len(array) and 0 <= y+dy < len(array[x]):
                        if array[x+dx][y+dy] == "@": buffer += 1
                if buffer < 4: 
                    countP1 += 1
                    array[x][y] = "."
                    print(countP1)



# Answer: 8768